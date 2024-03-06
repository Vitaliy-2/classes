# Задача №2

# Пользовательский ввод
numbers_input = input('Введите номера телефонов через точку с запятой: ')
numbers_list = numbers_input.split(';')

# Цикл перебора номеров из списка
for phone_number in numbers_list:
    # Удаляем все лишние символы
    clear_number = (phone_number.replace('+', '').replace(' ', '')
                    .replace('(', '').replace(')', '').replace('-', ''))
    # Проверка начинается ли номер с 8, +7 или +(7
    if not (phone_number.startswith('8') or phone_number.startswith('+7') or phone_number.startswith('+(7')):
        # Печатаем ошибку, при неверном вводе номера
        raise ValueError(f'Номер телефона {phone_number} не соответствует формату!\n'
                         f'Начинаться номер должен с 8, +7 или +(7')
    # Проверка на длину
    if len(clear_number) != 11:
        # Печатаем ошибку, при неверном вводе номера
        raise ValueError(f'Номер телефона {phone_number} не соответствует формату!\n'
                         f'Номер больше или меньше 11 цифр!')
    # Проверка на только цифры
    if not clear_number.isdigit():
        # Печатаем ошибку, при неверном вводе номера
        raise ValueError(f'Номер телефона {phone_number} не соответствует формату!\n'
                         f'Номер должен состоять только из цифр!')
# Если номера прошли проверки, печатаем список правильных номеров
else:
    print(f'\nВведенный список номеров прошел проверку:\n'
          f'{numbers_list}')
