CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    group_name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    department VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    semester INT,
    exam_type VARCHAR(20) CHECK (exam_type IN ('экзамен', 'зачёт'))
);

DELETE FROM students;
DELETE FROM teachers;
DELETE FROM courses;

INSERT INTO students (first_name, last_name, group_name) VALUES
('Иван', 'Иванов', 'Группа 101'),
('Петр', 'Петров', 'Группа 102'),
('Анна', 'Сидорова', 'Группа 103'),
('Елена', 'Смирнова', 'Группа 101');

INSERT INTO teachers (full_name, department) VALUES
('Сергей Владимирович Новиков', 'Кафедра математики'),
('Ольга Александровна Павлова', 'Кафедра информатики'),
('Дмитрий Иванович Соколов', 'Кафедра физики');

INSERT INTO courses (title, semester, exam_type) VALUES
('Математический анализ', 1, 'экзамен'),
('Программирование на Python', 2, 'зачёт'),
('Физика', 1, 'экзамен'),
('Базы данных', 3, 'зачёт'),
('Алгоритмы и структуры данных', 4, 'экзамен');

SELECT 'Студенты из группы 101:' AS query_title;
SELECT * FROM students WHERE group_name = 'Группа 101';

SELECT 'Курсы с экзаменом:' AS query_title;
SELECT * FROM courses WHERE exam_type = 'экзамен';

SELECT 'Преподаватели кафедры информатики:' AS query_title;
SELECT * FROM teachers WHERE department = 'Кафедра информатики';

UPDATE students SET last_name = 'Ивановский' 
WHERE first_name = 'Иван' AND last_name = 'Иванов';
SELECT 'После изменения фамилии студента:' AS query_title;
SELECT * FROM students WHERE id = 1;

UPDATE courses SET exam_type = 'экзамен' 
WHERE title = 'Программирование на Python';
SELECT 'После изменения формы оценки курса:' AS query_title;
SELECT * FROM courses WHERE title = 'Программирование на Python';

DELETE FROM teachers 
WHERE full_name = 'Дмитрий Иванович Соколов';
SELECT 'После удаления преподавателя:' AS query_title;
SELECT * FROM teachers;

SELECT 'Финальное состояние таблицы students:' AS query_title;
SELECT * FROM students;
SELECT 'Финальное состояние таблицы teachers:' AS query_title;
SELECT * FROM teachers;
SELECT 'Финальное состояние таблицы courses:' AS query_title;
SELECT * FROM courses;
