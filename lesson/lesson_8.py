"""
Lesson 8
Повторение материала
- Условные операторы
- Исклюения
- Индексы. Срезы. Работа с упорядоченными коллекциями
- Повторение циклов for и while
- Множества и методы множеств
"""

# Пожалуйста введите число от 1 до 5
# num = input('Пожалуйста введите число от 1 до 5: ')
# try:
#     num = int(num)
# except ValueError:
#     print('Вы ввели не число!')
#     exit()
#
# if not (0 < num <= 5):
#     raise ValueError(f'{num} - это число вне диапазона от 1 до 5')
# elif num == 1:
#     print('Вы ввели число 1')
# elif num == 2:
#     print('Вы ввели число 2')
# elif num == 3:
#     print('Вы ввели число 3')
# elif num == 4:
#     print('Вы ввели число 4')
# elif num == 5:
#     print('Вы ввели число 5')

# print(*args, sep=' ', end='\n')
# print(1, 2, 3, 4, 5, sep=' | ', end='!')
# print(1, 2, 3, 4, 5, sep=' | ', end='!')
# print(1, 2, 3, 4, 5, sep=' | ')
# print(1, 2, 3, 4, 5, sep=' | ')

# is_married = True
#
# if is_married:
#     print('Вы женаты')
#
# is_married = False
#
# if not is_married:
#     print('Вы не женаты')

# Индексы. Срезы. Работа с упорядоченными коллекциями
# Строка - упорядоченная неизменяемая последовательность символов
# Список - упорядоченная изменяемая коллекция объектов произвольных типов
# Кортеж - упорядоченная неизменяемая коллекция объектов произвольных типов

# some_str = '012345'
# some_list = [1, 2, 3, 4, 5]
# some_tuple = (1, 2, 3, 4, 5)
# some_set = {1, 2, 3, 4, 5}

# Отладочная строка
# print(f'{some_str[0]=}')
# print(f'{some_list[0]=}')
# print(f'{some_tuple[0]=}')
# print(f'{some_set[0]=}')  # TypeError: 'set' object is not subscriptable

# some_list[1] = '2'
# print(f'{some_list=}')

# some_str[1] = '2' # TypeError: 'str' object does not support item assignment
# some_tuple[1] = '2' # TypeError: 'tuple' object does not support item assignment

# Срезы
# some_str[start:stop:step]

# print(f'{some_str[4:1:-1]=}')
# print(f'{some_str[2:4:-1]=}')  # Пустая строка (потому что шаг отрицательный)
# print(f'{some_list[-1:-4:-1]=}')
# print(f'{some_tuple[-1:-4:-1]=}')

# Разница между find и index
# find - возвращает индекс первого вхождения подстроки в строку, если подстрока не найдена - выдает -1
# index - возвращает индекс первого вхождения подстроки, если подстрока не найдена - выдает ошибку
#
# some_password = '1234567890'
# some_password2 = '123 4567890'
#
# print(f'{some_password.find(" ")=}')
# print(f'{some_password2.find(" ")=}')
#
# # print(f'{some_password.index(" ")=}')  # ValueError: substring not found
# print(f'{some_password2.index(" ")=}')  # ValueError: substring not found
#
# if some_password2.find(' ') != -1:
#     raise ValueError('В пароле присутствует пробел')

# Повторение циклов for и while

shop_list = ['шоколадный дед мороз', 'Коньяк "Арарат 5 звёзд"', "мандарины"]
for product in shop_list:
    print(product)

for i in range(len(shop_list)):
    print(shop_list[i])

while shop_list:
    print(shop_list.pop())

shop_list_table = [
    ["Название", "Количество", "Цена"],
    ["Шоколадный дед мороз", 5, 200],
    ["Коньяк", 2, 2500],
    ["Ананасы", 3, 300],
]

for row in shop_list_table[1:]:
    product_title = row[0]
    product_count = row[1]
    product_price = row[2]
    print(f'{product_title} - {product_count} шт. - {product_price} руб.')

    print(f'Перебор символов в строке {product_title}')
    for letter in product_title:
        print(letter)

    print(f'Я закончил перебор символов в строке {product_title}')

# Сет - неупорядоченная коллекция уникальных неизменяемых объектов произвольных типов
set_1 = {1, 2, 3, 4, 5}

# Пустой сет
set_2 = set()

# set_3 = {[1, 2, 3], 1, 2, 3, 4, 5}  # TypeError: unhashable type: 'list'

# Union - объединение множеств. На выходе получаем новое множество
# Update - добавление элементов из другого множества. На выходе получаем измененное множество

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

set_3 = set_1.union(set_2)
print(f'{set_3=}')
set_1.update(set_2)
print(f'{set_1=}')

# Comprenhension - генераторы коллекций

# Список
shop_list = ['шоколадный дед мороз', 'Коньяк "Арарат 5 звёзд"', "мандарины", 'Коньяк "Арарат 5 звёзд"', '']

new_shop_list = []
for product in shop_list:
    if product != 'мандарины':
        new_shop_list.append(product.capitalize())

print(f'{new_shop_list=}')

# Простой генератор списка
new_shop_list = [product.capitalize() for product in shop_list if product != 'мандарины']
new_shop_list = {product.capitalize() if product != "мандарины" else None for product in shop_list}
print(f'{new_shop_list=}')

# Пользователь вводит список чисел через запятую, мы можем его превратить в список целых чисел
user_input = input('Введите числа через запятую: ').split(',')
print(f'{user_input=}')
user_input = [int(num) if num.isdigit() else None for num in user_input]
print(f'{user_input=}')


# comprision
MESSAGE = "Это не число"
result = [item ** 2 if item else MESSAGE for item in user_input]
print(result)