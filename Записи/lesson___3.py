"""
13.12.2023
1. Блок-схема погодного приложения
- Нарисуйте блок-схему погодного приложения со следующей логикой:
Пользователь вводит температуру в градусах Цельсия
Пользователь вводит описание погоды (солнечно - пасмурно)
Если температура больше 20 градусов - выводим сообщение "Сегодня тепло"
Если температура ниже 20 градусов - выводим сообщение "Оденься потеплее"
Если на улице солнечно - выводим сообщение "Не забудь солнечные очки"
Если на улице пасмурно - выводим сообщение "Не забудь зонт"

"""

# degree_data = int(input('Введите градусы: '))
# weather_data = input('Состояние погоды (солнечно - пасмурно): ')
#
# if degree_data >= 20:
#     print('Сегодня тепло')
# else: print('Оденься потеплее')
#
# if weather_data == 'солнечно':
#     print('Не забудь солнечные очки')
# else: print('Не забудь зонт')

user_mark = int(input('Введите оценку по 100 бальной системе: '))

if 0 < user_mark <= 20:
    print('Ужасно')
elif 20 < user_mark <= 40:
    print('Плохо')
elif 40 < user_mark <= 60:
    print('Удовлетворительно')
elif 60 < user_mark <= 80:
    print('Хорошо')
elif 80 < user_mark <= 100:
    print('Отлично')
else: print('Некорректный ввод')
