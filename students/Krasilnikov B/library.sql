-- ========================
-- 1. Создание таблиц
-- ========================

CREATE TABLE readers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    year_published INT,
    category VARCHAR(50)
);

CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    reader_id INT REFERENCES readers(id),
    loan_date DATE NOT NULL,
    return_date DATE
);

CREATE TABLE loan_items (
    loan_id INT REFERENCES loans(id),
    book_id INT REFERENCES books(id),
    loan_period INT NOT NULL, -- период выдачи в днях
    PRIMARY KEY (loan_id, book_id)
);

-- ========================
-- 2. Тестовые данные
-- ========================

INSERT INTO readers (name, city) VALUES
('Иван Иванов', 'Москва'),
('Анна Смирнова', 'Санкт-Петербург'),
('Петр Кузнецов', 'Новосибирск');

INSERT INTO books (title, author, year_published, category) VALUES
('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман'),
('Преступление и наказание', 'Федор Достоевский', 1866, 'Классика'),
('1984', 'Джордж Оруэлл', 1949, 'Антиутопия'),
('Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 'Фэнтези');

INSERT INTO loans (reader_id, loan_date, return_date) VALUES
(1, '2025-08-01', '2025-08-15'),
(1, '2025-08-05', '2025-08-20'),
(2, '2025-08-07', NULL); -- книга еще не возвращена

INSERT INTO loan_items (loan_id, book_id, loan_period) VALUES
(1, 1, 14),   -- Иван взял "Мастер и Маргарита" на 14 дней
(1, 3, 14),   -- Иван взял "1984" на 14 дней
(2, 2, 15),   -- Иван взял "Преступление и наказание" на 15 дней
(3, 4, 21);   -- Анна взяла "Гарри Поттер" на 21 день

-- ========================
-- 3. Запросы
-- ========================

-- 1. Список выданных книг с именами читателей
SELECT l.id AS loan_id, r.name, l.loan_date, l.return_date
FROM loans l
JOIN readers r ON l.reader_id = r.id;

-- 2. Все книги, которые брал Иван Иванов
SELECT DISTINCT b.title, b.author
FROM loan_items li
JOIN books b ON li.book_id = b.id
JOIN loans l ON li.loan_id = l.id
JOIN readers r ON l.reader_id = r.id
WHERE r.name = 'Иван Иванов';

-- 3. Подсчитать количество выдач по каждому читателю
SELECT r.name, COUNT(l.id) AS total_loans
FROM readers r
LEFT JOIN loans l ON r.id = l.reader_id
GROUP BY r.name;

-- 4. Найти книги определенного автора, которые хоть раз выдавались
SELECT DISTINCT b.title
FROM books b
JOIN loan_items li ON b.id = li.book_id
WHERE b.author = 'Михаил Булгаков';

-- 5. Вывести общее количество дней выдачи для каждого займа
SELECT l.id AS loan_id, SUM(li.loan_period) AS total_loan_days
FROM loans l
JOIN loan_items li ON l.id = li.loan_id
GROUP BY l.id;

-- 6. Топ-2 читателей по количеству взятых книг
SELECT r.name, COUNT(li.book_id) AS total_books_borrowed
FROM readers r
JOIN loans l ON r.id = l.reader_id
JOIN loan_items li ON l.id = li.loan_id
GROUP BY r.name
ORDER BY total_books_borrowed DESC
LIMIT 2;

-- 7. Средний период выдачи книг в каждом городе
SELECT r.city, AVG(li.loan_period) AS avg_loan_period
FROM readers r
JOIN loans l ON r.id = l.reader_id
JOIN loan_items li ON l.id = li.loan_id
GROUP BY r.city;

-- 8. Книги, которые никогда не выдавались
SELECT b.title, b.author
FROM books b
LEFT JOIN loan_items li ON b.id = li.book_id
WHERE li.book_id IS NULL;

-- 9. Читатели, которые брали книги более 1 раза
SELECT r.name, COUNT(l.id) AS loans_count
FROM readers r
JOIN loans l ON r.id = l.reader_id
GROUP BY r.name
HAVING COUNT(l.id) > 1;

-- 10. Количество выдач по каждой книге
SELECT b.title, b.author, COUNT(li.loan_id) AS times_borrowed
FROM books b
LEFT JOIN loan_items li ON b.id = li.book_id
GROUP BY b.title, b.author
ORDER BY times_borrowed DESC;

-- 11. Книги, которые currently на руках (не возвращены)
SELECT b.title, r.name, l.loan_date
FROM books b
JOIN loan_items li ON b.id = li.book_id
JOIN loans l ON li.loan_id = l.id
JOIN readers r ON l.reader_id = r.id
WHERE l.return_date IS NULL;

-- 12. Самые популярные категории книг
SELECT b.category, COUNT(li.loan_id) AS popularity
FROM books b
JOIN loan_items li ON b.id = li.book_id
GROUP BY b.category
ORDER BY popularity DESC;
