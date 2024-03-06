"""
Lesson 13
29.01.2024
- datetime
- текущая дата и время
- strftime
- timedelta
- функции
- позиционные аргументы
- аргумент по умолчанию
- docstring (документация)
- args (множественные позиционные аргументы)

- Завтра
- Порядок аргументов
- kwargs (множественные именованные аргументы)
- Основы аннотаций типов?


Активация виртуального окружения
env/Scrips/activate - Windows
env/bin/activate - Linux and MacOS

Деактивация виртуального окружения
env/Scripts/deactivate - Windows
env/bin/deactivate - Linux and MacOS

# 336 vs 338 у Гугла? Почему?
"""

"""

"""
import datetime
import calendar
import locale

# locale - модуль для работы с локалью
# setlocale - устанавливает локаль
# LC_ALL - константа для установки локали (все категории)
# 'ru_RU.UTF-8' - код локали
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# Текущая дата и время
"""
Мы получаем данные в формате 2021-01-24 14:55:00.000000
После . мы получаем микросекунды
"""
now = datetime.datetime.now()
print(f'Текущая дата и время: {now}')  # 2021-01-24 14:55:00.000000

# Получаем текущий день недели
"""
Мы получаем данные в формате чисел
0 - понедельник
6 - воскресенье
"""
day_of_week = now.weekday()
print(f'Текущий день недели: {day_of_week}')  # 6

print(f'Текущий день недели: {calendar.day_name[day_of_week]}')  # Sunday (Без русской локали)

# Получаем дни недели на русском языке

# Форматирование даты и времени
"""
.strftime - инструмент для форматирования даты и времени
%Y - год
%m - месяц
%d - день
%H - час
%M - минуты
%S - секунды
%a - день недели (сокращенный)
%A - день недели (полный)
%b - месяц (сокращенный)
%B - месяц (полный)
"""

# Текущее время в формате понедельник, 29 января 2024 года 18-15
print(now.strftime('%A, %d %B %Y года %H-%M'))  # Sunday, 24 January 2021 года 14-55

# Разница между датами (сколько осталось до следующего Нового Года?)
date1 = datetime.datetime(2024, 12, 31)
date2 = datetime.datetime.now()

delta = date1 - date2
print(delta)  # 365 days, 9:04:11.000000
print(type(delta))  # <class 'datetime.timedelta'>
# Форматируем в месяцы и дни
# delta.days - мы можем вытащить дни из объекта timedelta
print(
    f'До нового года осталось: {delta.days // 30} месяцев и {delta.days % 30} дней')  # До нового года осталось: 11 месяцев и 6 дней

# Посмотрим какие еще поля есть у объекта delta (только пользовательские)
# print(dir(delta))

# days - количество дней
# seconds - количество секунд
# microseconds - количество микросекунд
# total_seconds - общее количество секунд

print(delta.days)
print(delta)
print(delta // 30)  # Я считал целые месяцы, но получил дни. Ошибка
print(delta.days // 30)  #

# Функции
# Функция - это набор инструкций, которые выполняются при вызове функции
# Вызов функции происходит через ее имя и круглые скобки ()
print('Hello, Python315!')

# Синтаксис функции
"""
def - ключевое слово для создания функции (definition - определение)
имя функции
параметры функции (если они есть)
тело функции
"""

"""
Правила нейминга функций
1. Имя функции должно быть глаголом
2. Имя функции должно быть с маленькой буквы
3. Имя функции должно быть в стиле snake_case
4. Имя функции должно быть понятным и описывать то, что она делает
"""


def say_hello_to_python315():
    print('Hello, Python315!')


def say_hello_to_python316():
    print('Hello, Python316!')


# Вызов функции
say_hello_to_python315()
say_hello_to_python316()


# Работа с 1 аргументом и принтом
def say_hello_to_group(group_name):
    print(f'Привет, {group_name}!')


say_hello_to_group('Python315')
say_hello_to_group('Python316')

message = say_hello_to_group('Python315')
print(message)  # None


# Возвращаем значение из функции
def say_hello_to_group2(group_name):
    return f'Привет, {group_name}!'


message = say_hello_to_group2('Python315')
print(message)  # Привет, Python315!

print(say_hello_to_group2('Python315'))  # Привет, Python315!


# Позиционные аргументы
def get_message(name, message):
    return f'Имя: {name}, сообщение: {message}'


print(get_message('Сергей', 'Привет!'))  # Имя: Сергей, сообщение: Привет, Python315!
print(get_message('Привет', 'Павел'))  # Имя: Привет!, сообщение: Сергей


# print(get_message('Сергей'))  # TypeError: get_message() missing 1 required positional argument: 'message'


# Аргумент "по умолчанию" (default) (или именованный аргумент)
def get_message(name, message='Привет!'):
    return f'Имя: {name}, сообщение: {message}'


print(get_message('Сергей'))  # Имя: Сергей, сообщение: Привет!
print(get_message('Сергей', 'Привет, Python315!'))  # Имя: Сергей, сообщение: Привет, Python315!


# print()
# print(sep='')

# Немного усложняем пример
def get_message(fist_name, last_name, message='Привет!'):
    return f'Имя: {fist_name}. Фамилия: {last_name}, сообщение: {message}'


result = get_message(
    message='Привет, Python315!',
    fist_name='Сергей',
    last_name='Петров'
)
print(result)  # Имя: Сергей Петров, сообщение: Привет, Python315!

user_dict = {
    'fist_name': 'Сергей',
}


def get_key_value_tuple(dict_):
    key_str = str(dict_.keys())
    value_str = str(dict_.values())
    return key_str, value_str


result = get_key_value_tuple(user_dict)
print(result)  # ('fist_name', 'Сергей')

# TODO Практика - функция get_cities_set
"""
На вход принимает переменную типа list[dict]
На выходе возвращает сет из dict['name']
"""

from data.cities import cities_list


def get_set_from_cities_list(cities_list):
    """
    Функция которая принимает список словарей с городами
    в игре "Города" и возвращает сет с названиями городов
    :param cities_list: Список словарей с городами
    :return: Сет с названиями городов
    """
    return {city['name'] for city in cities_list}


result = get_set_from_cities_list(cities_list)
print(result)


# Args - множественные позиционные аргументы

def get_sum_2_integers(a, b):
    return sum((a, b))


def get_sum_3_integers(a, b, c):
    return sum((a, b, c))


def get_sum(*integers):
    print(integers)
    print(*integers)
    print(type(integers))
    return sum(integers)


# some_list = [1, 2, 3, 4, 5]
# print(*some_list)
# print(some_list[0], some_list[1], some_list[2], some_list[3], some_list[4])

print(get_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
print(get_sum(1, 2, 3, 4, 5))  # 15

# TODO Практика - функция is_palinrome
"""
Напишите функцию, которая принимает *palindrome (n-ое количество аргументов строк)
и возвращает словарь где ключ это слово, а значение это True или False в зависимости
от того является ли слово палиндромом или нет
По типу
def is_palindrome(*palindrome):
...

result = is_palindrome('шалаш', 'казак', 'привет', 'топот')
print(result)

{"шалаш": True, "казак": True, "привет": False, "топот": True}
....
"""


# def is_palindrome(*palindrome):
#     return {word: word == word[::-1] for word in palindrome}

def is_palindrome(*palindrome):
    result = {}
    for word in palindrome:
        row_word = word.replace(' ', '').lower()
        result[word] = row_word == row_word[::-1]
    return result

result = is_palindrome('шалаш', 'казак', 'привет', 'топот', 'А роза упала на лапу Азора')
print(result)
# {'шалаш': True, 'казак': True, 'привет': False, 'топот': True}


def is_palindrome(*palindrome):
    # return {word: word == word[::-1] for word in palindrome}
    return {word: word.replace(' ', '').lower() == word.replace(' ', '').lower()[::-1] for word in palindrome}

result = is_palindrome('шалаш', 'казак', 'привет', 'топот', 'А роза упала на лапу Азора')
print(result)