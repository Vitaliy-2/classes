-- Lesson 43
-- Аномалии. Нормализация. Целостность данных.
-- 22.05.2024

-- Простой пример связи между таблицами
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY,
    Name TEXT
);

CREATE TABLE Photos (
    PhotoID INTEGER PRIMARY KEY,
    Description TEXT,
    PersonID INTEGER,
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)
);




-- Три типа связей между таблицами:
-- 1. Один человек - одни контактные данные.
-- 2. Один ко многим. В нашем примере, одна геолокация, много фотографий.
-- 3. Многие ко многим. Один человек может быть на многих фотографиях, и на одной фотографии может быть много людей.


-- Таблица контактных данных
-- CREATE TABLE Contacts (
--     ContactID INTEGER PRIMARY KEY AUTOINCREMENT,
--     Phone TEXT,
--     Email TEXT,
--     PersonID INTEGER UNIQUE,
--     FOREIGN KEY (PersonID) REFERENCES People (PersonID)
-- );




-- ОДИН К ОДНОМУ
-- Ограничение на уникальность PersonID гарантирует, что у каждого человека будет только один набор контактных данных.
-- Ограничение телефонов гарантирует, что у разных людей не будет одинаковых телефонов.
-- Таблица телефонов
CREATE TABLE Phones (
    PhoneID INTEGER PRIMARY KEY AUTOINCREMENT,           -- Уникальный идентификатор телефона
    Phone TEXT UNIQUE,                                   -- Уникальный номер телефона
    PersonID INTEGER UNIQUE,                             -- Уникальный идентификатор человека, связанный с телефоном
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)  -- Внешний ключ на таблицу People
);

-- Таблица людей
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор человека
    FirstName TEXT,                              -- Имя человека
    MiddleName TEXT,                             -- Отчество человека
    LastName TEXT                                -- Фамилия человека
);

-- Сняв некоторые ограничения мы можем получить один ко многим

-- Таблица телефонов
CREATE TABLE Phones (
    PhoneID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор телефона
    Phone TEXT UNIQUE,                          -- Уникальный номер телефона
    PersonID INTEGER,                           -- ОДИН человек может оставить МНОГО телефонов
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)  -- Внешний ключ на таблицу People
);


-- МЫ не ограничили уникальность PersonID, теперь у одного человека может быть несколько телефонов
-- Таблица людей
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор человека
    FirstName TEXT,                              -- Имя человека
    MiddleName TEXT,                             -- Отчество человека
    LastName TEXT                                -- Фамилия человека
);




CREATE Photos (
    PhotoID INTEGER PRIMARY KEY AUTOINCREMENT,
    Description TEXT,
    PersonID INTEGER,
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)
);



-- МНОГИЕ КО МНОГИМ. Связующая таблица PhotosPeople
CREATE TABLE PhotosPeople (
    
    PhotoID INTEGER,
    PersonID INTEGER,

    FOREIGN KEY (PhotoID) REFERENCES Photos (PhotoID),
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)

);





-- Практика
-- Студенты, Студенческие билеты, Факультеты, Преподаватели

-- 1. Студенты и студенческие билеты (один к одному)
-- Students: StudentID, FirstName, LastName, StudentCardID
-- StudentCards: StudentCardID, StudentID, DateOfIssue, DateOfExpiry
-- Подумайте, как обеспечить связь один - к - одному между студентами и студенческими билетами.

-- У студентов не может быть двух студенческих билетов, и у студенческого билета не может быть двух студентов.



CREATE TABLE StudentsTwo (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID)
);



CREATE TABLE StudentCards (
    StudentCardID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER UNIQUE,
    DateOfIssue TEXT,
    DateOfExpiry TEXT,
    FOREIGN KEY (StudentID) REFERENCES StudentsTwo (StudentID)
);



-- 2. Студенты и факультеты (один ко многим)
-- Students: Таблица уже есть. Надо добавить поле FacultyID (Команда ALTER TABLE) или пересоздать таблицу.
-- Faculties: FacultyID, FacultyName, Director
-- Подумайте, как обеспечить связь один - ко - многим между студентами и факультетами.
-- У студента может быть только один факультет, но у факультета может быть много студентов.


CREATE TABLE StudentsFree (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FacultyID INTEGER,
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID)
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID)
);



CREATE TABLE Faculties (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    FacultyName TEXT,
    Director TEXT
);




-- 3. Преподаватели и факультеты (многие ко многим)
-- Teachers: TeacherID, FirstName, LastName
-- TeachersFaculties: TeacherID, FacultyID
-- Вам надо правильно описать связующую таблицу. У преподавателя может быть много факультетов, и у факультета может быть много преподавателей.
-- Давайте подумаем, как обеспечить связь многие - ко - многим между преподавателями и факультетами.
-- При этом не определив на дважды или трижды одного препода на одном факультете, и наоборот.



CREATE TABLE Teachers (
    TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT
);


CREATE TABLE TeachersFaculties (
    TeacherID INTEGER,
    FacultyID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID)
);


DROP TABLE IF EXISTS TeachersFaculties;