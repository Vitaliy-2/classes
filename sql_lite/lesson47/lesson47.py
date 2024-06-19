# Lesson 47
# 05.06.2024
# SQLite3 - встроенная библиотека для работы с базами данных

# Методы объекта подключения:
# commit() - сохранение изменений
# close() - закрытие соединения
# rollback() - откат изменений

# Основные методы курсора:
# execute() - выполнение запроса
# executemany() - выполнение запроса много раз
# executescript() - выполнение нескольких запросов
# fetchone() - получение одной строки результата
# fetchall() - получение всех строк результата
# fetchmany() - получение заданного количества строк результата


import sqlite3

ROW_SQL = """

-- Таблица котики
-- id, name, id_shop

CREATE TABLE Cats (
    CatID INTEGER PRIMARY KEY AUTOINCREMENT,
    CatName TEXT,
    ShopID INTEGER,
    FOREIGN KEY (ShopID) REFERENCES Shops (ShopID)
);

-- Таблица магазинов
-- ShopID, ShopName

CREATE TABLE Shops (
    ShopID INTEGER PRIMARY KEY AUTOINCREMENT,
    ShopName TEXT
);

-- Добавим 3 магазина и 4й без названия
INSERT INTO Shops (ShopName) VALUES
    ('Зоомагазин "Котики"'),
    ('Зоомагазин "Кошки"'),
    ('Зоомагазин "Коты"'),
    (NULL);

-- Добавим несколько котиков с именем, и без имени
INSERT INTO Cats (CatName, ShopID) VALUES
    ('Мурка', 1),
    ('Барсик', 2),
    ('Матроскин', 4),
    (NULL, 3);

"""

import os

# # Определение пути к базе данных относительно текущего местоположения скрипта
# script_dir = os.path.dirname(__file__)
# db_path = os.path.join(script_dir, 'lesson_47.db')

# print(db_path)

# # Создание объекта подключения к базе данных lesson47.db
# conn = sqlite3.connect(db_path)



# # Создание объекта курсора - это основной объект для выполнения запросов
# cursor = conn.cursor()

# Выполнение скрипта
# cursor.executescript(ROW_SQL)

# Созранение изменений
# conn.commit()



# Делаем котикам SQL инъекцию!
# НЕ безопасный запрос
# SQL_INJECTION = "SELECT * FROM Cats WHERE CatID = {};"
# cat_id = "1 OR 1 = 1"

# cursor.execute(SQL_INJECTION.format(cat_id))

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# print('-------------------')
# Сделаем правильно!
# Безопасный запрос
# Знак вопроса ? позволяет получить только одно значение
# а не всю базу данных. То есть запрещает ставить выражения
# SAFE_SQL = "SELECT * FROM Cats WHERE CatID = ?;"
# cursor.execute(SAFE_SQL, (1,))

# rows = cursor.fetchall()
# for row in rows:
#     print(row)



# Создадим список кортежей для добавления новых котиков
# new_cats = [
#     ('Белка', 1),
#     ('Стрелка', 2),
#     ('Кекс', 3),
#     ('Дунька', 4),
# ]

# # # Добавим новых котиков

# # # Создадим параметризованный запрос для executemany
# INSERT_SQL = "INSERT INTO Cats (CatName, ShopID) VALUES (?, ?);"

# # Выполним запрос
# cursor.executemany(INSERT_SQL, new_cats)

# # Сохранение изменений
# conn.commit()


# Задание

# Определение пути к базе данных относительно текущего местоположения скрипта
script_dir = os.path.dirname(__file__)
db_path = os.path.join(script_dir, 'lesson_47.db')

# Взяли абсолютный путь до файла, и добавили /lesson_47.sql
SQL_FILE = os.path.join(script_dir, 'lesson47.sql')


def connect_to_db(db_name: str) -> sqlite3.Connection:
    """Подключается к базе данных SQLite"""
    return sqlite3.connect(db_name)


def create_tables(connection: sqlite3.Connection) -> None:
    """Создает таблицы в базе данных"""
    with open(SQL_FILE, 'r') as f:
        connection.executescript(f.read())


def main() -> None:
    connection = connect_to_db(db_path)
    create_tables(connection)
    connection.close()


if __name__ == '__main__':
    main()







