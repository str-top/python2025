CREATE TABLE students (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  group_name VARCHAR(20) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE teachers (
  id INT NOT NULL AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  department VARCHAR(50) NOT NULL,  
  PRIMARY KEY(id)
);

CREATE TABLE courses (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  semester INT,
  exam_type VARCHAR(10),
  PRIMARY KEY(id)
);

INSERT INTO students (first_name, last_name, group_name)
VALUES ('Маша', 'Иванова','математика');
INSERT INTO students (first_name, last_name, group_name)
VALUES ('Саша', 'Собачкин','русский');
INSERT INTO students (first_name, last_name, group_name)
VALUES ('Ева', 'Петрова','математика');

INSERT INTO teachers (full_name, department)
VALUES ('Ольга Игоревна','школа 52');
INSERT INTO teachers (full_name, department)
VALUES ('Антон Миргулин','гимназия 1');
INSERT INTO teachers (full_name, department)
VALUES ('Павел Игоревич','лицей 2');

INSERT INTO courses (title, semester, exam_type)
VALUES ('математика', 3, 'Экзамен');
INSERT INTO courses (title, semester, exam_type)
VALUES ('английский', 2, 'Зачет');
INSERT INTO courses (title, semester, exam_type)
VALUES ('русский', 1, 'Зачет');
INSERT INTO courses (title, semester, exam_type) 
VALUES ('испанский', 4, 'Экзамен');  

-- Выборки (правильно)
SELECT first_name, last_name FROM students WHERE group_name = 'математика';
SELECT title, semester FROM courses WHERE exam_type = 'Экзамен';
SELECT full_name FROM teachers WHERE department = 'школа 52'; 

UPDATE students SET last_name = 'Мраткина' WHERE last_name = 'Иванова';
UPDATE courses SET exam_type = 'Экзамен' WHERE exam_type = 'Зачет';

DELETE FROM teachers WHERE full_name = 'Ольга Игоревна';

SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM courses;
