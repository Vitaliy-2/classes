-- Домашнее задание по SQL №43
-- Проектирование базы данных для учебного заведения с использованием SQLite.


-- 1. Связь один-к-одному:

-- Таблица со студентами
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID)
);


-- Таблица со студенческими билетами
CREATE TABLE StudentCards (
    StudentCardID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER,
    DateOfIssue TEXT,
    DateOfExpiry TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
);




-- 2. Связь один-ко-многим:


-- Таблица со студентами
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FacultyID INTEGER,
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID)
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID)
);


-- Таблица с факультетами
CREATE TABLE Faculties (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    FacultyName TEXT UNIQUE NOT NULL,
    Director TEXT
);




-- 3. Связь многие-ко-многим:


-- Таблица с преподавателями
CREATE TABLE Teachers (
    TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT DEFAULT 'Неизвестно',
    LastName TEXT
);


-- Связующая таблица преподавателей и факультетов
CREATE TABLE TeachersFaculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TeacherID INTEGER,
    FacultyID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID),
    UNIQUE (TeacherID, FacultyID)
);



