-- Lesson 40: Запросы в одной таблице
-- 13.05.2024


-- Рабочая таблица
-- CREATE TABLE MarvelCharacters (
--     id               INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id          INTEGER,
--     name             TEXT,
--     urlslug          TEXT,
--     identify         TEXT,
--     ALIGN            TEXT,
--     EYE              TEXT,
--     HAIR             TEXT,
--     SEX              TEXT,
--     GSM              TEXT,
--     ALIVE            TEXT,
--     APPEARANCES      INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year             INTEGER
-- );



-- Логические операторы в WHERE
-- По приоритету:

-- () - скобки
-- NOT - не
-- AND - и
-- OR - или

-- Операторы сравнения в WHERE
-- = - равно
-- <> - не равно
-- > - больше
-- < - меньше
-- >= - больше или равно
-- <= - меньше или равно
-- BETWEEN - между
-- IN - в списке
-- IS NULL - пусто
-- IS NOT NULL - не пусто
-- LIKE - похоже на


-- Знакомимся с логическими операторами в SQL
-- 1. Персонажи Blond Hair и Blue Eyes
SELECT name, HAIR, eye, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = "Blond Hair" AND EYE = "Blue Eyes"
ORDER BY APPEARANCES DESC
LIMIT 5;


-- Практика
-- 2. Персонажи с красными глазами или черными волосами
-- Появлений больше 100 сортированы по году появления и по количеству появлений по убыванию


SELECT name, Hair, eye, APPEARANCES, Year
FROM MarvelCharacters
WHERE (EYE = "Red Eyes" OR HAIR = "Black Hair") 
AND APPEARANCES > 100
ORDER BY Year, APPEARANCES DESC;


SELECT name, Hair, eye, APPEARANCES, Year
FROM MarvelCharacters
WHERE (EYE = "Red Eyes" OR HAIR = "Black Hair") 
AND APPEARANCES > 100
AND EYE not null
AND Hair not null
AND year not null
ORDER BY Year, APPEARANCES DESC;


-- Практика
-- Выборка: имя, цвет глаз, количество появлений, год появления
-- Найдите персонажей с  Variable Eyes
-- Появлений больше 100, исключите все NULL значения
-- Сортировка по году появления и по количеству появлений по убыванию

SELECT name,eye, APPEARANCES, Year
FROM MarvelCharacters
WHERE EYE = "Variable Eyes"  
AND APPEARANCES > 100
AND EYE not null
AND year not null
ORDER BY Year, APPEARANCES DESC;


-- Похожий запрос, но мы ищем 4 варианта цвета глаз

-- Посмотрим вообще какой цвет глаз есть
SELECT DISTINCT eye
FROM MarvelCharacters
WHERE eye NOT NULL

-- Amber Eyes, Black Eyeballs, Black Eyes, Compound Eyes, Yellow Eyeballs

SELECT name, eye, appearances
FROM MarvelCharacters
WHERE eye IN ("Amber Eyes", "Black Eyeballs", "Black Eyes", "Compound Eyes")
and appearances > 0
ORDER BY EYE, APPEARANCES DESC


-- BETWEEN - между
-- Как это может быть без BETWEEN

SELECT name, year, appearances
FROM MarvelCharacters
WHERE year >= 1960 and year <= 1970

-- BETWEEN - между
SELECT name, year, appearances
FROM MarvelCharacters
WHERE year BETWEEN 1960 and 1970


-- LIKE - похоже на
-- % - любое количество символов
-- _ - один символ

-- Персонажи с именем начинающимся на Spider

SELECT name, year, appearances
FROM MarvelCharacters
WHERE name LIKE '%Spider %'
OR name LIKE 'Spider-%'


SELECT name, year, appearances
FROM MarvelCharacters
WHERE name LIKE '%Loki%'

SELECT name, year, eye, appearances
FROM MarvelCharacters
WHERE eye LIKE '%black%'
