"""
Lesson 10
17.01.2024

- Модули
- Пакеты
- Импорт модулей и пакетов
"""
from pprint import pprint

# import lesson_9 # Импорт всего модуля
# from lesson_9 import *
# from lesson_9 import shop_list
from lesson_9 import shop_list as sl  # Даем псевдоним
# from temp_import import temp_import_string
# print(f'{sl=}')


# print(lesson_9.shop_list) # import lesson_9 # Импорт всего модуля
# print(shop_list) # from lesson_9 import *

# print(f'{shop_list=}') # from lesson_9 import shop_list
# print(f'{temp_import_string=}') # from temp_import import temp_import_string

# from 11_lesson import lesson_11 # Импорт не будет работать - т.к. не правильный нейминг

from data.marvel import full_dict

# print(full_dict)

# # TODO Практика!
# """
# Пересоздать full_dict в виде списка словарей
# В идеале, через list comprehension
#
# Как вариант можно создать пустой список
# В цикле его наполнить
#
# Тут мы работаем с .values()
# Принт - это просто для отладки
# """
# films_list = [film for film in full_dict.values()]
# # print(films_list[:2])
#
# films_list2 = []
# for film in full_dict.values():
#     films_list2.append(film)
#
# # print(films_list2[:2])
#
# # Сделаем список словарей. Но расширим словарь ID ключем
# films_list3 = [{
#     'id': id_film,
#     **film
# } for id_film, film in full_dict.items()]
# print(films_list3[:2])
#
# film_list4 = []
# for key, value in full_dict.items():
#     new_dict = value
#     new_dict['id'] = key
#     film_list4.append(new_dict)
#
# print(film_list4[:2])
#
# films_list5 =[{
#     'id': id_film,
#     'title': film['title'].upper() if film['title'] != 'TBA' else None,
#     'year': film['year'] if film['year'] != 'TBA' else None,
#     'director': film['director'],
#     'stage': film['stage'],
#
# } for id_film, film in full_dict.items()
# # if будет тут
# ]
#
# # Последние 3 элемента
# print(films_list5[-3:])
#
# # TODO Практика!
# """
# 1. Пользовательский ввод
# Пользователь вводит фазу во вселенной Марвел
# В виде "Пятая фаза"
#
# Ваш list comprehension должен вернуть список словарей
# только тех фильмов, которые относятся к этой фазе
#
# в словарях должны быть ключи
# id
# title
# year
# """
#
# # user_phase = input('Введите фазу: ').lower()
# user_phase = 'пятая фаза'
# result = [
#     {
#         'id': id_film,
#         'title': film['title'],
#         'year': film['year'],
#         'stage': film['stage'],
#
#     }
#     for id_film, film in full_dict.items()
#     if film['stage'].lower() == user_phase
# ]
# pprint(result)

# # Методы словарей (от наиболее часто используемых к менее часто используемым)
# # values - возвращает значения словаря
# # keys - возвращает ключи словаря
# # items - возвращает пары ключ-значение
# # update - обновляет словарь, добавляя пары ключ-значение из другого словаря
# # get - возвращает значение по ключу (если ключа нет, возвращает None)
# # clear - очищает словарь
# # copy - возвращает копию словаря
# # pop - возвращает значение по ключу и удаляет ключ
# # popitem - возвращает пару ключ-значение и удаляет ее
# # setdefault - возвращает значение по ключу, если его нет, то создает ключ со значением
# # fromkeys - создает словарь с ключами из списка и значением
#
# # len - возвращает длину словаря (количество пар ключ-значение)
# # zip - создает словарь из двух списков (ключи и значения)

person_dict = {
    'name': 'John',
    'age': 30,
    'phone': '+71234567890',
    'email': 'john@yahoo.com'
}

# pop - возвращает значение по ключу и удаляет ключ
# print(person_dict.pop('phone'))
# print(person_dict)

# popitem - возвращает пару ключ-значение и удаляет ее
# print(person_dict.popitem())
# print(person_dict)

# person_dict_items = list(person_dict.items())
# print(f'{person_dict_items=}')
#
# # Сшиваем это обратно в словарь dict
# person_dict = dict(person_dict_items)
# print(f'{person_dict=}')
#
# person_dict_keys = list(person_dict.keys())
# person_dict_values = list(person_dict.values())
#
# zip_person_dict = zip(person_dict_keys, person_dict_values)
# print(f'{dict(zip_person_dict)=}')
#
# new_dict = {}
# for index in range(len(person_dict_keys)):
#     new_dict[person_dict_keys[index]] = person_dict_values[index]

person_dict = {
    'name': 'John',
    'age': 30,
    'phone': '+71234567890',
    'email': 'john@yahoo.com'
}

# Get - вернет либо значение по ключу, либо None
# print(person_dict.get('name'))
# print(person_dict['is_married']) # KeyError: 'is_married'
# print(person_dict.get('is_married'))
# print(person_dict.get('is_student', 'Не указано'))

# Update - обновляет словарь, добавляя пары ключ-значение из другого словаря

person_dict.update({
    'is_married': True,
    'is_student': True,
    'age': 31,
    'name': 'Ivan',
    'email': 'IvanSmith@yandex.ru',
})

print(f'{person_dict=}')


person_dict = {
    'name': 'John',
    'age': 30,
    'contacts': {
        'phone': '+71234567890',
        'email': 'john@yahoo.com'
        }
}

person_dict_copy = person_dict.copy()

person_dict_copy['contacts']['phone'] = '+71234567891'

print(f'{person_dict=}')
print(f'{person_dict_copy=}')