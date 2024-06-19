-- Lesson 39: Знакомство с SQL
-- 24.04.2024

-- SELECT - выбрать (столбцы)
-- FROM - из (таблицы)
-- ; - конец запроса
-- Регистронезависимый язык

SELECT *
FROM MarvelCharacters;

SELECT name, identify, hair, sex, appearances
FROM MarvelCharacters;

-- Мы можем использовать простую фильтрацию
-- WHERE - где, пишут после SELECT и после FROM

-- Персонажи, где появлений больше 100
SELECT name, identify, hair, appearances
FROM MarvelCharacters
WHERE appearances > 100;

-- ORDER BY - сортировать по (столбцу) DESC - по убыванию
-- Сортировка может быть по нескольким столбцам
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100
ORDER BY HAIR, name;


-- В WHERE могут быть логические условия (похожие на пайтон)
-- Приоритет логических операторов
-- () - скобки. Первыми выполняются внутри скобок
-- NOT - не
-- AND - и
-- OR - или
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100 and sex = "Female Characters"
ORDER BY APPEARANCES DESC;

-- DISTINCT - уникальные значения

SELECT DISTINCT sex
FROM MarvelCharacters
WHERE sex not null;


-- LIMIT - ограничить количество строк
-- OFFSET - пропустить строки
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year = 1962
ORDER BY APPEARANCES DESC
LIMIT 5
OFFSET 3

-- пример подзапроса - топ появлений по году человека паука)

-- Получить персонажей с разным цветом глаз
-- No Eyes, Compound Eyes, Multiple Eyes, Variable Eyes, One Eye,


SELECT name, APPEARANCES, year, eye
FROM MarvelCharacters
WHERE eye = "No Eyes" OR eye = "Compound Eyes" OR eye = "Multiple Eyes" OR eye = "Variable Eyes" OR eye = "One Eye"
ORDER BY APPEARANCES DESC

-- IN - входит в список
-- NOT IN - не входит в список

SELECT name, APPEARANCES, year, eye
FROM MarvelCharacters
WHERE eye IN ("No Eyes", "Compound Eyes", "Multiple Eyes", "Variable Eyes", "One Eye")
ORDER BY APPEARANCES DESC


-- Список операторов которе мы сегодня посмотрели:
-- SELECT - выбрать (столбцы)
-- FROM - из (таблицы)
-- ; - конец запроса
-- WHERE - где
-- ORDER BY - сортировать по (столбцу)
-- DESC - по убыванию
-- () - скобки
-- NOT - не
-- AND - и
-- OR - или

-- DISTINCT - уникальные значения
-- LIMIT - ограничить количество строк
-- OFFSET - пропустить строки
-- IN - входит в список
-- NOT IN - не входит в список
