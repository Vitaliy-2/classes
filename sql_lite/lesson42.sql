-- Lesson 42
-- 20.05.2024

-- CREATE TABLE
-- IF NOT EXISTS - если таблицы еще нет в базе
-- INSERT INTO
-- UPDATE
-- DELETE



-- Создание таблицы студенты
-- Типы данных в SQLite:
-- NULL - пусто
-- INTEGER - целое число
-- REAL - число с плавающей точкой
-- TEXT - текст
-- BLOB - двоичные данные
-- NUMERIC - число
-- INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор, который автоматически увеличивается на 1
-- AUTOINCREMENT - КАЖДАЯ ЗАПИСЬ БУДЕТ ЧИСЛО +1
-- ALTER - изменить таблицу


CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER,
    group_number TEXT,
    auditory TEXT,
    proffesors TEXT
);

-- Вставка данных в таблицу студенты
-- Добавим пустую запись

INSERT INTO Students DEFAULT VALUES;

-- DEFAULT VALUES - вставка пустой записи

-- DROP TABLE - удаление таблицы

-- Удалим таблицу студенты
DROP TABLE IF EXISTS Students;



-- Создадим более строгую таблицу студенты
-- UNIQUE - уникальное значение
-- NOT NULL - не пустое значение

-- CREATE TABLE IF NOT EXISTS Students (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT,
--     surname TEXT,
--     age INTEGER,
--     group_number TEXT,
--     auditory TEXT,
--     proffesors TEXT
-- );


CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    student_id TEXT UNIQUE NOT NULL,
    group_number TEXT,
    proffesors TEXT
);
    -- Обозначим уникальность для группы first_name, middle_name, last_name
    -- UNIQUE (first_name, middle_name, last_name)

    -- Составной первичный ключ по столбцам first_name, middle_name, last_name
    -- PRIMARY KEY (first_name, middle_name, last_name)


-- Вставим данные в таблицу студенты (несколько записей)
INSERT INTO Students (first_name, middle_name, last_name, age, student_id, group_number, proffesors)
VALUES ('Иван', 'Семёнович', 'Бурунов', 20, '123456', 'ИС-19-1', 'Галустян С.Б.'),
       ('Петр', 'Моисеевич', 'Моисеев', 21, '123457', 'ИС-19-1', 'Масляков П.П.'),
       ('Сидор', 'Бедросович', 'Киркин', 22, '123458', 'ИС-19-1', 'Воля П.С.');


SELECT *
FROM Students;


-- Обновление данных в таблице студенты
-- Добавим всем 1 год к возрасту

UPDATE Students
SET age = age + 1;


-- Переведем Киркина в другую группу

-- Мы можем перепроверить, что это нужный Киркин
SELECT * FROM Students
WHERE last_name = 'Киркин';

-- И уже вносим изменения
UPDATE Students
SET group_number = 'ИС-19-2'
WHERE last_name = 'Киркин';


-- Или же сделать это найдя ID через подзапрос
UPDATE Students
SET group_number = 'ИС-19-2'
WHERE id = (
    SELECT id
    FROM Students
    WHERE last_name = 'Киркин'
    and first_name = 'Сидор'
    LIMIT 1
);



-- Добавим студента в группу ИС-19-2
-- Басков Александр, 20 лет, 123459, ИС-19-2

INSERT INTO Students (first_name, last_name, age, student_id, group_number)
VALUES ('Александр', 'Басков', 20, '123459', 'ИС-19-2');

SELECT * FROM Students;


-- Удалим студента по ID
DELETE FROM Students
WHERE id = 4;


-- Добавим столбец средний балл
-- ALTER - изменить таблицу
ALTER TABLE Students
ADD COLUMN average_score REAL;

-- Обновим средний балл для студентов
UPDATE Students
SET average_score = 4.5;


-- Добавить столбец со значением по умолчанию
-- ALTER - изменить таблицу
ALTER TABLE Students
ADD COlUMN is_student INTEGER DEFAULT 1;



-- Удалить столбец в SQLite нельзя
-- Нам надо создать новую таблицу и перенести данные

-- Транзакции - это группа операций, которые выполняются как единое целое
-- Начало транзакции - BEGIN TRANSACTION
-- Коммит транзакции - COMMIT
-- Откат транзакции - ROLLBACK

-- Начнем транзакцию
BEGIN TRANSACTION;

-- Создадим новую таблицу
CREATE TABLE IF NOT EXISTS Students_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    student_id TEXT UNIQUE NOT NULL,
    group_number TEXT
);


-- Перенесем данные из старой таблицы в новую
INSERT INTO Students_new (first_name, middle_name, last_name, age, student_id, group_number)
SELECT first_name, middle_name, last_name, age, student_id, group_number
FROM Students;


-- Удалим старую таблицу
DROP TABLE IF EXISTS Students;

-- Изменим название новой таблицы
ALTER TABLE Students_new
RENAME TO Students;


-- Перед завершением транзакции лучше посмотреть что получается,
-- и только потом комитить (завершать транзакцию)
SELECT * FROM Students;

-- Закончим транзакцию
COMMIT;

SELECT * FROM Students;





