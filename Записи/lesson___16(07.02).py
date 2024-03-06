# Анонимная функция
# get_sum = lambda x, y: x + y
#
# print(get_sum(1, 2))
#
# list1 = [1, 2, 3, 'банан', 4, 5]
# result_integers = list(map(int, list1))
# # print(result_integers)
#
# result_integers = list(map(lambda x: int(x) if x.isdigit() else None, list1))
# print(result_integers)
from pprint import pprint
from typing import Callable, Iterator, Any

# def map_analog(func: callable, iterable: list | set | tuple):
#     for i in iterable:
#         yield func(i)

# from data.marvel import full_dict
# films2008 = [film['title'] for film in full_dict.values() if full_dict['year'] == 2008]
# print(films2008)

user_integesr_input = ['1', '2', '3', '4', 'hello']
print(user_integesr_input)
# result = list(map(str, list_user))
result_integers = list(map(lambda x: int(x) if x.isdigit() else None, user_integesr_input))
print(result_integers)


# def map_analog(func: callable, iterable: list | set | tuple) -> list:
#     result = []
#     for i in iterable:
#         result.append(func(i))
#     return result


# print(map_analog(lambda x: int(x) if x.isdigit() else None, user_integesr_input))


def my_range(start: int, stop: int, step: int = 1):
    while start <= stop:
        yield start
        start += step


# my_range = my_range(0, 10, 2)
# # print(next(my_range))
# # print(next(my_range))
# # print(next(my_range))
# # print(next(my_range))
# # print(next(my_range))
# # print(next(my_range))
# # print(next(my_range))
# for i in my_range:
#     print(i)
user_integesr_input = ['1', '2', '3', '4', 'hello', '5']


def map_analog(func: Callable, iterable: list | set | tuple) -> Iterator:
    for i in iterable:
        yield func(i)


print_iter = map_analog(print, user_integesr_input)
for i in print_iter:
    continue

from data.marvel import full_dict

marvel_list = [film for film in full_dict.values()]
# pprint(marvel_list)

film2008 = [film for film in marvel_list if film['year'] == 2008]
# pprint(film2008, sort_dicts=False)

films_2008 = list(filter(lambda film: film['year'] == 2008, marvel_list))
# pprint(films_2008, sort_dicts=False)

films_ch = list(filter(lambda film: film['title'].startswith('Ч')
if isinstance(film['title'], str) else False, marvel_list))
# pprint(films_word, sort_dicts=False)

name_films = [title['title'] for title in films_ch]
pprint(name_films)

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

