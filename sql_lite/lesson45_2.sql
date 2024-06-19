-- Lesson 45
-- 29.05.2024
-- JOIN в SQLite

-- Lesson 44
-- 27.05.2024
-- Повторяем транзакции
-- Повторяем типы отношений в БД
-- Смотрим, что будет происходить с данными при изменении и удалении
-- Начинаем изучать JOIN




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
-- CREATE TABLE TeachersFaculties (
--     TeacherID INTEGER,
--     FacultyID INTEGER,
--     PRIMARY KEY (TeacherID, FacultyID),
--     FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID) ON DELETE CASCADE,
--     FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID) ON DELETE CASCADE
-- );
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
UPDATE Students
SET StudentCardID = (
        SELECT StudentCardID
        FROM StudentCards
        WHERE StudentID = Students.StudentID
    );
-- Добавление преподавателей к факультетам
INSERT INTO TeachersFaculties (TeacherID, FacultyID)
VALUES (1, 1),
   ФИО (2, 2), ИМЯ ФАКУЛЬТЕТА
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

-- Наберем этот запрос с использованием Alias
SELECT s.StudentID, s.FirstName, s.LastName, f.FacultyName, f.Director
FROM Students s 
JOIN Faculties f ON s.FacultyID = f.FacultyID;


-- Добавим к предыдущему запросу еще и студ.билеты
SELECT s.FirstName, s.LastName, f.FacultyName, f.Director, sc.DateOfIssue, sc.DateOfExpiry
FROM Students s
JOIN Faculties f ON s.FacultyID = f.FacultyID
JOIN StudentCards sc ON s.StudentCardID = sc.StudentCardID;



-- Сделайте из этого выборку.
-- Отсейте только те позиции, где в фамилии f.Director есть "ов"
SELECT s.FirstName, s.LastName, f.FacultyName, f.Director, sc.DateOfIssue, sc.DateOfExpiry
FROM Students s
JOIN Faculties f ON s.FacultyID = f.FacultyID
JOIN StudentCards sc ON s.StudentCardID = sc.StudentCardID
WHERE f.Director LIKE '%ов%'
ORDER BY s.LastName;



-- Дадим нагрузки нашим преподам :)

-- Добавление преподавателей к факультетам
INSERT INTO TeachersFaculties (TeacherID, FacultyID)
VALUES (1, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (2, 5);



-- Начнем набирать JOIN многие-ко-многим
-- 11 В таблице не будет названий факультетов
SELECT Teachers.FirstName, Teachers.LastName, TeachersFaculties.TeacherID, TeachersFaculties.FacultyID
FROM Teachers
JOIN TeachersFaculties ON Teachers.TeacherID = TeachersFaculties.TeacherID



-- 12 Версия без сокращений (псевдонимов)
-- и добавили колонку с названиями факультетов
SELECT Teachers.FirstName, Teachers.LastName, TeachersFaculties.TeacherID, TeachersFaculties.FacultyID, Faculties.FacultyName
FROM Teachers
JOIN TeachersFaculties ON Teachers.TeacherID = TeachersFaculties.TeacherID
JOIN Faculties ON TeachersFaculties.FacultyID = Faculties.FacultyID;


-- 13  Находим все факультеты для каждого преподавателя
SELECT t.FirstName, t.LastName, f.FacultyName
FROM Teachers t
JOIN TeachersFaculties tf ON t.TeacherID = tf.TeacherID
JOIN Faculties f ON tf.FacultyID = f.FacultyID;



-- 14
-- Сложим факультеты, через запятую, чтобы небыло дубликатов ФИО
-- GROUP_CONCAT - встроенная функция, которая группирует факультеты у одного препода в одноу строчку
SELECT t.FirstName Имя, t.LastName Фамилия, GROUP_CONCAT(f.FacultyName) Факультеты
FROM Teachers t
JOIN TeachersFaculties tf ON t.TeacherID = tf.TeacherID
JOIN Faculties f ON tf.FacultyID = f.FacultyID
GROUP BY t.TeacherID;



