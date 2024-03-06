# some_str = '012345'
# for symbol in some_str:
#     print(symbol, end=' ')

# data_user = input('Введите цифры без пробелов: ')
# sum_sum = 0
# for symbol in data_user:
#     if symbol.isdigit():
#         sum_int = int(symbol)
#         sum_sum += sum_int  # += присвоение и добавления сразу
# print(sum_sum)

# input_nums_str = input('Введите цифры без пробелов: ')
# sum_nums = 0
# for symbol in input_nums_str:
#     if symbol.isdigit():
#         sum_int = int(symbol)
#         sum_nums += sum_int  # += присвоение и добавления сразу
#     else:
#         print(f'Символ {symbol} не является цифрой\n'
#               f'Цикл завершился с break')
#         break
#         # print('Эта строка не должна отображаться')
# else:
#     print('Все символы строки являются цифрами\n'
#           'Цикл завершился без break')
# print(f'Сумма цифр: {sum_nums}')


# shop_str = "молоко, хлеб, яйца, сыр"
# shop_list = shop_str.split(', ')
# print(shop_list)
#
# for product in shop_list:
#     print(f'Купить: {product}')

# pass_list = ['qwerty', '12345', 'фыва', 'password', 'пароль', 'qwerty12345']
#
# for password in pass_list:
#     print(f'Анализируем пароль: {password}')
#     for symbol in password:
#         print(f'Символ: {symbol}')
#     print(f'Анализ пароля {password} завершен\n')

# user_password = input('Введите пароли через запятую: ')
# pass_list = user_password.split(', ')
#
# for password in pass_list:
#     print(f'Анализируем пароль: {password}')
#     for symbol in password:
#         print(f'Символ: {symbol}')
#     print(f'Анализ пароля {password} завершен\n')

member = input('Введите цифры без пробелов: ')
sum_member = 0
for cifra in member:
    if cifra.isdigit():
        sum_member = sum_member + int(cifra)
    else:
        continue
print(sum_member)
