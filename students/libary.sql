CREATE TABLE authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    author_id INT,
    publish_year YEAR,
    genre VARCHAR(50),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE readers (
    reader_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    contact_info VARCHAR(255)
);

CREATE TABLE borrowings (
    borrowing_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    reader_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (reader_id) REFERENCES readers(reader_id)
);

INSERT INTO authors (first_name, last_name, birth_date) VALUES
('Лев', 'Толстой', '1828-09-09'),
('Федор', 'Достоевский', '1821-11-11');

INSERT INTO books (title, author_id, publish_year, genre) VALUES
('Война и мир', 1, 1869, 'Исторический роман'),
('Преступление и наказание', 2, 1866, 'Психологический роман');

INSERT INTO readers (first_name, last_name, birth_date, contact_info) VALUES
('Иван', 'Иванов', '1990-05-15', 'ivanov@example.com'),
('Петр', 'Петров', '1985-08-20', 'petrov@example.com');

INSERT INTO borrowings (book_id, reader_id, borrow_date, return_date) VALUES
(1, 1, '2023-10-01', NULL),
(2, 2, '2023-09-15', '2023-10-05');
