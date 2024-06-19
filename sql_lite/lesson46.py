# Lesson 46
# 03.06.2024
# sqlite3 - встроеенная библиотека для работы с базами данных

import sqlite3

# Создание объекта подключения к базе данных
# Аргументом передается имя файла базы данных с путем
# ../ - переход на уровень выше
# ./ - текущий уровень
# если базы нет - она создается
# Можно взять полный путь C:\PY\ПРИМЕРЫ КОДА\python315\marvel_normal.db
#
# path = r"../../marvel_normal.db"


conn = sqlite3.connect('marvel.db')


# Методы объекта подключения:
# commit() - сохранение изменений
# close() - закрытие соединения
# rollback() - откат изменений

# Создание объекта курсора - это основной объект для выполнения запросов
cursor = conn.cursor()


# Основные методы курсора:
# execute() - выполнение запроса
# executemany() - выполнение запроса много раз
# fetchone() - получение одной строки результата
# fetchall() - получение всех строк результата
# fetchmany() - получение заданного количества строк результата


# Получим все записи из таблицы marvelcharacters
# cursor.execute('SELECT * FROM marvelcharacters')
# # Получение всех записей
# rows = cursor.fetchall()
# for row in rows[:5]:
#     print(row)



# Получим все записи из таблицы MarvelCharacters сортированные по Appearances
# Возьмем первое значение
    
cursor.execute("SELECT * FROM MarvelCharacters ORDER BY APPEARANCES DESC")
# row = cursor.fetchone()
# print(row)

# fetchmany() - получение заданного количества строк результата
rows = cursor.fetchmany(5)
for row in rows:
    print(row)




