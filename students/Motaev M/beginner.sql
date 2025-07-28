CREATE TABLE students (
  id INT NOT NULL AUTO_INCREMENT,
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  groupname VARCHAR(20) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE teachers (
  id INT NOT NULL AUTO_INCREMENT,
  fullname VARCHAR(100) NOT NULL,
  departament VARCHAR(50) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE courses (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  semester  INT,
  examtype  VARCHAR(10),
  PRIMARY KEY(id)
);

-- insert

INSERT INTO students (firstname,lastname,groupname)
VALUES ('Максим', 'Мотаев','python');
INSERT INTO students (firstname,lastname,groupname)
VALUES ('Богдан', 'Крутой','python');
INSERT INTO students (firstname,lastname,groupname)
 VALUES ('Егор', 'Васильев','Youtube');



INSERT INTO teachers (fullname,departament)
VALUES ('Инна Вячеславовна','СКСиПТ');
INSERT INTO teachers (fullname,departament)
VALUES ('Павел Игоревич','TOP');
INSERT INTO teachers (fullname,departament)
VALUES ('Николай Александрович','ЛИЦЕЙ №1');


INSERT INTO courses (title, semester, examtype)
VALUES ('Python', 2, 'Зачёт');

INSERT INTO courses (title, semester, examtype)
VALUES ('Математика', 1, 'Экзамен');

INSERT INTO courses (title, semester, examtype)
VALUES ('Русский язык 1', 3, 'Зачет');

INSERT INTO courses (title, semester, examtype)
VALUES ('Youtube', 4, 'Экзамен');




SELECT firstname,lastname FROM students WHERE groupname = 'python';
SELECT title,semester FROM courses WHERE examtype = 'Экзамен';
SELECT fullname FROM teachers WHERE departament = 'СКСиПТ';

UPDATE students SET lastname = 'Шишкин' WHERE lastname = 'Васильев';
UPDATE courses SET examtype = 'Экзамен' WHERE examtype = 'Зачет';

DELETE FROM teachers WHERE fullname = 'Инна Вячеславовна';
SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM courses;
