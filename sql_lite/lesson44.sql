-- Чтобы обеспечность связь таблиц один к одному нужно:
-- 1. Либо ослабить уникальность значений, например убрать
-- уникум у студенческих билетов, что позволит заполнять данные.
-- 2. Либо отключить в ручную у sql проверку на целостность командой:
-- Begin transation:
-- PRAGMA foreign_keys = OFF
-- И начать заполнять таблицы данными.
-- PRAGMA foreign_keys = ON
-- COMIT;
-- ЭТО НЕВОЗМОЖНО СДЕЛАТЬ.

-- Как вариант, убрать id и добавить данные в одну таблицу, а потом в другую
-- Самое просто смягчить требования и убрать уникум у студент кард.



-- Что будет происходить со связанными данными при операциях UPDATE и DELETE?
-- 1. CASCADE - при удалении или обновлении родительской записи, 
-- дочерняя запись также будет удалена или обновлена.
-- 2. SET NULL - при удалении или обновлении родительской записи, 
-- дочерняя запись будет обновлена, и в столбце, который ссылается на родительскую запись, будет NULL.
-- 3. SET DEFAULT - при удалении или обновлении родительской записи, 
-- дочерняя запись будет обновлена, и в столбце, который ссылается на родительскую запись, будет значение по умолчанию.
-- 4. NO ACTION - при удалении или обновлении родительской записи, 
-- дочерняя запись не будет удалена или обновлена.
-- 5. RESTRICT - при удалении или обновлении родительской записи, 
-- дочерняя запись не будет удалена или обновлена, если нарушается целостность данных.



CREATE TABLE StudentCards (
    StudentCardID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER,
    DateOfIssue TEXT,
    DateOfExpiry TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
);

CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FacultyID INTEGER,
    -- Если тут даем UNIQUE - это будет один к одному а не многие к одному
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID)
);

CREATE TABLE Faculties (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    FacultyName TEXT UNIQUE NOT NULL,
    Director TEXT
);

CREATE TABLE Teachers (
    TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT DEFAULT 'Неизвестно',
    LastName TEXT
);

CREATE TABLE TeachersFaculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TeacherID INTEGER,
    FacultyID INTEGER,
    DateOfAppointment TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID),
    UNIQUE (TeacherID, FacultyID)
);

-- ### Фейковые данные
-- #### Студенты:
-- 1. Иван Иванов
-- 2. Анна Петрова
-- 3. Дмитрий Сидоров
-- 4. Елена Кузнецова
-- 5. Сергей Смирнов
-- #### Факультеты:
-- 1. Информатики
-- 2. Математики
-- 3. Физики
-- 4. Химии
-- 5. Биологии
-- #### Преподаватели:
-- 1. Алексей Николаев
-- 2. Мария Федорова
-- 3. Виктор Петров
-- 4. Ольга Сидорова
-- 5. Михаил Иванов
-- 6. Татьяна Кузнецова
-- 7. Николай Смирнов
-- 8. Екатерина Васильева
-- 9. Владимир Морозов
-- 10. Наталья Павлова



-- Добавление факультетов
INSERT INTO Faculties (FacultyName, Director)
VALUES ('Информатики', 'Алексей Николаев'),
    ('Математики', 'Мария Федорова'),
    ('Физики', 'Виктор Петров'),
    ('Химии', 'Ольга Сидорова'),
    ('Биологии', 'Михаил Иванов');


-- Добавление преподавателей
INSERT INTO Teachers (FirstName, LastName)
VALUES ('Алексей', 'Николаев'),
    ('Мария', 'Федорова'),
    ('Виктор', 'Петров'),
    ('Ольга', 'Сидорова'),
    ('Михаил', 'Иванов'),
    ('Татьяна', 'Кузнецова'),
    ('Николай', 'Смирнов'),
    ('Екатерина', 'Васильева'),
    ('Владимир', 'Морозов'),
    ('Наталья', 'Павлова');


-- Добавление студентов
INSERT INTO Students (FirstName, LastName, FacultyID)
VALUES ('Иван', 'Иванов', 1),
    ('Анна', 'Петрова', 2),
    ('Дмитрий', 'Сидоров', 3),
    ('Елена', 'Кузнецова', 4),
    ('Сергей', 'Смирнов', 5);


-- Добавление студенческих билетов
INSERT INTO StudentCards (StudentID, DateOfIssue, DateOfExpiry)
VALUES (1, '2024-01-01', '2028-01-01'),
    (2, '2024-01-01', '2028-01-01'),
    (3, '2024-01-01', '2028-01-01'),
    (4, '2024-01-01', '2028-01-01');
    -- (5, '2024-01-01', '2028-01-01');


-- Допустим я НЕ знаю ID 5 но знаю что работаю с Сергеем Смирновым
INSERT INTO StudentCards (StudentID, DateOfIssue, DateOfExpiry)
VALUES (
        (
            SELECT StudentID
            FROM Students
            WHERE FirstName = 'Сергей'
                AND LastName = 'Смирнов'
        ),
        '2024-01-01',
        '2028-01-01'
    );


-- Связывание студенческих билетов со студентами
-- SET - Установить
UPDATE Students
SET StudentCardID = (
        SELECT StudentCardID
        FROM StudentCards
        WHERE StudentID = Students.StudentID
    );


-- Добавление преподавателей к факультетам
INSERT INTO TeachersFaculties (TeacherID, FacultyID)
VALUES (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 1),
    (7, 2),
    (8, 3),
    (9, 4),
    (10, 5);



-- Выборка всех студентов
SELECT *
FROM Students;

-- JOIN - объединение таблиц
-- Получим всех студентов и их факультеты
-- У нас многотабличный запрос. И нам надо явно указать откуда берем данные Таблица.Столбец

SELECT Students.FirstName, Students.LastName, Faculties.FacultyName, Faculties.Director
FROM Students
JOIN Faculties ON Students.FacultyID = Faculties.FacultyID;

--TODO - БУДЕТ ЛИ ВОЗМОЖНОСТЬ СДЕЛАТЬ ЭТО БЕЗ ВНЕШНИХ КЛЮЧЕЙ?
