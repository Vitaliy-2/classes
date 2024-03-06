# print('\U0001F600')
#
# print(ord('A'))
# print(ord('a'))
# print(ord('?'))
# print(chr(65))
# print(chr(97))
# print(chr(128512))
import csv

# txt_file = open('python315.txt', 'w', encoding='windows-1251')
# txt_file.write('Hello, Python315!\n')
# txt_file.close()
#
# txt_file = open('python315.txt', 'a', encoding='windows-1251')
# txt_file.write('Hello, Python315!\n')
# txt_file.close()

# txt_file = open('python315.txt', 'r', encoding='windows-1251')
# # print(txt_file.readlines())
# # print(txt_file.readline(), end='')
# # print(txt_file.readline())
# # print(txt_file.readlines())
# print(txt_file.read())

from data.marvel import simple_set

# with open('marvel.txt', 'w', encoding='windows-1251') as marvel_file:
#     marvel_file.writelines([f'{line}\n' for line in simple_set])
#     # print(marvel.txt)
#
# with open('marvel.txt', 'r', encoding='windows-1251') as marvel_file:
#     marvel_list = marvel_file.readlines()  # Возвращает список строк
#
# marvel_set = {line.strip() for line in marvel_list}
# print(marvel_set)

# with open('marvel.txt', 'r', encoding='windows-1251')




# from data.marvel import simple_set
#
# with open('marvel.txt', 'w', encoding='utf-8') as marvel_file:
#     marvel_file.writelines([f'{line}\n' for line in simple_set])
#
# with open('marvel.txt', 'r', encoding='utf-8') as marvel_file:
#     file_list = set(marvel_file.readlines())
# data = {line.strip() for line in file_list}
# print(data)
#
# student_list = [
# ['name', 'age', 'group'],
# ['Иван', 20, 'Python'],
# ['Петр', 30, 'Java'],
# ['Алексей', 40, 'C#'],
# ['Николай', 24, 'C++'],
# ]

# with open('students.csv', 'w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(student_list)


# with open('students.csv', 'w', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerow(student_list)
#
# students_list_dicts = [
# {'name': 'Иван', 'age': 20, 'group': 'Python'},
# {'name': 'Петр', 'age': 30, 'group': 'Java'},
# {'name': 'Алексей', 'age': 40, 'group': 'C#'},
# {'name': 'Николай', 'age': 24, 'group': 'C++'},
# ]
#

# data = ';'.join(simple_set)
# print(data)
#
# with open('marvel.txt', 'w', encoding='utf-8') as file:
#     file.write(data)
#
# with open('marvel.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#
# marvel_list = data.split(';')
# marvel_set = set(marvel_list)
#
# print(marvel_set)

# student_list = [
# ['name', 'age', 'group'],
# ['Иван', 20, 'Python'],
# ['Петр', 30, 'Java'],
# ['Алексей', 40, 'C#'],
# ['Николай', 24, 'C++'],
# ]
#
# with open('students.csv', 'w', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerows(student_list)
#
# new_student = ['Сергей', 35, 'Python']
#
# # with open('students.csv', 'a', encoding='windows-1251') as file:
# #     writer = csv.writer(file, delimiter=';', lineterminator='\n')
# #     writer.writerow(new_student)
#
# with open('students.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.reader(file, delimiter=';')
#     # student_list = list(reader)
#     # print(student_list)
#     for line in reader:
#         print(line)

students_list_dicts = [
    {'name': 'Иван', 'age': 20, 'group': 'Python'},
    {'name': 'Петр', 'age': 30, 'group': 'Java'},
    {'name': 'Алексей', 'age': 40, 'group': 'C#'},
    {'name': 'Николай', 'age': 24, 'group': 'C++'},
]

with open('students.dict.csv', 'w', encoding='windows-1251') as file:
    fieldnames = list(students_list_dicts[0].keys())
    writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    writer.writerows(students_list_dicts)

with open('students.dict.csv', 'r', encoding='windows-1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    students_list_dicts = list(reader)
    print(students_list_dicts)

new_student = {
    'name': 'Сергей',
    'age': 35,
    'group': 'Python'
}

# Дозапись в csv файл
with open('students.dict.csv', 'a', encoding='windows-1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=new_student.keys(), lineterminator='\n')
    writer.writerow(new_student)

