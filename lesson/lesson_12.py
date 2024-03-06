"""
cp1251 - Без этого не исполняется код

- JSON
json.dumps - превращает объект Пайтона в строку
json.loads - превращает строку в объект Пайтона
json.dump - записывает объект Пайтона в файл
Как делать красивый json - indent=4, ensure_ascii=False
Как делать дозапись в файл json - перезаписываем все!)

Работа со временем
datetime
date
calendar
pytz - сторонняя

Lesson 12
24.01.2024

- JSON
"""

# some_list = [
#     {
#         'name': 'Вася',
#         'age': 20,
#         'skills': ['JS', 'Python', 'C++', 'C#', 'Java'],
#         'work': None,
#         'is_student': True
#     },
#     {
#         'name': 'Маша',
#         'age': 18,
#         'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
#     },
#     {
#         'name': 'Петя',
#         'age': 25,
#         'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
#     }
#     ]

# JSON - JavaScript Object Notation
# Импортируем модуль json
import json
# dump - запись в файл
# dumps - возвращает строку
# load - чтение из файла
# loads - возвращает объект из строки

# Превратим в строку
# json_string = json.dumps(some_list, ensure_ascii=False)
# print(json_string)
# print(type(json_string))

# Превращаем назад в объект Пайтона
# python_object = json.loads(json_string)
#
# print(f'{python_object=}')
# print(type(python_object))

# Запись в файл
# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(some_list, file, ensure_ascii=False, indent=4)

# Чтение из файла
# with open('students.json', 'r', encoding='utf-8') as file:
#     python_object = json.load(file)

# print(f'{python_object=}')

# Допишем еще один список через append в json файл а потом
# прочитаем его

# with open('students.json', 'a', encoding='utf-8') as file:
#     json.dump(some_list, file, ensure_ascii=False, indent=4)

# JSONDecodeError
# with open('students.json', 'r', encoding='utf-8') as file:
#     python_object = json.load(file)
#
#
# # Append = нам надо прочитать, добавить, ПЕРЕЗАПИСАТЬ с флагом w
# python_object.append({
#     'name': 'Сергей',
#     'age': 35,
#     'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
# })
#
# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(python_object, file, ensure_ascii=False, indent=4)
#
# # TODO - Практика 1
# """
# Давайте запишем Marvel full_dict в файл json
# Используйте ensure_ascii=False и indent=4
# """

from data.marvel import full_dict

with open('marvel.json', 'w', encoding='utf-8') as file:
    json.dump(full_dict, file, ensure_ascii=False, indent=2)


# Datetime

import datetime

date_ = datetime.date(2024, 1, 24)
date_2 = datetime.date(2024, 2, 24)

today_ = datetime.date.today()

print(f'{date_=}')
print(f'{date_2=}')
print(f'{today_=}')
print(type(today_))

time_ = datetime.time(12, 30, 59)
time_now = datetime.datetime.now()

print(f'{time_=}')
print(f'{time_now=}')

# strftime - превращает объект в строку
# strptime - превращает строку в объект

# прогоняем наши переменные туда и обратно
str_time = time_now.strftime('%H:%M:%S')
print(f'{str_time=}')

# Превращаем строку в объект
time_obj = datetime.datetime.strptime(str_time, '%H:%M:%S')

# От времени 20-20-00 отнимем текущее время
# узнаем сколько осталось до конца занятия
from datetime import timedelta
endtime_lesson = "20:20:00"
endtime_lesson_obj = datetime.datetime.strptime(endtime_lesson, '%H:%M:%S')

time_now = datetime.datetime.now()

delta = datetime.combine(time_now.date(), endtime_lesson_obj.time()) - time_now

formatted_delta = (str(timedelta(seconds=delta.seconds)))
print(f'{formatted_delta=}')