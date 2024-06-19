-- Lesson 41: GROUP BY и агрегатные функции
-- 15.05.2024


-- GROUP BY и агрегатные функции
-- GROUP BY - группировка строк по значениям столбца. Похоже на DISTINCT, 
-- но с возможностью использования агрегатных функций


SELECT eye
FROM MarvelCharacters
GROUP BY EYE;

SELECT DISTINCT eye
FROM MarvelCharacters;

-- В чем разница между этими запросами? 
-- Тут мы можем сделать так:

SELECT eye, COUNT(*) as количество
FROM MarvelCharacters
GROUP BY EYE
ORDER BY количество DESC;

SELECT eye, COUNT(*)
FROM MarvelCharacters
GROUP BY EYE
ORDER BY COUNT(*) DESC;



-- Уберем Null и значения меньше 20

SELECT eye as "цвет глаз", COUNT(*) as количество
FROM MarvelCharacters
WHERE eye IS NOT NULL
GROUP BY eye
HAVING COUNT(*) > 20
ORDER BY COUNT(*) DESC;


-- В чем разница, передать * или название столбца?
-- Передать * - это считать все строки, передать название 
-- столбца - это считать только значения без NULL
SELECT eye as "цвет глаз", COUNT(eye) as количество
FROM MarvelCharacters
GROUP BY eye
HAVING COUNT(eye) > 20
ORDER BY COUNT(eye) DESC;


-- Практика
-- Посчитайте количество персонажей, критерий: hair

SELECT hair as "прическа", COUNT(*) as количество
FROM MarvelCharacters
WHERE hair is not null
GROUP BY hair
ORDER BY COUNT(*) DESC;



-- Самый популярный цвет волос персонажей 60х
-- Найдем имя персонажа, год появления и 
-- количество появлений и цвет волос через MAX и GROUP BY


SELECT name as Имя, hair as Цвет, MAX(APPEARANCES) as Появлений, year as Год, COUNT(*) as "Всего персонажей"
FROM MarvelCharacters
WHERE year BETWEEN 1960 AND 1969
AND HAIR not null
GROUP BY hair
ORDER BY COUNT(*) DESC



-- Практика 
-- Попробуйте выполнить этот запрос для eye (цвет глаз)

SELECT name AS Имя, Eye AS "Цвет глаз", year AS "Год появления", COUNT(*) AS "Всего персонажей"
FROM MarvelCharacters
WHERE (year BETWEEN 1960 AND 1969) and eye not null
GROUP BY eye
ORDER BY COUNT(*) DESC;



-- MAX - найдем персонажа с максимальным количеством появлений
SELECT name, MAX(APPEARANCES)
FROM MarvelCharacters;

SELECT MAX(YEAR) as "Последний год"
FROM MarvelCharacters;



-- Выведем персонажа с максимальной длиной имени
SELECT name, LENGTH(name)
FROM MarvelCharacters
ORDER BY LENGTH(name) DESC
LIMIT 1;



-- Простой пример подзапроса
SELECT name
FROM MarvelCharacters
WHERE APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters);

-- Без поздапроса
SELECT name, MAX(APPEARANCES)
FROM MarvelCharacters


-- НЕ РАБОТАЕТ
SELECT name
FROM MarvelCharacters
WHERE MAX(APPEARANCES)

SELECT name
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 1


SELECT name, Year
FROM MarvelCharacters
WHERE Year IN (SELECT Year FROM MarvelCharacters WHERE name
LIKE '%Spider%' OR name LIKE '%Man%')





-- 18. **Название: Персонажи с максимальным количеством появлений в десятилетие**
--     - **Описание:** Найти персонажа с максимальным количеством появлений в каждом десятилетии начиная с 1940-х. Вывести десятилетие, имя персонажа и количество появлений.
--     - **Выборка:** Группировка по десятилетиям (используя год), определение персонажа с максимальным количеством появлений в каждом десятилетии.


SELECT name, MAX(APPEARANCES) as MaxApp, DECADE
FROM (
    SELECT name, APPEARANCES, (Year / 10) * 10 as DECADE
    FROM MarvelCharacters
    WHERE YEAR is not null
)
GROUP BY DECADE
ORDER BY DECADE DESC;

