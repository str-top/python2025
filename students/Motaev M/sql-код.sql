CREATE TABLE groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(100) NOT NULL,
  group_id INT NOT NULL,
  FOREIGN KEY (group_id) REFERENCES groups(id)
);

INSERT INTO groups (group_name) VALUES
  ('32-В'),
  ('PYthon41'),
  ('ИСП-41');
  
INSERT INTO students (name, group_id) VALUES
  ('Максим Мотаев', 1),
  ('Богдан Красильников', 1),
  ('Егор Васильев', 2),
  ('Анна Касым', 3),
  ('Принц Тёмный', 2);
  
SELECT students.name AS student_name, groups.group_name
FROM students
JOIN groups ON students.group_id = groups.id;

SELECT * FROM students;
