CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    year INT,
    genre VARCHAR(50),
    is_available BOOLEAN DEFAULT TRUE
);

CREATE TABLE readers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE book_loans (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    reader_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (reader_id) REFERENCES readers(id)
);

INSERT INTO books (title, author, year, genre) VALUES
('Война и мир', 'Лев Толстой', 1869, 'Роман'),
('Евгений Онегин', 'Александр Пушкин', 1833, 'Роман в стихах'),
('Герой нашего времени', 'Михаил Лермонтов', 1840, 'Роман');

INSERT INTO readers (name, phone, email) VALUES
('Иван Иванов', '+79161234567', 'ivanov@mail.ru'),
('Мария Петрова', '+79169876543', 'petrova@mail.ru'),
('Алексей Сидоров', '+79165554433', 'sidorov@mail.ru');

INSERT INTO book_loans (book_id, reader_id, loan_date, return_date) VALUES
(1, 1, '2024-01-15', '2024-01-29'),
(3, 2, '2024-01-20', NULL),
(2, 3, '2024-01-25', NULL);

SELECT * FROM books;

SELECT * FROM readers;

SELECT * FROM books WHERE is_available = TRUE;

SELECT * FROM books WHERE author = 'Лев Толстой';

SELECT r.name, b.title, b.author, bl.loan_date
FROM book_loans bl
JOIN readers r ON bl.reader_id = r.id
JOIN books b ON bl.book_id = b.id
WHERE bl.return_date IS NULL;

-- Выдаем книгу с id=2 читателю с id=1
INSERT INTO book_loans (book_id, reader_id, loan_date) 
VALUES (2, 1, CURDATE());

-- Помечаем книгу как недоступную
UPDATE books SET is_available = FALSE WHERE id = 2;

-- Отмечаем дату возврата
UPDATE book_loans 
SET return_date = CURDATE() 
WHERE book_id = 1 AND reader_id = 1 AND return_date IS NULL;

-- Помечаем книгу как доступную
UPDATE books SET is_available = TRUE WHERE id = 1;
