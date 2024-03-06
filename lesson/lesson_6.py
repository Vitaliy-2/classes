"""
Lesson 12
25.12.2023

- Списки
- Методы списков
- List comprehension
- Random
- While
- Познакомились с set
"""

"""
Списки - упорядоченные изменяемые итерируемые коллекции 
объектов произвольных типов (почти как массивы в JS)
"""

# Методы списков
# list.append(x) - добавляет элемент в конец списка
# list.extend(L) - расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x) - вставляет на i-ый элемент значение x
# list.remove(x) - удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i]) - удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]]) - возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x) - возвращает количество элементов со значением x
# list.sort([key=функция]) - сортирует список на основе функции
# list.reverse() - разворачивает список
# list.copy() - возвращает копию списка
# list.clear() - очищает список
# del list[i] - удаляет i-ый элемент
# del list[i:j] - удаляет срез от i до j включительно
# del list[i:j:k] - удаляет элементы с i по j с шагом k


list_names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
list_names2 = ['Alex', 'John', 'Bob', 'Jack', 'Bill', 'Sam', 'Петя']

# Разница между append и extend
# list_names.append(list_names2)
# print(list_names)

list_names.extend(list_names2)
some_str = 'qwerty'
list_names.extend(some_str)
# print(list_names)
# print(set(list_names))

# insert - вставить элемент в список (по индексу)
shop_list = ['шоколадный дед мороз']

shop_list.insert(0, 'молоко')
shop_list.insert(0, 'хлеб')
shop_list.insert(0, 'яйца')

# print(f'{shop_list=}')

shop_list_2 = ['сыр', "сыр", "молоко", "молоко",
               "сыр", "хлеб", "молоко",
               "колбаса", "сыр", "хлеб",
               "коньяк", "шоколадный дед мороз", "коньяк"]


#TODO Практика!
"""
Пройти по циклу продуков из списка shop_list_2 циклом
посчитать количество каждого продукта в списке (count)
если количество больше одного, объявить вложенный цикл который
будет работать по range от 1 до количества продукта - 1
и удалять продукт из списка по названию
"""
# print(f'{shop_list_2=}')

for product in shop_list_2:
    count = shop_list_2.count(product)
    if count > 1:
        for i in range(count - 1):
            shop_list_2.remove(product)

# print(f'{shop_list_2=}')

# Вариант №2 if in

clear_shop_list_2 = []
for product in shop_list_2:
    if product not in clear_shop_list_2:
        clear_shop_list_2.append(product)

# print(f'{clear_shop_list_2=}')
# Вариант №3 set
clear_shop_list_2 = list(set(shop_list_2))
# print(f'{clear_shop_list_2=}')

# Функции для преобразования типов данных в python
# str() - преобразование в строку
# int() - преобразование в целое число
# float() - преобразование в вещественное число
# bool() - преобразование в логический тип данных
# list() - преобразование в список
# tuple() - преобразование в кортеж
# set() - преобразование в множество
# dict() - преобразование в словарь

# А что будет если мы str к списку?)
# print(f'{str(clear_shop_list_2)=}')
# print(f'{type(str(clear_shop_list_2))=}')


# pop - удаляет элемент из списка (по индексу)
print(f'{clear_shop_list_2=}')
set_clear_shop_list_2 = set(clear_shop_list_2)
random_element = set_clear_shop_list_2.pop()
print(f'{random_element=}')
print(f'{set_clear_shop_list_2=}')

# list comprehension - списковое включение
# [элемент for элемент in коллекция]

gifts_list = ['мишка', 'айфон',
              'билет на концерт', 'кроссовки',
              'билет на самолет']

list_comprehension = [gift for gift in gifts_list]
print(f'{list_comprehension=}')

list_comprehension = [gift.capitalize() for gift in gifts_list]
print(f'{list_comprehension=}')

# Только строки без пробелов
list_comprehension = [gift.capitalize() for gift in gifts_list if ' ' not in gift]
print(f'{list_comprehension=}')

# TODO Практика!
"""
Попросите пользователя ввести 5 чисел через пробел
Разделите это на список
Через list comprehension возведите каждое число в квадрат
"""

# user_input = input('Введите 5 чисел через пробел: ')
# user_list = user_input.split(' ')

# result = [int(num) ** 2 for num in user_list if num.isdigit()]

# print(f'{result=}')

# Плохой код. Но это тоже будет работать.
# print([int(num) ** 2 for num in input('Введите 5 чисел через пробел: ').split(' ') if num.isdigit()])

products = ['молоко', 'хлеб', 'яйца', 'сыр', 'колбаса', 'коньяк', 'шоколадный дед мороз']

[print(product.capitalize(), end=' ') for product in products]

password = 'qwerty12345&&**^'
pass_letters = [letter for letter in password if letter.isalpha()]
pass_digits = [digit for digit in password if digit.isdigit()]
pass_spec = [spec for spec in password if not spec.isalnum()]

sum_letters = len(pass_letters)
sum_digits = len(pass_digits)
sum_spec = len(pass_spec)

# прибавляем 1 если это буква
letters_count = sum([1 for letter in password if letter.isalpha()])
print([1 for letter in password if letter.isalpha()])

# random - модуль для генерации случайных чисел
import random

# random.random() - возвращает случайное число от 0 до 1
# random.randint(a, b) - возвращает случайное целое число в диапазоне от a до b включительно
# random.choice(seq) - возвращает случайный элемент из непустой последовательности seq
# random.shuffle(seq) - перемешивает непустую последовательность seq

print(f'{random.random()=}')
print(f'{random.randint(0, 2)=}')
print(f'{random.choice(products)=}')
# делаем shuffle
random.shuffle(products)
print(f'{products=}')

# while - цикл с предусловием
# бескоцнечный цикл
# count = 0
# while True:
#     count += 1
#     print(f'Привет в {count}й раз')


# while bool:
#    pass

# while list:
#    list.pop()

while products:
    product = products.pop()
    if product == 'каньяк':
        print('Коньяк не нужен')
        break

else:
    print('Закончили без break\n'
          'Новый Год удался )')