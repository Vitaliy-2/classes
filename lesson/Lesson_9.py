"""
Lesson 9
15.01.2024

- Зачем нам нужны словари?
- Синтаксис словарей
- Что может быть ключем?
- CRUD - операции со словарями
- Создание словаря, записей словаря
- Чтение значений по ключу
- Обновление значений по ключу
- Удаление значений по ключу
- Кортежи
- Распаковка значений
- pprint - модуль для красивого вывода
- параметры pprint
- Методы словарей
- Методы кортежей
- Распаковка списков
- Распаковка словарей в цикле
- Keys, values, items
- get
- Только познакомились с import (Продолжим в следующем уроке)
"""
from pprint import pprint
from data.marvel import full_dict, simple_set
print(full_dict)
print(simple_set)

# Пустой словарь
empty_dict = {}
empty_dict2 = dict()

# Ключи - уникальные неизменяемые объекты (числа, строки, кортежи, None, bool)
not_empty_dict = {
    1: 'Первый',
    '2': 'Второй',
    (1, 2, 3): 'Кортеж',
    None: 'None',
    True: 'True',
    False: 'False',
    1.5: 'Вещественное число',
    2: [1, 2, 3]}
# [1, 2, 3]: 'Список'
print(f'{not_empty_dict=}')

# Обращение к элементам словаря по ключу
person_dict = {
    "first_name": "Захар",
    "middle_name": "Илларионович",
    "last_name": "Прутков",
    "age": 85,
}

print(f'{person_dict["first_name"]=}')
print(f'{person_dict["middle_name"]=}')
print(f'{person_dict["last_name"]=}')

# Делаем Захара старше на 2 года
person_dict["age"] = 86
person_dict["age"] += 1

# Добавляем новый ключ
hobbies = ["Hacking", "White hat", "Python"]
person_dict["hobbies"] = hobbies

print(f'{person_dict=}')

# Добавляем хобби
person_dict["hobbies"].append("JavaScript")

# Ключ болезни
person_dict["diseases"] = None
print(f'{person_dict=}')
# Удаляем ключ болезни
del person_dict["diseases"]

pprint(person_dict)
# Параметры pprint
# pprint(person_dict, indent=4, width=100, depth=5, compact=True, sort_dicts=False)
# indent - отступ
# width - ширина строки
# depth - глубина вывода
# compact - компактный вывод
# sort_dicts - сортировать словари

pprint(person_dict, sort_dicts=False
       , indent=2, depth=1)

# Кортежи - неизменяемые упорядоченные последовательности произвольных объектов
# Создание кортежа
empty_tuple = ()
empty_tuple2 = tuple()

# Кортеж из одного элемента
one_element_tuple = (1,)
print(f'{type(one_element_tuple)=}')
print(f'{one_element_tuple=}')

# Кортеж из нескольких элементов
some_tuple = (1, 2, 3, 4, 5)
some_tuple2 = 1, 2  # Кортеж без скобок а не float

# Методы кортежей
# count - возвращает количество элементов в кортеже
# index - возвращает индекс элемента
# len - возвращает длину кортежа
# max - возвращает максимальный элемент
# min - возвращает минимальный элемент
# sum - возвращает сумму элементов

# Распаковка значений
names = ("Иван", "Петр", "Алексей")
names_list = ["Иван", "Петр", "Алексей"]
name_ivan, name_petr, name_alex = names
name2_ivan, name2_petr, name2_alex = names_list

print(name_ivan, name_petr, name_alex)
print(name2_ivan, name2_petr, name2_alex)

# Частичная распаковка
name_ivan, name_petr, *_ = names
*_, name_alex = names
_, _, name_alex3 = names

print(name_alex, name_alex3)

print(_)
print(names[2:])
print(*_)
print(*names[2:])
print('Алексей')

# # Проверяем айдишники
# print(f'{id(names[0])=}')
# print(f'{id(name_ivan)=}')
# print(f'{id(name2_ivan)=}')
#
# # Перепишем на Иван Васильевич в списке
# names_list[0] = "Иван Васильевич"
# print(f'{id(names[0])=}')
# print(f'{id(name_ivan)=}')
# print(f'{id(name2_ivan)=}')
#
# print(name_ivan, name_petr, name_alex)
# print(name2_ivan, name2_petr, name2_alex)

# Key - значение
# Value - значение
# Методы словарей
# keys - возвращает ключи словаря
# values - возвращает значения словаря
# items - возвращает пары ключ-значение

person_dict = {
    "first_name": "Захар",
    "middle_name": "Илларионович",
    "last_name": "Прутков",
    "age": 85,
}

print(f'{person_dict.keys()=}')
print(f'{person_dict.values()=}')
print(f'{person_dict.items()=}')

print(f'{type(person_dict.keys())=}')
print(f'{type(person_dict.values())=}')
print(f'{type(person_dict.items())=}')
list_items = list(person_dict.items())
print(f'{list_items=}')

list_items2 = [
    ('first_name', 'Захар'),
    ('middle_name', 'Илларионович'),
    ('last_name', 'Прутков'),
    ('age', 85)
]

for key, value in person_dict.items():
    print(f'{key=}, {value=}')

# person_table = [
#     [
#         "first_name",
#         "middle_name",
#         "last_name",
#         "age",
#         "more..."
#     ],
#     [
#         "Захар",
#         "Илларионович",
#         "Прутков",
#         85,
#         "more..."
#     ],
#     [
#         "Иван",
#         "Иванович",
#         "Иванов",
#         35,
#         "more..."
#     ],
#     [
#         "Петр",
#         "Петрович",
#         "Петров",
#         25,
#         "more..."
#     ],
# [
#         "Петр",
#         None,
#         "Петров",
#         None,
#     "more..."
#     ],
# ]
#
# for first_name, middle_name, last_name, *_ in person_table:
#     print(f'{first_name=}, {middle_name=}, {last_name=}, {_=}')

# TODO Практика!
"""
Наберите словарь не менее чем с 3 ключами
Сделайте цикл и выведите ключи словаря (метод keys)
Сделайте цикл и выведите значения словаря (метод values)
Сделайте цикл и выведите пары ключ-значение (метод items)
"""

simple_dict = {
    "title": "Hogwarts Legacy",
    "platform": "PS5",
    "genre": "RPG",
    "release_date": 2022,
    "copies_sold": 100500
}

for key in simple_dict.keys():
    print(key)

for value in simple_dict.values():
    print(value)

for key, value in simple_dict.items():
    print(f'{key=}, {value=}')

shop_list = [
    {
        "молочный отдел": ["молоко", "кефир", "творог", "йогурт"],
        "мясной отдел": ["свинина", "говядина", "курица", "баранина"],
        "овощной отдел": ["огурцы", "помидоры", "картофель", "морковь"],
        "алкогольный отдел": {
            "крепкий алкоголь": ["водка", "коньяк", "виски", "ром"],
            "слабоалкогольные напитки": ["пиво", "сидр", "ламбруско", "медовуха"],
        },
        "сумма": 10000,
        "валюта": "руб",
        "дата": "01.01.2021",
        "время": "13:00:25",
        "кассир": "Иванов Иван Иванович"
    },
    {
        "молочный отдел": ["молоко", "кефир", "творог", "йогурт"],
        "мясной отдел": ["свинина", "говядина", "курица", "баранина"],
        "овощной отдел": ["огурцы", "помидоры", "картофель", "морковь"],
        "алкогольный отдел": {
            "крепкий алкоголь": ["водка", "коньяк", "виски", "ром"],
            "слабоалкогольные напитки": ["пиво", "сидр", "ламбруско", "медовуха"],
        },
        "сумма": 10000,
        "валюта": "руб",
        "дата": "01.01.2021",

        "кассир": "Иванов Иван Иванович"
    }
]

for basket in shop_list:
    print(f'{"-" * 100}\n')
    # pprint(basket, sort_dicts=False)
    # Печатаем только основные данные - Сумма время дата кассир
    summ = basket["сумма"]
    date = basket["дата"]
    time = basket.get("время", "Время не указано")
    cashier = basket["кассир"]

    print(f'Информация по чеку: {summ=}, {date=}, {time=}, {cashier=}')
    print(f'{"-" * 100}\n')

# Методы словарей (от наиболее часто используемых к менее часто используемым)
# values - возвращает значения словаря
# keys - возвращает ключи словаря
# items - возвращает пары ключ-значение
# update - обновляет словарь, добавляя пары ключ-значение из другого словаря
# get - возвращает значение по ключу (если ключа нет, возвращает None)
# clear - очищает словарь
# copy - возвращает копию словаря
# pop - возвращает значение по ключу и удаляет ключ
# popitem - возвращает пару ключ-значение и удаляет ее
# setdefault - возвращает значение по ключу, если его нет, то создает ключ со значением
# fromkeys - создает словарь с ключами из списка и значением

# len - возвращает длину словаря (количество пар ключ-значение)
# zip - создает словарь из двух списков (ключи и значения)