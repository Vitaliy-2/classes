"""
Lesson 14
31.01.2024

- Повторение
- Порядок аргументов
- kwargs (множественные именованные аргументы)
- Области видимости
- name()
- Основы аннотаций типов
- Архитектура приложений на функциях
- Знакомство с mypy (pip install mypy)
"""


# Параметры функции - это переменные которые мы можем передать в функцию.
# Позиционные аргументы - аргументы которые мы передаем в функцию по порядку.
# Именованные аргументы - аргументы которые мы передаем в функцию по имени.
# Параметры по умолчанию - параметры которые имеют значение по умолчанию.


# Порядок аргументов
# def my_func(a, b, c, *args d=10, e=20, **kwargs,):

# def my_func(a, b, c, d=10, e=20, *args, **kwargs):
#     print(f'{a=}')
#     print(f'{b=}')
#     print(f'{c=}')
#     print(f'{d=}')
#     print(f'{e=}')
#     print(f'{args=}')
#     print(f'{kwargs=}')


# my_func(1, 2, 3)


# def message_to_group(message, *names, group_name='Python315'):
#     print(names)
#     print(f'{message}, {group_name}!')
#     print(f'{message}, {', '.join(names)}!')
#
#
# message_to_group('Привет', 'Иван', 'Маша', 'Петя', 'Вася', group_name='Python316')
# names_list = ['Иван', 'Маша', 'Петя', 'Вася']
#
#
# # print(*names_list)
# # print('Иван', 'Маша', 'Петя', 'Вася')
#
#
# def kwargs_printer(**kwargs):
#     print(kwargs)
#     print(*kwargs)

#
# kwargs_printer(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
#
# person_dict = {
#     'name': 'Иван',
#     'age': 20,
#     'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
# }
#
# # print(**person_dict)
#
# special_for_print_dict = {
#     'sep': ' - ',
#     'end': '!!!'
# }
#
# print('Hello', 'Python', 'Developers', **special_for_print_dict)
# print('Hello', 'Python', 'Developers', sep=' - ', end='!!!')
#
#
# def get_message(message='Привет', name='Тимур', group='Python315'):
#     return f'{message}, {name} из группы {group}!'
#
#
# func_params_dict = {
#     'message': 'Hello',
#     'name': 'Оксана',
#     'group': 'Python316'
# }
# print()
# print(get_message(**func_params_dict))

# # TODO Практика - функция count avarage mark
# """
# Напишите функцию count_avarage_mark которая принимает **kwargs
# Она разбирает словарь методом get и добывает из него
# - имя студента (name)
# - фамилию студента (surname)
# - список оценок студента (marks)
#
# Считает среднюю оценку и выводит сообщение
# Владимир Монин имеет средний балл 4.5
# """
#
# students_dict = {
#     'name': 'Владимир',
#     'surname': 'Иванов',
#     'marks': [5, 4, 4, 4, 5],
#     'group': 'Python333'
# }
#

# def count_avarage_mark(**student):
# def count_avarage_mark(name='Иван', surname:'Сергеев', marks=[1,1])
# def count_avarage_mark(name, surname, marks)

# def count_avarage_mark(**student):
#     name = student.get('name')
#     surname = student.get('surname')
#     marks = student.get('marks')
#
#     avarage_mark = round(sum(marks) / len(marks), 2)
#     return f'{name} {surname} имеет средний балл: {avarage_mark}'
#
#
# print(count_avarage_mark(**students_dict))


# def count_average_mark(group='Python315', **student):
#     name = student.get('name')
#     surname = student.get('surname')
#     marks = student.get('marks')
#
#     average_mark = round(sum(marks) / len(marks), 2)
#     return f'{name} {surname} из группы {group} имеет средний балл: {average_mark}'
#
#
# students_dict = {
#     'name': 'Владимир',
#     'surname': 'Иванов',
#     'marks': [5, 4, 4, 4, 5],
#     'group': 'Python333'
# }

# def count_avarage_mark(**student):
# def count_avarage_mark(name='Иван', surname:'Сергеев', marks=[1,1])
# def count_avarage_mark(name, surname, marks)

#
# print(count_average_mark(name='Иван', surname='Иванов', marks=[5, 4, 4, 4, 5]))
# print(count_average_mark(**students_dict))

# Области видимости (scope)
# Built-in scope - встроенная область видимости (Живут функции и классы Python, print, len, sum, dict, list, set, tuple)
# Global scope - глобальная область видимости (Наш файл, переменные, функции, классы)
# Local scope - локальная область видимости (Вселенная внутри функции)
# Nonlocal scope - нелокальная область видимости (Вселенная внутри функции внутри функции)

# name = 'Владислав'
# NAME = 'Гончик'
#
#
# def say_my_name(message):
#     name = 'Иван'
#     print(message, name)
#
#
# def say_my_name2(message):
#     name = 'Тимур'
#     print(message, name)
#
#
# def say_my_name3(message):
#     name = 'Александр'
#     print(message, name)


# def say_my_name4(message):
#     print(message, name)
#
#
# def say_my_name5(message, name=NAME):
#     print(message, name)
#
#
# say_my_name('Привет')
# say_my_name4('Привет')
# print(name)

# Global - объявление переменной в глобальной области видимости

# a = 1
# print(a)
#
#
# def some_func():
#     global a, b
#     a = 2
#     b = 5
#     print(a)


# some_func()
# print(a)
# print(b)

# def outer_func():
#     # nonlocal a  # SyntaxError: no binding for nonlocal 'a' found
#     a = 3
#     print(f'outer_func: {a}')
#
#     def inner_func():
#         # nonlocal a
#         a = 2
#         print(f'inner_func: {a}')
#
#     inner_func()
#     print(f'outer_func: {a}')
#
#
# print(f'global: {a}')
# outer_func()
# print(f'global: {a}')

# Архитектура приложений на функциях
### Начало файла
"""
Документация модуля
Программа для поиска фильмов Marvel по фазам
Пользователь вводит номер фазы (1,2,3,4) а программа выводит список фильмов
Функции:
1. Чтение данных из JSON файла
2. Расшифровка стадий (принимает номер стадии, возвращает название)
3. Поиск фильмов по стадии (принимает номер стадии, возвращает список фильмов)
4. Функция main - точка входа в программу


Описание модуля
Список функций
"""
# импорты
import json
from pprint import pprint
# константы
FILE_PATH = '../data/marvel.json'

# объявление функций

"""
Объявление функий, с документацией, аннотациями типов
"""

# функция main

"""
Объявление функции main. Внутри есть переменные, которые мы можем использовать
Вызовы других функций, и все что нужно для работы программы.
Она пишется так, что вызвав её вы запустите всю программу
"""

# Аннотация типов (в базовом варианте)
# def get_sum(a: int, b: int) -> int:  - >
# Базовые типы данных аннотации типов
# int, float, str, bool, list, set, tuple, dict, Any, None


def read_json_file(file_path: str = FILE_PATH) -> dict:
    """
    Функция, которая принимает путь к файлу и возвращает словарь
    :param file_path: Путь к файлу
    :return: Словарь
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_phase_name_by_number(phase_number: int) -> str | None:
    """
    Функция, которая принимает номер фазы и возвращает название фазы
    :param phase_number: Номер фазы
    :return: Название фазы
    """
    phase_dict = {
        1: 'Первая фаза',
        2: 'Вторая фаза',
        3: 'Третья фаза',
        4: 'Четвертая фаза',
        5: 'Пятая фаза',
        6: 'Шестая фаза',
    }

    return phase_dict.get(phase_number)


def get_movies_by_phase(phase_number: str, marvel_dict: dict) -> list:
    """
    Функция, которая принимает номер фазы и словарь marvel
    и возвращает список фильмов
    :param phase_number: Номер фазы
    :param marvel_dict: Словарь marvel
    :return: Список фильмов
    """
    if phase_number:
        return [movie for movie in marvel_dict.values() if phase_number.lower() == movie['stage'].lower()]
    else:
        return []


def main():
    """
    Точка входа в программу
    :return: None
    """
    # 1. Чтение данных из JSON файла
    marvel_dict = read_json_file(file_path=FILE_PATH)

    # 2. Получение номера фазы
    phase_number = int(input('Введите номер фазы: '))

    # 3. Расшифровка стадий (принимает номер стадии, возвращает название)
    phase_name = get_phase_name_by_number(phase_number)

    # 4. Поиск фильмов по стадии (принимает номер стадии, возвращает список фильмов)
    movies_list = get_movies_by_phase(phase_number, marvel_dict)

    # 5. Вывод результата
    print(f'Фаза: {phase_name}')
    pprint(f'Фильмы: {movies_list}')


if __name__ == '__main__':
    main()
