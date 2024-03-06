"""
Lesson 10 - строки итерация циклы
20.12.2023

понятие итерации и итерируемых объектов
строка как итерируемый объект
for - цикл для итерации по объекту
перебор строки в цикле for
практика
оператор break
оператор continue
закомство со списками
"""

# some_str = '012345'
# print(f'{some_str[0]=}')
# print(f'{some_str[1]=}')
# print(f'{some_str[2]=}')
# print(f'{some_str[3]=}')
# print(f'{some_str[4]=}')
# print(f'{some_str[5]=}')

# Ключевое слово for - цикл для итерации по объекту
# for - для
# in - в
# some_str - строка, которую мы хотим перебрать

# some_str = '012345'
# for symbol in some_str:
#     print(symbol, end=' ')

# TODO Практика!
# """
# Попробуйте написать программу:
# 1. Пользовательский ввод: введите цифры без пробелов
# 2. Объявите переменную, которая будет хранить сумму цифр
# 3. Сделайте цикл for, который будет перебирать строку
# - Преобразуйте символ в цифру
# - Прибавьте к сумме
# """
#
# input_nums_str = input('Введите цифры без пробелов: ')
# sum_nums = 0
#
# for symbol in input_nums_str:
#     if symbol.isdigit():
#         sum_int = int(symbol)
#         sum_nums += sum_int
#     else:
#         print(f'Символ {symbol} не является цифрой\n'
#               f'Цикл завершился с break')
#         break
#
# else:
#     print('Все символы строки являются цифрами\n'
#           'Цикл завершился без break')
#
# print(f'Сумма цифр: {sum_nums}')

"""
Список - упорядоченная изменяемая коллекция объектов произвольных типов.
Ссылочная структура данных.
"""
# some_list = [1, 2, 3, 4, 5]
# some_list2 = [1, '2', 3.0, True, None, [1, 2, 3]]

# print(f'{some_list=}')
# print(f'{some_list2=}')

# Обращение к элементам списка по индексу
# print(f'{some_list[0]=}')
# some_list[0] = 10
# print(f'{some_list[0]=}')

# shop_str = "молоко, хлеб, яйца, сыр, шоколадный дед мороз"
# shop_list = shop_str.split(', ')
# print(f'{shop_list=}')
#
# for product in shop_list:
#     print(f'Купить: {product}')

# Перебор каждого элемента списка посимвольно (цикл в цикле)

# pass_list = ['qwerty', '12345', 'фыва', 'йцукен', 'password', 'пароль',
#              '12345678', '1234567890', 'qwerty123', 'qwerty12345']
#
# for password in pass_list:
#     print(f'Анализируем пароль: {password}')
#     for symbol in password:
#         print(f'Символ: {symbol}')
#     print(f'Анализ пароля {password} завершен\n')

# TODO Практика!
"""
Цикл в цикле
Сделайте пользовательский ввод. Пользователь вводит пароли 
через разделитель (опеределите его сами).
Вы разбиваете строку на список паролей. .split("разделитель")

Далее перебираете каждый пароль и каждый символ пароля.
Выводите на экран сообщение:
"Анализируем пароль: qwerty"
"Символ: q"
...
"Анализ пароля qwerty завершен"
"""
#
# input_passwords_str = input('Введите пароли через разделитель: ')
# input_delimiter = input('Введите разделитель: ')
#
# passwords_list = input_passwords_str.split(input_delimiter)
#
# for password in passwords_list:
#     print(f'Анализируем пароль: {password}')
#     for symbol in password:
#         print(f'Символ: {symbol}')
#     print(f'Анализ пароля {password} завершен\n')


# Методы списков
# append - добавить элемент в конец списка
# pop - вытащить элемент из списка (по индексу)
# sort - сортировать список (key: функция сортировки, reverse: обратный порядок)
# count - посчитать количество элементов в списке (по значению)
# extend - расширить список другим списком
# index - найти индекс элемента в списке (первый найденный)
# copy - копировать список
# insert - вставить элемент в список (по индексу)
# remove - удалить элемент из списка (первый найденный)
# reverse - перевернуть список (первый станет последним)
# clear - очистить список (удалить все элементы)
# del - удалить элемент из списка (по индексу)

# Функции списков
# len - длина списка
# min - минимальный элемент списка
# max - максимальный элемент списка
# sum - сумма элементов списка
# all - True если все элементы True
# any - True если хотя бы один элемент True
# enumerate - возвращает индекс и значение элемента списка
# filter - фильтрует список по функции
# map - применяет функцию к каждому элементу списка
# reduce - применяет функцию к элементам списка, возвращает один элемент
# zip - объединяет два списка в список кортежей

# range - генератор последовательности чисел
# параметры - range(start, stop, step)

for i in range(1, 11, 2):
    print(i)

# Сколько элементов в списке покупок должно быть?
product_num = input('Сколько элементов в списке покупок должно быть? ')
product_num = int(product_num)

product_list = []
for i in range(product_num):
    product = input('Введите название продукта: ')
    product_list.append(product)

print(f'Ваш список покупок: {product_list}')

# Я что-то купил
bought_product = input('Я что-то купил: ')
product_list.remove(bought_product)
print(f'Ваш список покупок: {product_list}')

for i in range(len(product_list)):
    product = product_list[i]
    print(f'{i + 1}. {product}')

# Пример что список - ссылочная структура данных
# some_list = [1, 2, 3]
# print(f'{some_list=}')
# print(f'{id(some_list)=}')
# some_list.append(4)
# print(f'{some_list=}')
# print(f'{id(some_list)=}')

