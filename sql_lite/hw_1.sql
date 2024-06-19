-- Домашнее задание по SQL №1
-- SQL запросы к однотабличной базе данных


-- 1. Лысые злодеи 90х годов

SELECT name, Year, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = "Bald"
and ALIGN = "Bad Characters"
AND Year BETWEEN 1990 and 1999;

-- Результат: 94 строк.


-- 2. Герои с тайной идентичностью и необычными глазами

SELECT name, FIRST_APPEARANCE, EYE
FROM MarvelCharacters
WHERE identify = "Secret Identity"
and EYE not in ("Blue Eyes", "Brown Eyes", "Green Eyes")
AND FIRST_APPEARANCE not NULL;

-- Результат: 1028 строк.


-- 3. Персонажи с изменяющимся цветом волос

SELECT name, HAIR
FROM MarvelCharacters
WHERE Hair = "Variable Hair";

-- Результат: 32 строк.


-- 4. Женские персонажи с редким цветом глаз

SELECT name, EYE
FROM MarvelCharacters
WHERE sex = "Female Characters"
and EYE in ("Gold Eyes", "Amber Eyes");

-- Результат: 5 строк.


-- 5. Персонажи без двойной идентичности, сортированные по году появления

SELECT name, year
FROM MarvelCharacters
WHERE identify = "No Dual Identity"
ORDER BY Year DESC;

-- Результат: 1788 строк.


-- 6. Герои и злодеи с необычными прическами

SELECT name, ALIGN, Hair
FROM MarvelCharacters
WHERE Hair not in ("Brown Hair", "Black Hair", "Red Hair", "Blond Hair")
AND ALIGN in ("Good Characters", "Bad Characters");

-- Результат: 2744 строк.


-- 7. Персонажи, появившиеся в определённое десятилетие

SELECT name, Year
FROM MarvelCharacters
WHERE year BETWEEN 1960 and 1969;

-- Результат: 1306 строк.


-- 8. Персонажи с уникальным сочетанием цвета глаз и волос

SELECT name, EYE, Hair
FROM MarvelCharacters
WHERE eye = "Yellow Eyes"
and Hair = "Red Hair";

-- Результат: 13 строк.


-- 9. Персонажи с ограниченным количеством появлений

SELECT name, appearances
FROM MarvelCharacters
WHERE appearances < 10;

-- Результат: 11938 строк.


-- 10. Персонажи с наибольшим количеством появлений

SELECT name, appearances
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5;

-- Результат: 5 строк.


-- 11. Персонажи, появившиеся только в одном десятилетии

SELECT name, Year
FROM MarvelCharacters
WHERE year BETWEEN 2000 and 2009;

-- Результат: 3086 строк.


-- 12. Персонажи с самыми редкими цветами глаз

SELECT name, EYE
FROM MarvelCharacters
WHERE EYE in ("Magenta Eyes", "Pink Eyes", "Violet Eyes");

-- Результат: 34 строк.


-- 13. Герои с публичной идентичностью, сортированные по году

SELECT name, identify, Year
FROM MarvelCharacters
WHERE identify = "Public Identity"
ORDER BY Year;

-- Результат: 4528 строк.


-- 14. Персонажи с конкретным цветом волос и глаз, упорядоченные по имени

SELECT name, Hair, eye
FROM MarvelCharacters
WHERE Hair = "Black Hair"
and eye = "Green Eyes"
ORDER BY name;

-- Результат: 99 строк.


-- 15. Злодеи с нестандартными физическими характеристиками

SELECT name, sex
FROM MarvelCharacters
WHERE ALIGN = "Bad Characters"
and sex not in ("Male Characters", "Female Characters");

-- Результат: 20 строк.


-- 16. Название: Персонажи с наибольшим числом появлений по полу

SELECT name, sex as Пол, MAX(APPEARANCES) as MaxApp
FROM MarvelCharacters
WHERE sex is not null and sex in ("Male Characters", "Female Characters")
GROUP BY sex;

-- Результат: Susan Storm, Spider-Man.


-- 17. Название: Сравнение популярности персонажей по цвету волос и глаз

SELECT Hair, eye, SUM(APPEARANCES) as TotalApp
FROM MarvelCharacters
WHERE hair not null and eye not null
GROUP BY hair, eye
HAVING TotalApp is not NULL
ORDER BY TotalApp DESC;

-- Результат: 196 строк.


-- 18. Название: Персонажи с максимальным количеством появлений в десятилетие

SELECT name, MAX(APPEARANCES), DECADE
FROM (
    SELECT name, APPEARANCES, (year / 10) * 10 as DECADE
    FROM MarvelCharacters
    WHERE YEAR is not null and year > 1939
)
GROUP BY DECADE
ORDER BY DECADE;

-- Результат: 8 строк.


-- 19. Название: Герои и злодеи 80-х

SELECT ALIGN, COUNT(*) as COUNT
FROM MarvelCharacters
WHERE YEAR is not null and year BETWEEN 1980 and 1989
and ALIGN in ("Good Characters", "Bad Characters")
GROUP BY ALIGN;

-- Результат: Bad Characters - 920, Good Characters - 674.


-- 20. Название: Самые популярные прически супергероев

SELECT Hair, SUM(APPEARANCES) as TotalApp
FROM MarvelCharacters
WHERE hair not null
GROUP BY hair
ORDER BY TotalApp DESC
LIMIT 3;

-- Результат: 1. Black Hair, 2. Brown Hair. 3. Blond Hair.


-- 21. Название: Сколько Гитлеров вы насчитали?

SELECT name, appearances
FROM MarvelCharacters
WHERE name LIKE '%Hitler%'
ORDER BY name;

-- Результат: 2 персонажа (Adolf Hitler и Adolf Hitler (Clone))
