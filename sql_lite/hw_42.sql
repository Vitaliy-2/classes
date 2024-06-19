-- Домашнее задание по SQL №42
-- Создание и Импорт Данных в Базу данных `marvel`


-- Задание 1.
-- Создание Базы Данных 'marvel'
-- Создание таблицы

CREATE TABLE MarvelCharacters (  
    page_id          INTEGER,  
    name             TEXT,  
    urlslug          TEXT,  
    identify         TEXT,  
    ALIGN            TEXT,  
    EYE              TEXT,  
    HAIR             TEXT,  
    SEX              TEXT,  
    GSM              TEXT,  
    ALIVE            TEXT,  
    APPEARANCES      INTEGER,  
    FIRST_APPEARANCE TEXT,  
    Year             INTEGER  
);

-- Импорт данных из marvel.csv



-- Задание 2.
-- Создание Новой Таблицы `MarvelCharacters_new`

CREATE TABLE MarvelCharacters_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id INTEGER,  
    name TEXT,  
    urlslug TEXT,  
    identify TEXT,  
    ALIGN TEXT,  
    EYE TEXT,  
    HAIR TEXT,  
    SEX TEXT,  
    GSM TEXT,  
    ALIVE TEXT,  
    APPEARANCES INTEGER,  
    FIRST_APPEARANCE TEXT,  
    Year INTEGER  
);



-- Задание 3.
-- Копирование Данных

INSERT INTO MarvelCharacters_new (page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year)
SELECT page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year
FROM MarvelCharacters;

-- Удаление староц таблицы

DROP TABLE IF EXISTS MarvelCharacters;



-- Задание 4.
-- Переименование таблицы

ALTER TABLE MarvelCharacters_new
RENAME TO MarvelCharacters;



-- Задание 5.
-- Создание Таблиц для Уникальных Значений

-- Таблица принадлежности пола
CREATE TABLE Sex (
    sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

-- Цвет глаз
CREATE TABLE EyeColor (
    eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);

-- Цвет волос
CREATE TABLE HairColor (
    hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);

-- Положительность персонажа
CREATE TABLE Alignment (
    align_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

-- Живы или нет
CREATE TABLE LivingStatus (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT UNIQUE
);

-- Личность
CREATE TABLE Identity (
    identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identity TEXT UNIQUE
);

BEGIN TRANSACTION;

-- Задание 6.
-- Наполнение Уникальных Таблиц Данными

-- Наполнение таблицы по половому признаку
INSERT INTO Sex (name)
SELECT DISTINCT SEX FROM MarvelCharacters;

-- Наполнение таблицы по цвету глаз
INSERT INTO EyeColor (color)
SELECT DISTINCT EYE FROM MarvelCharacters;

-- Наполнение таблицы по цвету волос
INSERT INTO HairColor (color)
SELECT DISTINCT HAIR FROM MarvelCharacters;

-- Наполнение таблицы по положительности персонажа
INSERT INTO Alignment (name)
SELECT DISTINCT ALIGN FROM MarvelCharacters;

-- Наполнение таблицы жизни или смерти персонажа
INSERT INTO LivingStatus (status)
SELECT DISTINCT ALIVE FROM MarvelCharacters;

-- Наполнение таблицы с личностями
INSERT INTO Identity (identity)
SELECT DISTINCT Identify FROM MarvelCharacters;

COMMIT;


BEGIN TRANSACTION;
-- Задание 7.
-- Создание Таблицы `MarvelCharacters_New` с Внешними Ключами

CREATE TABLE MarvelCharacters_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id INTEGER,  
    name TEXT,  
    urlslug TEXT,  
    identity_id INTEGER,
    align_id INTEGER,
    eye_id INTEGER,
    hair_id INTEGER,
    sex_id INTEGER,
    GSM TEXT,  
    status_id INTEGER,
    APPEARANCES INTEGER,  
    FIRST_APPEARANCE TEXT,  
    Year INTEGER,
    FOREIGN KEY (identity_id) REFERENCES Identity (identity_id),
    FOREIGN KEY (align_id) REFERENCES Alignment (align_id),
    FOREIGN KEY (eye_id) REFERENCES EyeColor (eye_id),
    FOREIGN KEY (hair_id) REFERENCES HairColor (hair_id),
    FOREIGN KEY (sex_id) REFERENCES Sex (sex_id),
    FOREIGN KEY (status_id) REFERENCES LivingStatus (status_id)
);

COMMIT;



-- Задание 8.
-- Наполнение Новой Таблицы Данными

-- Заполнение таблицы MarvelCharacters_New данными
BEGIN TRANSACTION;

INSERT INTO MarvelCharacters_New (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, GSM, status_id, APPEARANCES, FIRST_APPEARANCE, Year)

SELECT mc.page_id, mc.name, mc.urlslug, id.identity_id, al.align_id, ec.eye_id, hc.hair_id, sx.sex_id, mc.GSM, ls.status_id, mc.APPEARANCES, mc.FIRST_APPEARANCE, mc.Year

FROM MarvelCharacters mc
LEFT JOIN Identity id ON mc.identify = id.identity
LEFT JOIN Alignment al ON mc.ALIGN = al.name
LEFT JOIN EyeColor ec ON mc.EYE = ec.color
LEFT JOIN HairColor hc ON mc.HAIR = hc.color
LEFT JOIN SEX sx ON mc.SEX = sx.name
LEFT JOIN LivingStatus ls ON mc.ALIVE = ls.status;

COMMIT;



-- Задание 9 и 10.
-- Удаление Старой и Переименование Новой Таблицы

-- Удаление староц таблицы
DROP TABLE IF EXISTS MarvelCharacters;

-- Переименование таблицы
ALTER TABLE MarvelCharacters_new
RENAME TO MarvelCharacters;


-- Проверка работоспособности БД через полноценный запрос
SELECT mc.name, mc.APPEARANCES, mc.FIRST_APPEARANCE, mc.Year,
          s.name as Sex, ec.color as EyeColor, hc.color as HairColor, 
          al.name as Alignment, ls.status as LivingStatus, id.identity as Identity
   FROM MarvelCharacters mc
   JOIN Sex s ON mc.sex_id = s.sex_id
   JOIN EyeColor ec ON mc.eye_id = ec.eye_id
   JOIN HairColor hc ON mc.hair_id = hc.hair_id
   JOIN Alignment al ON mc.align_id = al.align_id
   JOIN LivingStatus ls ON mc.status_id = ls.status_id
   JOIN Identity id ON mc.identity_id = id.identity_id;


