
-- create
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
VALUES ('Clark', 'Sales','python');
INSERT INTO students (firstname,lastname,groupname)
VALUES ('Dave', 'Accounting','python');
INSERT INTO students (firstname,lastname,groupname)
 VALUES ('Ava', 'Sales','YT');



INSERT INTO teachers (fullname,departament)
VALUES ('Мария Ивановна','УУНИТ');
INSERT INTO teachers (fullname,departament)
VALUES ('Павел Игоревич','TOP');
INSERT INTO teachers (fullname,departament)
VALUES ('Андрей Николаевич','УУНИТ');


INSERT INTO courses (title, semester, examtype)
VALUES ('Python 41', 4, 'Экзамен');

INSERT INTO courses (title, semester, examtype)
VALUES ('Python 21', 2, 'Зачет');

INSERT INTO courses (title, semester, examtype)
VALUES ('YT 1', 1, 'Зачет');

INSERT INTO courses (title, semester, examtype)
VALUES ('VK', 4, 'Экзамен');




SELECT firstname,lastname FROM students WHERE groupname = 'python';
SELECT title,semester FROM courses WHERE examtype = 'Экзамен';
SELECT fullname FROM teachers WHERE departament = 'УУНИТ';

UPDATE students SET lastname = 'Kurchatov' WHERE lastname = 'Sales';
UPDATE courses SET examtype = 'Экзамен' WHERE examtype = 'Зачет';

DELETE FROM teachers WHERE fullname = 'Мария Ивановна';
SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM courses;
