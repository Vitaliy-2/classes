# Задание №1. Проверка на правильность ввода номера.
phone_number = input('Введите номер телефона: ')

bad_report_string = ''
# Удаляем из номера лишние символы
data_number = (phone_number.replace('+', '').replace(' ', '').replace('(', '')
               .replace(')', '').replace('-', ''))

# Проверка на начало 8 или +7
if not (phone_number.startswith('8') or phone_number.startswith('+7') or phone_number.startswith('+(7')):
    bad_report_string += 'Номер должен начинаться с 8 или +7 или +(xxx)\n'
# Проверка на длину номер
if len(data_number) != 11:
    bad_report_string += 'Неверное количество цифр в номере\n'
# Проверка на то, чтобы в номере были только цифры
if not data_number.isdigit():
    bad_report_string += 'Номер должен состоять только из цифр\n'
if bad_report_string:
    print(f'Номер {phone_number} не прошел проверку\nПричины:\n{bad_report_string}')
else:
    print(f'Номер {phone_number} прошел проверку')


# Задание №2. Проверка пароля

user_password = input('Введите надежный пароль: ')
bad_password = ''

# Проверка на длину пароля
if not len(user_password) >= 7:
    bad_password += 'Пароль должен содержать 7 символов и более\n'
# Проверка на наличие пробела
if user_password.count(' ') > 0:
    bad_password += 'Пароль не должен содержать пробелы\n'
# Проверка наличия спецзнака
if user_password.isalnum():
    bad_password += 'Пароль должен содержать хотя бы один спецзнак\n'
# Проверка на регистр
if user_password.islower() or user_password.isupper():
    bad_password += 'Пароль должен содержать символы разных регистров\n'
if bad_password:
    print(f'Пароль {user_password} не прошел проверку\nПричины:\n{bad_password}')
else:
    print(f'Пароль "{user_password}" является надежным.')
