# HomeWork 17-18. Декоратор валидации пароля
import csv
from typing import Callable

# Входные данные
LEN_THRESHOLD = 8
DIGIT_THRESHOLD = 1
UPPERCASE_THRESHOLD = 1
LOWERCASE_THRESHOLD = 1
SPEC_SYMBOL_THRESHOLD = 1
SPEC_SYMBOLS = '!@#$%^&*()_+'

# Декоратор проверки сложности пароля


def password_checker(func: Callable) -> Callable:
    """
    Декоратор проверки пароля на надежность.
    :param func: Функция, которая содержит пароль
    :return: Сообщение об ошибке, либо одобрения пароля. (принт)
    """
    def wrapper(password: str) -> str:
        if len(password) < LEN_THRESHOLD:
            return 'Пароль слишком короткий'
        if sum([1 for i in password if i.isdigit()]) < DIGIT_THRESHOLD:
            return 'Пароль должен содержать хотя бы одну цифру'
        if sum([1 for i in password if i.isupper()]) < UPPERCASE_THRESHOLD:
            return 'Пароль должен содержать хотя бы одну заглавную букву'
        if sum([1 for i in password if i.islower()]) < LOWERCASE_THRESHOLD:
            return 'Пароль должен содержать хотя бы одну строчную букву'
        if sum([1 for i in password if i in SPEC_SYMBOLS]) < SPEC_SYMBOL_THRESHOLD:
            return 'Пароль должен содержать хотя бы один спецсимвол'
        return func(password)
    return wrapper


@password_checker
def register_user(password: str) -> str:
    """
    Фенкция принимает пароль в виде строки
    :param password: пароль
    :return: f строку
    """
    return f'Пользователь успешно зарегистрирован с паролем: {password}'


print('Задание №1')
print(register_user('34Fds#4fdg65'))  # Успешная проверка
print(register_user('34Fds#4'))  # Пароль не прошел проверку


#  Часть 2. Декоратор с параметрами
def password_validator(min_length: int = 8, min_uppercase: int = 1,
                       min_lowercase: int = 1, min_special_chars: int = 1):
    """
    Декоратор с параметрами для проверки пароля
    :param min_length: Проверка на минимальную длину пароля
    :param min_uppercase: Проверка на вхождение заглавных букв
    :param min_lowercase: Проверка на вхождение букв нижнего регистра
    :param min_special_chars: Проверка на вхождение спецзнаков
    :return: Ответ об ошибках или положительном ответе (пароль прошел проверку)
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError('Пароль слишком короткий')
            if sum([1 for i in password if i.isupper()]) < min_uppercase:
                raise ValueError('Пароль должен содержать не менее двух заглавных букв')
            if sum([1 for i in password if i.islower()]) < min_lowercase:
                raise ValueError('Пароль должен содержать не менее двух строчных букв')
            if sum([1 for i in password if i in SPEC_SYMBOLS]) < min_special_chars:
                raise ValueError('Пароль должен содержать не менее двух спецсимволов')
            return func(username, password)
        return wrapper
    return decorator

# Проверка правильности ввода имени


def username_validator(func: Callable) -> Callable:
    """
    Функция проверяет правильность ввода имени.
    :param func: Отдаёт имя.
    :return: Положительный или отрицательный ответ
    """
    def wrapper(username: str, password: str) -> str:
        if ' ' in username:
            raise ValueError('Имя пользователя не должно содержать пробелы')
        else:
            print('Имя пользователя и пароль успешно прошли проверки.')
        return func(username, password)
    return wrapper


@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
@username_validator
def register_user2(username: str, password: str) -> None:
    """
    Функция проходит через два декоратора для проверки имени и пароля
    :param username: Имя пользователя
    :param password: Пароль
    :return: При положительном результате запись в csv файл
    """
    with open('users.csv', 'a', encoding='windows-1251') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        writer.writerow([username, password])


print('Задание №2')
register_user2('Vitaliy', '12dF@#dfDgdgfgr')
