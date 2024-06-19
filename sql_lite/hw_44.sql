-- Домашнее задание по SQL №44
-- Чтение данных с группировкой и агрегатными функциями и JOIN


-- Задание 1.
-- Общее количество персонажей по статусу

SELECT LivingStatus.status, COUNT(MarvelCharacters.id) as Количечство
FROM MarvelCharacters
JOIN LivingStatus ON MarvelCharacters.status_id = LivingStatus.status_id
GROUP BY LivingStatus.status;

-- Результат: 2 строки (3765 и 12608).



-- Задание 2.
-- Среднее количество появлений персонажей с разным цветом глаз

SELECT EyeColor.color, round(avg(MarvelCharacters.APPEARANCES), 1) as "Среднее количество"
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id
GROUP BY EyeColor.color;

-- Результат: 24 строк.



-- Задание 3.
-- Максимальное количество появлений у персонажей с определенным цветом волос

SELECT HairColor.color, max(MarvelCharacters.APPEARANCES) as MaxApp
FROM MarvelCharacters
JOIN HairColor ON MarvelCharacters.hair_id = HairColor.hair_id
GROUP BY HairColor.color;

-- Результат: 25 строк.



-- Задание 4.
-- Минимальное количество появлений среди персонажей с известной и публичной личностью

SELECT Identity.identity, min(MarvelCharacters.APPEARANCES) as MinApp
FROM MarvelCharacters
JOIN Identity ON MarvelCharacters.identity_id = Identity.identity_id
WHERE Identity.identity = "Public Identity"
GROUP BY Identity.identity;

-- Результат: 1 строка.



-- Задание 5.
-- Общее количество персонажей по полу

SELECT Sex.name, COUNT(MarvelCharacters.id) as Количество
FROM MarvelCharacters
JOIN Sex ON MarvelCharacters.sex_id = Sex.sex_id
GROUP BY Sex.name;

-- Результат: 4 строк.



-- Задание 6.
-- Средний год первого появления персонажей с различным типом личности

SELECT Identity.identity, round(avg(MarvelCharacters.Year), 0) as "Средний год"
FROM MarvelCharacters
JOIN Identity ON MarvelCharacters.identity_id = Identity.identity_id
GROUP BY Identity.identity;

-- Результат: 4 строк.



-- Задание 7.
-- Количество персонажей с разным цветом глаз среди живых

SELECT EyeColor.color, COUNT(MarvelCharacters.id) as Количество
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id
JOIN LivingStatus ON MarvelCharacters.status_id = LivingStatus.status_id
WHERE LivingStatus.status = "Living Characters"
GROUP BY EyeColor.color;

-- Результат: 24 строк.



-- Задание 8.
-- Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос

SELECT HairColor.color, max(MarvelCharacters.APPEARANCES) as MaxApp, min(MarvelCharacters.APPEARANCES) as MinApp
FROM MarvelCharacters
JOIN HairColor ON MarvelCharacters.hair_id = HairColor.hair_id
GROUP BY HairColor.color;

-- Результат: 25 строк.



-- Задание 9.
-- Количество персонажей с различным типом личности среди умерших

SELECT Identity.identity, COUNT(MarvelCharacters.id) as Количество
FROM MarvelCharacters
JOIN Identity ON MarvelCharacters.identity_id = Identity.identity_id
JOIN LivingStatus ON MarvelCharacters.status_id = LivingStatus.status_id
WHERE LivingStatus.status = "Deceased Characters"
GROUP BY Identity.identity;

-- Результат: 4 строк.



-- Задание 10.
-- Средний год первого появления персонажей с различным цветом глаз

SELECT EyeColor.color, round(avg(MarvelCharacters.Year), 0) as "Средний год"
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id
GROUP BY EyeColor.color;

-- Результат: 24 строк.


-- Подзапросы

-- Задание 11.
-- Персонаж с наибольшим количеством появлений

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (
    SELECT MAX(APPEARANCES)
    FROM MarvelCharacters
    );

-- Результат: 1 строка (4043).



-- Задание 12.
-- Персонажи, впервые появившиеся в том же году, что и персонаж с максимальными появлениями

SELECT name, Year as Год
FROM MarvelCharacters
WHERE Year = (
    SELECT Year
    FROM MarvelCharacters
    WHERE APPEARANCES = (
        SELECT MAX(APPEARANCES)
        FROM MarvelCharacters
    )
);

-- Результат: 105 строк.



-- Задание 13.
-- Персонажи с наименьшим количеством появлений среди живых

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (
    SELECT MIN(APPEARANCES)
    FROM MarvelCharacters
    JOIN LivingStatus ON MarvelCharacters.status_id = 
    LivingStatus.status_id
        WHERE LivingStatus.status = 'Living Characters'
);

-- Результат: 4810 строк.



-- Задание 14.
-- Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета

SELECT MarvelCharacters.name, HairColor.color, max(MarvelCharacters.APPEARANCES) as APPEARANCES
FROM MarvelCharacters
JOIN HairColor ON MarvelCharacters.hair_id = HairColor.hair_id
GROUP BY MarvelCharacters.hair_id;

-- Результат: 25 строк.



-- Задание 15.
-- Персонажи с публичной личностью и наименьшим количеством появлений

SELECT mc.name, i.identity, min(mc.APPEARANCES) as APPEARANCES
FROM MarvelCharacters mc
JOIN Identity i ON mc.identity_id = i.identity_id
WHERE i.identity = 'Public Identity';

-- Результат: 1 строк.



-- Операции обновления, добавления и удаления данных


-- Задание 16.
-- Обновление статуса персонажей

BEGIN TRANSACTION;

UPDATE MarvelCharacters
SET status_id = (SELECT status_id FROM LivingStatus WHERE status = 'Living Characters')
WHERE status_id = (SELECT status_id FROM LivingStatus WHERE status = 'Deceased Characters');

-- Проверка
SELECT * FROM MarvelCharacters
WHERE status_id = (SELECT status_id FROM LivingStatus WHERE status = 'Deceased Characters');

ROLLBACK;

-- Результат: Обновить статус на "Living Characters".



-- Задание 17.
-- Добавление нового персонажа

INSERT INTO MarvelCharacters (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, GSM, status_id, APPEARANCES, FIRST_APPEARANCE, Year)
VALUES (
    999999,
    'Человек-Кодер',
    '/coderman',
    (SELECT identity_id FROM Identity WHERE identity = 'Public Identity'),
    (SELECT align_id FROM Alignment WHERE name = 'Bad Characters'),
    (SELECT eye_id FROM EyeColor WHERE color = 'Red Eyes'),
    (SELECT hair_id FROM HairColor WHERE color = 'Bold Hair'),
    (SELECT sex_id FROM Sex WHERE name = "Male Characters"),
    NULL,
    (SELECT status_id FROM LivingStatus WHERE status = 'Living Characters'),
    4444,
    'MAY2020',
    2020

);

-- Добудем нового персонажа по имени Человек-Кодер
SELECT * FROM MarvelCharacters
WHERE name = 'Человек-Кодер';

-- Результат: Добавить нового персонажа.



-- Задание 18.
-- Удаление персонажей с нулевыми появлениями

BEGIN TRANSACTION;

DELETE FROM MarvelCharacters
WHERE APPEARANCES = 0;

-- Проверка
SELECT * FROM MarvelCharacters
WHERE APPEARANCES = 0;

ROLLBACK;

-- Результат: Удаление персонажей с 0 появлениями.



-- Задание 19.
-- Обновление цвета волос персонажей

UPDATE MarvelCharacters
SET hair_id = (SELECT hair_id FROM HairColor WHERE color = 'Blond Hair')
WHERE hair_id = (SELECT hair_id FROM HairColor WHERE color = 'Strawberry Blond Hair');

-- Результат: Обновление цвета волос с Strawberry Blond Hair на Blond Hair.



-- Задание 20.
-- Добавление нового статуса

INSERT INTO LivingStatus (status)
VALUES ('Unknown Status');

-- Результат: Добавление статуса Unknown Status.




