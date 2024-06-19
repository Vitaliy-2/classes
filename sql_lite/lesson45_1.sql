-- Lesson 45
-- 29.05.2024
-- JOIN в SQLite на котиках

-- Таблица котики
-- id, name, id_shop

CREATE TABLE Cats (
    CatID INTEGER PRIMARY KEY AUTOINCREMENT,
    CatName TEXT,
    ShopID INTEGER,
    FOREIGN KEY (ShopID) REFERENCES Shops (ShopID)
)

-- Таблица магазинов
-- ShopID, ShopName

CREATE TABLE Shops (
    ShopID INTEGER PRIMARY KEY AUTOINCREMENT,
    ShopName TEXT
)


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



-- Виды JOIN
-- JOIN - он же по умолчанию INNER JOIN. Выводит только те строки, данные которых есть в обеих таблицах
-- LEFT JOIN - сделает акцент на левой таблице, и если в правой таблице нет данных, то в левой таблице будут NULL
-- RIGHT JOIN - сделает акцент на правой таблице, и если в левой таблице нет данных, то в правой таблице будут NULL
-- FULL JOIN он же OUTER JOIN - выведет все данные из обеих таблиц, и если данных нет, то NULL

-- Какая таблица левая, какая правая?
-- Мы решаем! Первая таблица - левая, вторая - правая

-- Я делаю выборку из Cats - она будет левой. Я делаю JOIN с Shops - она будет правой


SELECT * 
FROM Cats
JOIN Shops ON Cats.ShopID = Shops.ShopID;


-- В выдаче будет Null
-- Сделаем выбрку столбцов

SELECT Cats.CatName, Shops.ShopName
FROM Cats
JOIN Shops ON Cats.ShopID = Shops.ShopID;


-- Добавим Alias - псевдоним

SELECT c.CatName, s.ShopName
FROM Cats c 
JOIN Shops s ON c.ShopID = s.ShopID;


-- Добавим еще несколько котиков Рыжик Фёдор без ID магазина
INSERT INTO Cats (CatName, ShopID) VALUES
    ('Рыжик', NULL),
    ('Фёдор', NULL);

-- Добавим ID магазина для ясности.
-- Будет 3 Null. У Матроскина, который обитает в магазине ID 4 с названием NULL, и у Рыжика и Фёдора, у которых нет вообще ссылки на магазин.
-- Попробуйте все виды JOIN
-- LEFT JOIN
-- RIGHT JOIN
-- FULL JOIN
-- INNER JOIN (обычный JOIN)


SELECT c.CatName, s.ShopName, s.ShopID
FROM Cats as c
LEFT JOIN Shops as s ON c.ShopID = s.ShopID;
