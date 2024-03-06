"""
Lesson 11
22.01.2024
Кодировка текста
Виды кодировок
ascii - american standard code for information interchange
Кодировка UTF-8
Кодировка Windows-1251
ord - функция которая добывает номер в таблице символов
chr - функция которая добывает символ по номеру в таблице символов
Сравнение строк
Запись данных в файл
open
close
флаги открытия файла
read - чтение всего файла (возвращает строку)
readline - чтение одной строки (достаем строки построчно до конца файла)
readlines - чтение всех строк (возвращает список строк)
read - чтение всего файла (возвращает строку - весь документ)
with open
writelines - запись списка строк в файл
write - запись строки в файл
"""

# Печатаем эмодзи smile
# print('\U0001F600')

# Функция которая добывает номер в таблице символов
# print(ord('A'))
# print(ord('a'))
# print(ord('😀'))

# Функция которая добывает символ по номеру в таблице символов
# print(chr(65))
# print(chr(97))
# print(chr(128512))
#
# print(f'{"A" > "a"}')
# print(f'{"A" < "a"}')
# print(f'{"😀" < "a"}')
# print(f'{"😀" > "a"}')

# Запись данных в файл
# open - открывает файл
# close - закрывает файл
# Флаги открытия файла
# r - открытие на чтение (является значением по умолчанию).
# w - открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# a - открытие на дозапись, информация добавляется в конец файла. Создает новый файл, если файл не существует.
# b - открытие в двоичном режиме.

# Давайте уже что-то запишем в файл
# txt_file = open('python315.txt', 'a', encoding='windows-1251')
# txt_file.write('Hello, Python315!\n')
# txt_file.close()

# txt_file = open('python315.txt', 'a', encoding='windows-1251')
# txt_file.write('Hello, Python315!\n')
# txt_file.close()

# Чтение построчно
# txt_file = open('python315.txt', 'r', encoding='windows-1251')
# for line in txt_file:
#     print(line, end='') # 2 переноса строки - 1. из файла, 2. print
# txt_file.close()

# Чтение всего файла
# txt_file = open('python315.txt', 'r', encoding='windows-1251')
# str_list = txt_file.readlines()
# str_list = txt_file.read()
# print(str_list)
# print(type(str_list))
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readline())
# txt_file.close()
#
# # Контекстный менеджер with open
# # Гарантирует закрытие файла в любом случае
# with open('python315.txt', 'r', encoding='windows-1251') as txt_file:
#     file_list = txt_file.readlines()
#
# data = [line.strip() for line in file_list]
# print(data)
#
# # data - пишем обратно в файл
# with open('python315.txt', 'a', encoding='windows-1251') as txt_file:
#     txt_file.writelines([f'{line}\n' for line in data])


# todo Практика
"""
1. Импортируйте simple set из модуля marvel
2. Запишите его в файл marvel.txt
3. Прочитайте из файла marvel.txt и запишите в переменную marvel_set сет
"""

"""
Мы работаем с txt и текстом.
Есть несколько вариантов это сделать

1. Превратить сет в список, а потом в строку указав разделитель
2. Записать.
3. Прочитать, разбить на список по разделителю, превратить в сет

Второй вариант - инструменты по работе с коллекциями
1. Записать в файл список
2. Прочитать из файла список
3. Превратить список в сет
"""
from data.marvel import simple_set

# Второй вариант - запись списка строк в файл

# with open('marvel.txt', 'w', encoding='utf-8') as file:
#     file.writelines([f'{line}\n' for line in simple_set])
#
# with open('marvel.txt', 'r', encoding='utf-8') as file:
#     marvel_list = file.readlines() # Вернет список строк
#
# marvel_set = {line.strip() for line in marvel_list}
# print(marvel_set)

# Исключения при работе с файлами
# FileNotFoundError - файл не найден
# PermissionError - нет прав доступа
# Исключения кодировки
# UnicodeDecodeError - ошибка декодирования
# UnicodeEncodeError - ошибка кодирования

# Вариант №1 - работа с 1 строкой и разделителем ;

# data = ';'.join(simple_set)
# print(data)
#
# # пишем строку data в файл
# with open('marvel.txt', 'w', encoding='utf-8') as file:
#     file.write(data)
#
# # читаем строку из файла
# with open('marvel.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#
# # превращаем строку в список
# marvel_list = data.split(';')
# marvel_set = set(marvel_list)
#
# print(marvel_set)

# csv - comma separated values
import csv

student_list = [
    ['name', 'age', 'group'],
    ['Иван', 20, 'Python'],
    ['Петр', 30, 'Java'],
    ['Алексей', 40, 'C#'],
    ['Николай', 24, 'C++'],
]

# Проблема с кодировкой, проблема с разделителем, проблема с переносом строки
# with open('students.csv', 'w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(student_list)

# используем windows-1251 (для Excel)
# delimiter - разделитель (указываем ; для Excel)
# lineterminator - символ переноса строки (убираем лишние переносы)
# with open('students.csv', 'w', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerows(student_list)

# writer - объект класса writer, писатель - он пишет в файл csv
# методы writer
# writerow - запись одной строки
# writerows - запись нескольких строк
# reader - объект класса reader, читатель - он читает из файла csv
# методы reader
# for line in reader - чтение одной строки
# list(reader) - чтение всех строк

new_student = ['Сергей', 35, 'Python']

# Дописываем нового студента в файл
# with open('students.csv', 'a', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerow(new_student)

# Читаем из файла
with open('students.csv', 'r', encoding='windows-1251') as file:
    reader = csv.reader(file, delimiter=';')
    # Чтение всего файла
    # students_list = list(reader)
    # print(students_list)
    # Построчное чтение
    # for student in reader:
    #     print(student)

# print(list_students)

students_list_dicts = [
    {'name': 'Иван', 'age': 20, 'group': 'Python'},
    {'name': 'Петр', 'age': 30, 'group': 'Java'},
    {'name': 'Алексей', 'age': 40, 'group': 'C#'},
    {'name': 'Николай', 'age': 24, 'group': 'C++'},
]

# Запись в students_dict.csv списка словарей
with open('students_dict.csv', 'w', encoding='windows-1251') as file:
    # fieldnames = ['name', 'age', 'group']
    fieldnames = list(students_list_dicts[0].keys())
    writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    writer.writerows(students_list_dicts)

# Чтение из students_dict.csv в список словарей
with open('students_dict.csv', 'r', encoding='windows-1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    students_list_dicts = list(reader)
    print(students_list_dicts)

# openpyxl - библиотека для работы с Excel
# или математический пакет numpy

new_student = {
    'name': 'Сергей',
    'age': 35,
    'group': 'Python'
}

# Дозапись в csv файл
with open('students_dict.csv', 'a', encoding='windows-1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=new_student.keys(), lineterminator='\n')
    writer.writerow(new_student)
