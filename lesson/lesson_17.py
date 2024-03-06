"""
Lesson 17
12.02.2024

- Comprehensions
- Dict Comprehensions
- lambda
- map, filter, sorted
- Разбор домашнего задания
"""
from pprint import pprint
from typing import Dict, Union

#
# product_list = ['apple', 'banana', 'orange', 'milk', 'bread', 'butter', 'cheese', 'water', 'juice', 'cucumber']
# # Простая копия
# product_list_copy = [product for product in product_list]
# # делаем реплейс a на b
# product_list_replace = [product.replace('a', 'b') for product in product_list]
# # Если в продукте есть буква p
# product_list_p = [product for product in product_list if 'p' in product]
# # Если продукт начинается на букву b делаем реплейс на n
# product_list_b = [product if not product.startswith('b') else product.replace('b', 'n') for product in product_list]
# # Если продукт длинне 5 символов - мы вообще его не трогаем. Если в нем есть i - пишем None
# product_list_len = [product if 'i' not in product.lower() else None for product in product_list if len(product) <= 5]
# print(product_list_len)
#
#
# def get_upper(product: str) -> str:
#     return product.upper()
#
#
#
# # Map - делаем upper к каждому элементу
# product_list_upper = list(map(get_upper, product_list))
# product_list_upper_comp = [get_upper(product) for product in product_list]
#
# # Filter - оставляем только продукты с буквой p c помощью функции letter_filter без lambda
# letter = 'p'
# product_list_p = list(filter(lambda product: letter in product.lower(), product_list))
# product_list_comp = [product for product in product_list if letter in product.lower()]
#
# # Dict Comprehensions
# person = {
#     'name': 'John',
#     'age': 30,
#     'job': 'developer'
# }
#
# # Простая копия словаря
# person_copy = {key: value for key, value in person.items()}
# person_dict_keys_set = {key for key in person.keys()}
# person_dict_values_set = {value for value in person.values()}
#
# # Приведем все ключи к верхнему регистру
# person_upper = {key.upper(): value for key, value in person.items()}
#
# # Приведем все значения к lower
# # isinstance - проверка на тип данных, первый аргумент - значение, второй - тип данных
# person_copy = person.copy()
# person_copy = {key: value.lower() if isinstance(value, str) else value for key, value in person_copy.items()}
# print(person_copy)
# # Это же, с условием что ключ не начинается на букву a
# person_lower = {key: value.lower() if isinstance(value, str) else value for key, value in person.items() if not key.startswith('a')}
# print(person_lower)
#
# count = 0
# product_dict = {count + i: product for i, product in enumerate(product_list)}
# print(product_dict)
#
from data.marvel import full_dict

full_dict_id = [{'id': id_film, **film} for id_film, film in full_dict.items()]
some_dict = {
    'title': 'Блэйд',
    'year': '2025',
    'director': 'Ян Деманж',
    'screenwriter': 'Майкл Старрбери и Ник Пиццолатто',
    'producer': 'Кевин Файги и Эрик Кэрролл',
    'stage': 'Пятая фаза',
    1: 'Блэйд',
    2: '2025',
    'AA': 'A',
}

# Сортировка - sorded
# Аргументы: iterable, key, reverse


# Сортировка записей словаря по ключам на выходе словарь с сортированными ключами
# sorted_dict = dict(sorted(some_dict.items()))
# pprint(sorted_dict, sort_dicts=False)

# Сортировка записей словаря по значениям на выходе словарь с сортированными значениями
# sorted_dict = dict(sorted(some_dict.items(), key=lambda x: x[1]))
# pprint(sorted_dict, sort_dicts=False)

# Сортировка записей словаря по второй букве ключей на выходе словарь с сортированными ключами
# sorted_dict = dict(sorted(some_dict.items(), key=lambda x: x[0][1] if isinstance(x[0], str) else 'A'))
# pprint(sorted_dict, sort_dicts=False)
#
# diff_dict = {1:
#                  {11:
#                       {111: 'a',
#                        112: 'b'
#                        },
#                   12:
#                       {121: 'c',
#                        122: 'd'
#                        }
#                   },
#              2:
#                  {21:
#                       {211: 'e',
#                        212: 'f'
#                        },
#                   22:
#                       {221: 'g',
#                        222: 'h'
#                        }
#                   }
#              }


# print(diff_dict[1][11][112])
# Возьмем values.values
# print((dict(diff_dict.items()).items()))

# Сортировка - sorded
# Аргументы: iterable, key, reverse
#
# product_list = ['bread', 'apple', 'banana', 'orange', 'milk',  'butter', 'cheese', 'water', 'juice', 'cucumber']
# result = sorted(product_list)
# result2 = sorted(product_list, reverse=True)
# print(result2)
#
# # Сортировка по длине
# result3 = sorted(product_list, key=len)
# print(result3)
#
# # Сортировка по 2м признакам, длина и первая буква
# result4 = sorted(product_list, key=lambda x: (len(x), x))
# print(result4)
#
# # Список словарей 4 студента из 2х разных групп
# students = [
#     {'name': 'John', 'group': 'A', 'age': 20},
#     {'name': 'Bob', 'group': 'B', 'age': 22},
#     {'name': 'Tom', 'group': 'A', 'age': 21},
#     {'name': 'Sam', 'group': 'B', 'age': 23},
# ]
#
# # Сортировка по группе и по имени
# result5 = sorted(students, key=lambda x: (x['group'], x['name']))
# pprint(result5)

"""
Встряхните пыль с дата-сета Marvel! Он нам ещё пригодится!

1. Сделайте импорт `full_dict` из документа `Marvel.py`
2. Напишите пользовательский ввод цифр через пробел, разбейте его на список, и примените к каждому элементу списка 
`int` используя `map`, но только в том случае, если этот элемент списка число, иначе замените его на `None`

3. Используйте `filter` и получите аналогичный по структуре словарь, который будет содержать исходные `id` и остальные ключи, но только тех фильмов, `id` которых есть в полученном списке в п.2
4. Составьте `set comprehension` (генератор множества) собрав множество содержимого ключа `director` словаря дата-сета
5. Составьте `dict comprehension` (генератор словаря) сделав копию исходного словаря `full_dict`, при этом применим в к каждому `'year'` значению, функцию `str`
6. Используйте `filter` и получите аналогичный по структуре словарь, который будет содержать исходные `id` и остальные ключи, но только тех фильмов, которые начинаются на букву `Ч`
7. Опционально: Сделайте сортировку словаря `full_dict` по одному (любому) параметру, с использованием `lambda` на выходе аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете сортировку!
8. Опционально: сделайте сортировку словаря `full_dict` по двум (любом) параметрам, с использованием `lambda` на выходе аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете сортировку!
9. Опционально: напишите однострочник, в котором мы получаем аналогичный по структуре `full_dict` но отфильтрованный через `filter` и с использованием в этой же строке `sorted`
10. Опционально: напишите аннотацию типов для переменных, в которых будет результат и пройдите проверку `mypy` (оставьте сообщение в комментариях в коде об успешной проверке. Я всё читаю!)
11. Сделайте красивый принт результатов `pprint` с подписью, какое задание и где выполнено 💪 (помните, что у него надо выключить сортировку, иначе он сортирует словарь еще раз)
"""

from data.marvel import full_dict

# 2
# user_input = input('Введите числа через пробел: ').split()
# user_input = list(map(lambda x: int(x) if x.isdigit() else None, user_input))
# pprint([num for num in user_input if num], sort_dicts=False)
# print(sum(user_input))

# ids = [id for id in user_input if id]

# 3
# filtered_dict = {id: film for id, film in full_dict.items() if id in ids}
# filtered_dict = dict(filter(lambda x: x[0] in ids, full_dict.items()))
# pprint(filtered_dict, sort_dicts=False)

# 4
directors = {film['director'] for film in full_dict.values()}
print(directors)

# 5
# full_dict_copy = {id: {key: value if key != 'year' else str(value) for key, value in film.items()}
#                   for id, film in full_dict.items()}
#
# stage_description = {
#     'Первая фаза': 1,
#     'Вторая фаза': 2,
#     'Третья фаза': 3,
#     'Четвертая фаза': 4,
#     'Пятая фаза': 5,
#     'Шестая фаза': 6
# }
#
# full_dict_copy = {id: {
#     "title": film["title"],
#     "year": str(film["year"]) if isinstance(film["year"], int) else film["year"],
#     "director": film["director"],
#     "screenwriter": film["screenwriter"],
#     "producer": film["producer"],
#     "stage": stage_description.get(film["stage"], film["stage"])
# }
#     for id, film in full_dict.items()}
#
# pprint(full_dict_copy, sort_dicts=False)

# 6
# print(full_dict)
# films_ch = {id: film for id, film in full_dict.items() if  isinstance(film['title'], str) and film['title'].startswith('Ч')}
# pprint(films_ch, sort_dicts=False)

# 7 Сортировка словаря full_dict по названию фильма
# sorted_dict = dict(sorted(full_dict.items(), key=lambda x: x[1]['title'] if isinstance(x[1]['title'], str) else 'я'))
# pprint(sorted_dict, sort_dicts=False)

# 8 Сортировка словаря full_dict по году выпуска и названию фильма
# Пересоберем словарь, чтобы взять только те фильмы, у которых год выпуска число и название фильма строка
full_dict: Dict[int, Dict[str, Union[str, int]]] = {id: film for id, film in full_dict.items() if isinstance(film['year'], int) and isinstance(film['title'], str)}
# Это же на фильтре
# full_dict = dict(filter(lambda x: isinstance(x[1]['year'], int) and isinstance(x[1]['title'], str), full_dict.items()))

# Сортировка
sorted_dict = dict(sorted(full_dict.items(), key=lambda x: (x[1]['year'], x[1]['title'])))
# pprint(sorted_dict, sort_dicts=False)


# 9 используем очищенную коллекцию full_dict и фильтруем фильмы 2023 года выпуска и сортируем по алфавиту
sorted_dict: Dict[int, Dict[str, Union[str, int]]] = dict(sorted(filter(lambda x: x[1]['year'] == 2023, full_dict.items()), key=lambda x: x[1]['title']))
pprint(sorted_dict, sort_dicts=False)

### Области видимости
# local - локальная область видимости
# global - глобальная область видимости
# builtins - область видимости встроенных функций
# nonlocal - область видимости вложенных функций


# global a
a = 2
b = 3
def some_func():
    # local a
    # nonlocal b # Error
    a = 3
    b = 4
    c = 6
    print(f'some_func: {a}')
    print(f'some_func: {b}')
    def some_inner_func():
        # local a
        # nonlocal c
        global a
        a = 4
        b = 5
        c = 7
        print(f'some_inner_func: {a}')
        print(f'some_inner_func: {b}')
        print(f'some_inner_func: {c}')

    some_inner_func()
    print(f'some_func: {a}')
    print(f'some_func: {b}')
    print(f'some_func: {c}')

print(f'global: {a}')
print(f'global: {b}')
some_func()
print(f'global: {a}')
print(f'global: {b}')



some_dict = {
    'title': 'Блэйд',
    'year': '2025',
    'director': 'Ян Деманж',
    'screenwriter': 'Майкл Старрбери и Ник Пиццолатто',
    'producer': 'Кевин Файги и Эрик Кэрролл',
    'stage': 'Пятая фаза',
    1: 'Блэйд',
    2: '2025',
    'AA': 'A',
}

print(some_dict.items())
print(list(some_dict.items()))