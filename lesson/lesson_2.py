"""
Lesson 4
11.12.2023

len() - встроенная функция для определения длины объекта
type() - встроенная функция для определения типа объекта
Отладочная строка. f'{var=}'
zen python - https://pythonchik.ru/osnovy/dzen-python-pep20
pep8 - https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html
математические операции
str() - встроенная функция для приведения объекта к строковому типу
сложение строк, умножение строк
print(*args, sep=' ', end='\n')
input('Введите число: ') - ввод данных с клавиатуры, всегда возвращает строку

int() - встроенная функция для приведения объекта к целочисленному типу
float() - встроенная функция для приведения объекта к вещественному типу
int, float - работа с числами
boolian - логический тип данных - bool()

операторы сравнения
логические операторы

bool() - встроенная функция для приведения объекта к логическому типу
"""

# name = 'Владимир'
# age = 23
# message = f'Hi, {name}, {age}'  # Комментарий

# Мы можем посмотреть тип объекта. Это может быть очень полезно при отладке
# print(type(name))
# print(type(message))
# print(type(age))

# Но таких принтов может быть очень много. Поэтому мы можем использовать отладочную строку
# Часто её делают именно такой, чтобы было удобно читать
# print(f'Тип переменной name: {type(name)}')

# Но есть секретный способ, о котором никто не знает))
# print(f'{name=}')
# print(f'{type(name)=}')
#
# print(f'\t{message=} имеет тип данных {type(message)}\n'
#       f'{age=} имеет\tтип данных {type(age)}')
#
# age = str(age)
# name_age_concat = name + ' ' + age + '\n'
# name_age_concat = name_age_concat * 5
# print(name_age_concat)

# print - функция для вывода данных в консоль
# print(*args, sep=' ', end='\n')
# *args - неограниченное количество аргументов

# print('Привет', 'группа', 'Python315', sep=' | ', end='!')
# print('Привет', 'группа', 'Python315')
# print('Привет', 'группа', 'Python315')
#
# print('.', end='')
# print('.', end='')
# print('.', end='')
# print('.', end='')

# int() - встроенная функция для приведения объекта к целочисленному типу
# float() - встроенная функция для приведения объекта к вещественному типу
# some_int = '5'
# print(type(some_int))  # str
# some_int = int(some_int)
#
# print(type(some_int))  # int
#
# print(float('5'))

# input('Prompt') - ввод данных с клавиатуры, всегда возвращает строку
# prompt - подсказка пользователю, что от него требуется
# num_a = input('Введите число a: ')
# some_float = 5, 5
# print(type(some_float))
#
# some_float = 5.5
# print(f'{some_float=}, {type(some_float)=}')

# TODO: Практика!
"""
1. Запросите ввод числа a и b 
2. Выведите сумму чисел a и b
"""
# Максимально плоский вариант

# a = input('Введите число a: ')
# b = input('Введите число b: ')
#
# a = int(a)
# b = int(b)
#
# result = a + b
# print(result)

# Вариант 2
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
#
# print(f'Cумма чисел {a} и {b} равна {a + b}')

# Вариант 3 (самый плоский - плохой код.) Читаемость, имеет большое значение
# print(f'{int(input("Введите число a: ")) + int(input("Введите число b: "))}')

# Математические операции
# Сложение +
# Вычитание -
# Умножение *
# Деление /
# Возведение в степень **
# Целочисленное деление //
# Остаток от деления %
# Квадратный корень ** 0.5
# Кубический корень math.pow(x, 1/3)
# Округление round()
# Модуль числа abs()


# a = 5
# b = 12
# Сложение
# print(f'{a + b=}')

# Вычитание
# print(f'{a - b=}')

# Умножение
# print(f'{a * b=}')

# Деление
# print(f'{a / b=}')

# Возведение в степень
# print(f'{a ** b=}')

# Целочисленное деление
# print(f'{b // a=}')

# Остаток от деления
# print(f'{b % a=}')

# Round - округление
# round(число, количество знаков после запятой)
# print(f'{round(51222.4234)=}')
# print(f'{round(51222.4234, 2)=}')
# print(f'{round(51922.4234, -3)=}')
#
# print(f'{2+2*2=}')
# print(f'{(2+2)*2=}')

# Boolian - логический тип данных - bool()
# True - истина
# False - ложь

# bool() - встроенная функция для приведения объекта к логическому типу

# int_zero = 0
# int_negative = -5
# int_positive = 5

# str_empty = ''
# str_with_space = ' '
#
# float_zero = 0.0
# float_negative = -5.5
# float_positive = 5.5
#
# bool_true = True
# bool_false = False
#
# empty_list = []
# not_empty_list = [1, 2, 3]
#
# empty_dict = {}
# not_empty_dict = {'a': 1, 'b': 2}

# print(f'Приводим к bool: {int_zero=}, {bool(int_zero)=}, {int_negative=}, {bool(int_negative)=}, {int_positive=}, {bool(int_positive)=}')
# print(f'Приводим к bool: {str_empty=}, {bool(str_empty)=}, {str_with_space=}, {bool(str_with_space)=}')
# print(f'Приводим к bool: {float_zero=}, {bool(float_zero)=}, {float_negative=}, {bool(float_negative)=}, {float_positive=}, {bool(float_positive)=}')
# print(f'Приводим к bool: {bool_true=}, {bool(bool_true)=}, {bool_false=}, {bool(bool_false)=}')
# print(f'Приводим к bool: {empty_list=}, {bool(empty_list)=}, {not_empty_list=}, {bool(not_empty_list)=}')
# print(f'Приводим к bool: {empty_dict=}, {bool(empty_dict)=}, {not_empty_dict=}, {bool(not_empty_dict)=}')

# Операторы сравнения
# == - равно
# != - не равно ! =
# > - больше
# < - меньше
# >= - больше или равно > =
# <= - меньше или равно < =

# a = 5
# b = 10
#
# print(f'{a == b=}')
# print(f'{a != b=}')
# print(f'{a > b=}')
# print(f'{a < b=}')
# print(f'{a >= b=}')
# print(f'{a <= b=}')

# Логические операторы в порядке приоритета
# () - скобки
# not - не
# and - и
# or - или

# not True = False
# not False = True
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# True or True = True
# True or False = True
# False or True = True
# False or False = False


# a = 2
# b = 3

# print(f'{a=}, {b=} {a == b and a > b=}')
# print(f'{a=}, {b=} {a == b or a < b=}')
# print(f'{a=}, {b=} {not a == b=}')
# print(f'{a=}, {b=} {not a == b and a > b=}')
# print(f'{a=}, {b=} {not a == b or a > b=}')
# print(f'{a=}, {b=} {not a == b or not a > b=}')
# print(f'{a=}, {b=} {not a == b and not a > b=}')
# print(f'{a=}, {b=} {not (a == b and a > b)=}')

#todo: Практика!

"""
0. Задайте переменную, которая будет хранить минимально приемлемый рейтинг фильма (целое число от 0 до 10)
1. Запросите пользовательский ввод названия фильма
2. Запросите рейтинг фильма от пользователя (в виде дробного числа от 0 до 10 с любым количеством знаков после запятой)
- округляем рейтинг до 1 знака после запятой
3. Выведите ф-строку, Название фильма. Рейтинг фильма: Рейтинг. Приемлемо для просмотра: True/False

Для получения true/false используйте операторы сравнения
Для приведения к типу float используйте функцию float()
"""

MIN_RATING_THRESHOLD = 5

movie_name = input('Введите название фильма: ')
movie_rating = float(input('Введите рейтинг фильма: '))

result_string = (f'Название фильма: {movie_name}.\n'
                 f'Рейтинг фильма: {round(movie_rating, 1)}\n'
                 f'Приемлемо для просмотра: {movie_rating >= MIN_RATING_THRESHOLD}')

print(result_string)