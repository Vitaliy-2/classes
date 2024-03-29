"""
Lesson 8
18.12.2023

- Работа со строками
- Методы строк
- Вложенные условия
- Практика
- Совмещаем с логическими операторами и методами строк
- Реализация сложных проверок (вложенные условия) VS плоская структура

Методы строк. От самых часто используемых к менее используемым

str.lower() - приводит строку к нижнему регистру
str.upper() - приводит строку к верхнему регистру
str.replace() - заменяет одну подстроку на другую
str.split() - разделяет строку на части по разделителю
str.join() - склеивает строки в одну строку с помощью разделителя
str.capitalize() - приводит строку к виду "Слово cлово слово"
str.title() - приводит строку к виду "Слово Слово Слово"
str.strip() - удаляет пробелы в начале и в конце строки
str.count() - считает количество вхождений подстроки в строку
str.find() - возвращает индекс первого вхождения подстроки в строку
str.index() - возвращает индекс первого вхождения подстроки в строку
str.startswith() - проверяет, начинается ли строка с подстроки
str.endswith() - проверяет, заканчивается ли строка подстрокой
str.isalpha() - проверяет, состоит ли строка только из букв
str.isdigit() - проверяет, состоит ли строка только из цифр
str.isalnum() - проверяет, состоит ли строка только из цифр и букв
str.isspace() - проверяет, состоит ли строка только из пробелов
str.istitle() - проверяет, является ли строка заголовком
str.islower() - проверяет, состоит ли строка только из символов в нижнем регистре
str.isupper() - проверяет, состоит ли строка только из символов в верхнем регистре
str.lstrip() - удаляет пробелы в начале строки
str.rstrip() - удаляет пробелы в конце строки
str.swapcase() - меняет регистр каждой буквы в строке на противоположный
str.rfind() - возвращает индекс последнего вхождения подстроки в строку
str.rindex() - возвращает индекс последнего вхождения подстроки в строку
str.rsplit() - разделяет строку на части по разделителю, начиная с конца


"""
# main_string = input('Введите строку: ')
# sub_string = input('Что конкретно желаете заменить? ')
# new_sub_string = input('На что хотите заменить? ')
# print(f'Исходная строка: {main_string}')
# print(f'Новая строка: {main_string.replace(sub_string, new_sub_string)}')

user_data = input('Введите сообщение: ')
user_replace = input('Что хотите заменить? ')
user_new_words = input('На что хотите заменить? ')

user_new = user_data.replace(user_replace, user_new_words)
print(f'Исходная строка: {user_data}\nИзмененная строка: {user_new}')
