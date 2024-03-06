# some_int = '5'
# print(type(some_int))
# some_int = int(some_int)
# print(type(some_int))

# primer = 19
# print(type([primer]))
#
# print(float('5'))
# prompt = 'Введите число: '
#
# some_float = 5, 5
# print(type(some_float))
#
# some_float = 5.5
# print(type(some_float))

# a = input('Введите число a: ')
# b = input('Введите число b: ')
# a = int(a)
# b = int(b)
# result = a + b
# print(result)

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# print(a + b)


# a = 5
# b = 10
# print(f'{a + b=}')


a = 7
film = input('Введите название фильма:')
rating = float(input('Укажите рейтинг фильма от 0 до 10:'))
print(f'Ваш фильм: {film}. Рейтинг фильма: {round(rating, 1)}.\nПриемлемо для просмотра: {rating > a}')
