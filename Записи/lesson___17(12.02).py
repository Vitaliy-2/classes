from pprint import pprint

product_list = ['apple', 'banana', 'orange', 'milk', 'bread', 'butter', 'cheese', 'water', 'juice', 'cucumber']
# Простая копия
product_list_copy = [product for product in product_list]
# делаем замену a на b
product_list_replace = [product.replace('a', 'b') for product in product_list]
# Если в продукте есть буква p
product_list_p = [product for product in product_list if 'p' in product]
# Если продукт начинается на букву b делаем замену на n
product_list_b = [product if not product.startswith('b') else product.replace('b', 'n') for product in product_list]

# print(product_list)
# print(product_list_copy)
# print(product_list_replace)
# print(product_list_p)
# print(product_list_b)

from data.marvel import full_dict

new_dict = [{'id': id_film, **film} for id_film, film in full_dict.items()]
# pprint(new_dict)

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
#
# # Сортировка записей словаря по значениям на выходе словарь с сортированными значениями
# sorted_dict = dict(sorted(some_dict.items(), key=lambda x: x[1]))
# pprint(sorted_dict, sort_dicts=False)

# Сортировка записей словаря по второй букве ключей на выходе словарь с сортированными ключами
# sorted_dict = dict(sorted(some_dict.items(), key=lambda x: x[0][1] if isinstance(x[0], str) else 'A'))
# pprint(sorted_dict, sort_dicts=False)

diff_dict = {1:
                 {11:
                      {111: 'a',
                       112: 'b'
                       },
                  12:
                      {121: 'c',
                       122: 'd'
                       }
                  },
             2:
                 {21:
                      {211: 'e',
                       212: 'f'
                       },
                  22:
                      {221: 'g',
                       222: 'h'
                       }
                  }
             }

# print(diff_dict[1][11][112])
# # Возьмем values.values
# print(dict(diff_dict.items()).items())


product_list = ['bread', 'apple', 'banana', 'orange', 'milk', 'butter', 'cheese', 'water', 'juice', 'cucumber']
result = sorted(product_list)
result2 = sorted(product_list, reverse=True)
print(result)
print(result2)
#
# # Сортировка по длине
result3 = sorted(product_list, key=len, reverse=True)
print(result3)
#
# # Сортировка по 2м признакам, длина и первая буква
result4 = sorted(product_list, key=lambda x: (len(x), x))
print(result4)
#
# # Список словарей 4 студента из 2х разных групп
students = [
    {'name': 'John', 'group': 'A', 'age': 28},
    {'name': 'Bob', 'group': 'B', 'age': 25},
    {'name': 'Tom', 'group': 'A', 'age': 21},
    {'name': 'Sam', 'group': 'B', 'age': 23},
]
#
# # Сортировка по группе и по имени
result5 = sorted(students, key=lambda x: (x['group'], x['name']))
pprint(result5)

a = 5
print(a)


def sum_func():
    global a
    a = 10
    b = 14
    return a, b


print(sum_func())
print(a)
print(b)
