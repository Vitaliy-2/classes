# Домашнее задание по SQL №45
# Создание базы sqlite3 для блога а так же мини-ORM на Python sqlite3 библиотеке

import sqlite3
from typing import List, Tuple, Optional


# Часть 2: Реализация модуля на Python

# Функции модуля

# 1. Подключение к базе данных
def connect_to_db(db_name: str) -> sqlite3.Connection:
    """Подключается к базе данных SQLite."""
    return sqlite3.connect(db_name)


# 2. Создание курсора
def create_cursor(connection: sqlite3.Connection) -> sqlite3.Cursor:
    """Создает курсор для выполнения SQL-запросов."""
    return connection.cursor()


# 3. Создание таблиц
def create_tables(connection: sqlite3.Connection):
    """Создает таблицы в базе данных."""
    with open('sql_lite/blog_tables.sql', 'r') as f:
        connection.executescript(f.read())


# 4. Добавление нового поста
def add_post(connection: sqlite3.Connection,
            title: str,
            content: str,
            category_name: str,
            tags: list[str]):
    """Добавляет новый пост в базу данных."""
    cursor = create_cursor(connection)
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (category_name,))
    cursor.execute("SELECT category_id FROM categories WHERE name = ?", (category_name,))
    category_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO posts (title, content, category_id) VALUES (?, ?, ?)", (title, content, category_id))
    post_id = cursor.lastrowid

    for tag in tags:
        cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag,))
        cursor.execute("SELECT tag_id FROM tags WHERE name = ?", (tag,))
        tag_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (?, ?)", (post_id, tag_id))
    
    connection.commit()


# 5. Чтение всех постов
def get_all_posts(connection: sqlite3.Connection) -> list[tuple]:
    """Возвращает все записи из таблицы posts."""
    cursor = create_cursor(connection)
    cursor.execute("SELECT * FROM posts")
    return cursor.fetchall()


# 6. Чтение конкретного поста по ID
def get_post_by_id(connection: sqlite3.Connection, post_id: int) -> tuple:
    """Возвращает запись из таблицы posts по ID."""
    cursor = create_cursor(connection)
    cursor.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
    result = cursor.fetchone()

    if result is None:
        raise ValueError(f"Post with ID {post_id} does not exist.")
    
    return result


# 7. Обновление существующего поста
def update_post(connection: sqlite3.Connection,
                post_id: int,
                title: str = None,
                content: str = None,
                category_name: str = None,
                tags: list[str] = None):
    """Обновляет запись в таблице posts по ID."""
    if not any([title, content, category_name, tags]):
        raise ValueError("At least one field must be provided to update the post.")
    
    updates = []
    params = []

    if title:
        updates.append("title = ?")
        params.append(title)
    
    if content:
        updates.append("content = ?")
        params.append(content)
    
    if category_name:
        updates.append("category_id = (SELECT category_id FROM categories WHERE name = ?)")
        params.append(category_name)
    
    if updates:
        sql = f"UPDATE posts SET {', '.join(updates)}, updated_at = CURRENT_TIMESTAMP WHERE post_id = ?"
        params.append(post_id)

        with connection:
            connection.execute(sql, params)

            if tags is not None:
                with connection:
                    connection.execute("DELETE FROM post_tags WHERE post_id = ?", (post_id,))
                    for tag in tags:
                        connection.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag,))
                        connection.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (?, (SELECT tag_id FROM tags WHERE name = ?))", (post_id, tag))
                        

# 8. Удаление существующего поста
def delete_post(connection: sqlite3.Connection, post_id:int):
    """Удаляет запись из таблицы posts по ID"""
    with connection:
        connection.execute("DELETE FROM post_tags WHERE post_id = ?", (post_id,))
        connection.execute("DELETE FROM tags WHERE tag_id = ?", (post_id,))
        connection.execute("DELETE FROM categories WHERE category_id = ?", (post_id,))
        rows_affected = connection.execute("DELETE FROM posts WHERE post_id = ?", (post_id,)).rowcount

        if rows_affected == 0:
            raise ValueError("No post exists with ID {post_id}")


# 9. Основная функция запуска скрипта
def main():
    """
    Основная функция запуска скрипта.
    Создает структуру базы данных и предлагает пользователю выполнить CRUD операции.
    """
    connection = connect_to_db('sql_lite/sqlite3.db')
    create_tables(connection)

    while True:
        print("\nВыберите действие:")
        print("1 - Создать нвоый пост")
        print("2 - Прочитать все записи")
        print("3 - Прочитать запись по ID")
        print("4 - Обновить запись по ID")
        print("5 - Удалить запись по ID")
        print("0 - Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            title = input("Введите заголовок поста: ")
            content = input("Введите содержимое поста: ")
            category_name = input("Введите название категории: ")
            tags = input("Введите теги через запятую: ").split(',')
            add_post(connection, title, content, category_name.strip(), [tag.strip() for tag in tags])
            print("Пост успешно добавлен!")
        
        elif choice == '2':
            posts = get_all_posts(connection)
            for post in posts:
                print(post)
        
        elif choice == '3':
            try:
                post_id = int(input("Введите ID поста: "))
                post = get_post_by_id(connection, post_id)
                print(post)
            except ValueError as e:
                print(e)
        
        elif choice == '4':
            try:
                post_id = int(input("Введите ID поста для обновления: "))
                title = input("Введите новый заголовок (оставьте пустым для пропуска): ")
                content = input("Введите новое содержимое (оставьте пустым для пропуска): ")
                category_name = input("Введите новую категорию (оставьте пустым для пропуска): ")
                tags_input = input("Введите новые теги через запятую (оставьте пустым для пропуска): ")

                tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else None

                update_post(connection, post_id, title or None, content or None, category_name or None, tags)

                print(f"Пост с ID {post_id} успешно обновлен!")
            
            except ValueError as e:
                print(e)
        
        elif choice == '5':
            try:
                post_id = int(input("Введите ID поста для удаления: "))
                delete_post(connection, post_id)
                print(f"Пост с ID {post_id} успешно удален!")

            except ValueError as e:
                print(e)
        
        elif choice == '0':
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите один из предложенных вариантов.")


if __name__ == '__main__':
    main()
