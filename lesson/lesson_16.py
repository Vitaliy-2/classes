"""
Lesson 16
07.02.2024
- Анонимные функции (lambda)
- Map,
- Generators
- All, Any
- Filter, Sorted
"""
from pprint import pprint
from typing import Callable, Iterator


# Анонимные функции (lambda)
# get_sum = lambda x, y: x + y


# def get_sum2(x, y):
#     return x + y
#
#
# print(get_sum2(1, 2))

# Map - функия высшего порядка, принимает функцию и итерируемый объект
# Возвращает map-объект
#
# user_integesr_input = ['1', '2', '3', '4', 'банан']
# result_integers = [int(i) if i.isdigit() else None for i in user_integesr_input]

# result_integers = []
# for i in user_integesr_input:
#     if i.isdigit():
#         result_integers.append(int(i))
#     else:
#         result_integers.append(None)

# result_integers = list(map(int, user_integesr_input))
# result_integers = list(map(lambda x: int(x) if x.isdigit() else None, user_integesr_input))
# print(result_integers)


# def get_int_or_none(x: int) -> int:
#     """
#     Это можно было бы заменить на lambda!
#     :param x:
#     :return:
#     """
#     if x.isdigit():
#         return int(x)
#     else:
#         return None


# result_integers = list(map(get_int_or_none, user_integesr_input))


# def map_analog(func: callable, iterable: list | set | tuple) -> list:
#     result = []
#     for i in iterable:
#         result.append(func(i))
#     return result

#
# slag_list = ['python-dict', 'python-list', 'python-tuple', 'python-set']
#
#
# def get_url_by_slag(slag: str) -> str:
#     return f'https://www.python.org/{slag}/'


# result_urls_by_my_function = map_analog(get_url_by_slag, slag_list)
# reuslt_urls_by_map = list(map(get_url_by_slag, slag_list))

# Это же с lambda
# result_urls_by_my_function = map_analog(lambda slag: f'https://www.python.org/{slag}/', slag_list)
# reuslt_urls_by_map = list(map(lambda slag: f'https://www.python.org/{slag}/', slag_list))

# Это же через компрехеншен
# result_urls_by_my_function = [lambda x: f'https://www.python.org/{x}/' for x in slag_list] # Не работает
# result_urls_by_my_function2 = [f'https://www.python.org/{slag}/' for slag in slag_list]
#
# print(result_urls_by_my_function)
# print(result_urls_by_my_function2)
#
# reuslt_urls_by_map = (map(lambda slag: f'https://www.python.org/{slag}/', slag_list))
# print(type(reuslt_urls_by_map))

# print(next(reuslt_urls_by_map))
# print(next(reuslt_urls_by_map))
# print(next(reuslt_urls_by_map))
# print(next(reuslt_urls_by_map))
# print(next(reuslt_urls_by_map))

# for url in reuslt_urls_by_map:
#     print(url)

# аналог цикла for с использованием map next и try except StopIteration
# reuslt_urls_by_map = (map(lambda slag: f'https://www.python.org/{slag}/', slag_list))
#
# while True:
#     try:
#         print(next(reuslt_urls_by_map))
#     except StopIteration:
#         break

# Список for i in range 100000000000000000 чтобы получить memory error

# memory_list = [i for i in range(1000**1000)]
# generator = (i for i in range(1000**1000))
#
# for i in generator:
#     print(i)


# yield - генератор

# def my_range(start: int, stop: int, step: int = 1):
#     while start <= stop:
#         yield start
#         start += step
#
#
# my_range = my_range(0, 10, 2)
# # print(len(my_range)) # Не работает - TypeError: object of type 'generator' has no len()
# # print(next(my_range))
# # print(next(my_range))
#
# for i in my_range:
#     print(i)
#
# # TODO - Практика 1
# """
# Напишите свой аналог map с использованием генератора
# за основу можете взять функцию ниже
# """
#
#
# # yield - можно перевести как "порождать" или "давать" или "выдавать"
# def map_analog(func: callable, iterable: list | set | tuple) -> list:
#     result = []
#     for i in iterable:
#         result.append(func(i))
#     return result
#
#
# # iter
# def map_analog_generator(func: Callable, iterable: list | set | tuple) -> Iterator:
#     for i in iterable:
#         yield func(i)
#
#
# print_generator = map_analog_generator(print, [1, 2, 3, 4, 5])
#
#
# # Функия ленивого чтения txt документа с использованием yield
# def read_txt_file(file_path: str) -> str:
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             yield line.strip()
#
#
# file_generator = read_txt_file('../data/generator.txt')
# print(next(file_generator))
# print(next(file_generator))
# print(next(file_generator))
# # print(next(file_generator))
#
# # All, Any - встроенные функции + generator
# # all - возвращает True если все элементы итерируемого объекта True
# # any - возвращает True если хотя бы один элемент итерируемого объекта True
# # Но вместе с генераторами они будут работать быстрее, так как они ленивые
# # И при первом же False (для all) или True (для any) они прекратят свою работу
#
# product_list = [
#     'milk',
#     'bread',
#     'water',
#     'apple',
#     'banana',
#     ''
# ]
#
# # all на то что нет пустых строк
# print(all(product_list))  # False
# # any на то что есть пустые строки
# print(any(product_list))  # True
#
# # проверка на pp в продукте
# print(all('pp' in product for product in product_list))  # False
# print(any('pp' in product for product in product_list))  # True
#
# # Тоже самое с лямбдой
# print(all(map(lambda x: 'pp' in x.lower(), product_list)))  # False
# print(any(map(lambda x: 'pp' in x.lower(), product_list)))  # True
#
# # Filter - функция высшего порядка, принимает функцию и итерируемый объект
# # Возвращает filter-объект (генератор)
# # Принимаемая функция должна возвращать True или False
#
# pp_filter = filter(lambda x: 'pp' in x.lower(), product_list)
# print(', '.join([i for i in pp_filter]))
#
# from data.marvel import full_dict
#
# marvel_list = [film for film in full_dict.values()]
# # pprint(marvel_list, sort_dicts=False)
#
# # Filter comprihanshion
# films_2008 = [film for film in marvel_list if film['year'] == 2008]
# # pprint(films_2008, sort_dicts=False)
#
# # Filter + lambda
# films_2008 = list(filter(lambda film: film['year'] == 2008, marvel_list))
# pprint(films_2008, sort_dicts=False)
#
# # TODO - ищем фильмы на букву "Ч" через filter и lambda
# films_ch = list(filter(lambda film: film['title'].startswith('Ч')
# if isinstance(film['title'], str) else False, marvel_list))
#
#
# # Проверка в полном варианте
# def filter_ch(film: dict) -> bool:
#     if isinstance(film['title'], str):
#         return film['title'].startswith('Ч')
#     else:
#         return False
#

# Sort - сортировка списков
product_list = [
    'milk',
    'bread',
    'water',
    'apple',
    'banana',

]
# sort - сортирует список на месте
# аргументы
# key - функция для сортировки
# reverse - сортировка в обратном порядке
product_list.sort(key=lambda x: x[-1])
print(product_list)

# sorded - Работает с любыми итерируемыми объектами

some_dict = {
        'title': 'Блэйд',
        'year': '2025',
        'director': 'Ян Деманж',
        'screenwriter': 'Майкл Старрбери и Ник Пиццолатто',
        'producer': 'Кевин Файги и Эрик Кэрролл',
        'stage': 'Пятая фаза'
    }

# Сортировка записей словаря по ключам на выходе словарь с сортированными ключами
sorted_dict = dict(sorted(some_dict.items()))
pprint(sorted_dict, sort_dicts=False)

# Сортировка записей словаря по значениям на выходе словарь с сортированными значениями
sorted_dict = dict(sorted(some_dict.items(), key=lambda x: x[1]))
pprint(sorted_dict, sort_dicts=False)

# Сортировка записей словаря по второй букве ключей на выходе словарь с сортированными ключами
sorted_dict = dict(sorted(some_dict.items(), key=lambda x: x[0][1]))
pprint(sorted_dict, sort_dicts=False)