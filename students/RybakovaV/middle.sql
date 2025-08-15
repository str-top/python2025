CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50),
    email VARCHAR(55),
    registration_date DATE NOT NULL
);
DESCRIBE users;

INSERT INTO users (user_name, email, registration_date) 
VALUES
('Саша Петров', 'ivan@example.com', '2023-01-15'),
('Мария Иванова', 'maria@example.com', '2023-02-20'),
('Алексей Кукушкин', 'alex@example.com', '2023-03-10');

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL,
    description TEXT
);

INSERT INTO categories (category_name, description) 
VALUES
('Электроника', 'Техника и гаджеты'),
('Одежда', 'Мужская и женская одежда'),
('Книги', 'Художественная и научная литература');

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO products (product_name, category_id, price) 
VALUES
('Смартфон X', 1, 599.99),
('Ноутбук Pro', 1, 1299.99),
('Футболка', 2, 19.99),
('Джинсы', 2, 49.99),
('Роман "Война и мир"', 3, 12.99),
('Учебник по SQL', 3, 29.99);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO orders (user_id, order_date, status) VALUES
(1, '2023-05-01 10:30:00', 'completed'),
(2, '2023-05-02 14:45:00', 'processing'),
(1, '2023-05-03 09:15:00', 'completed'),
(3, '2023-05-04 16:20:00', 'shipped');

CREATE TABLE order_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price_at_order DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items (order_id, product_id, quantity, price_at_order) VALUES
(1, 1, 1, 599.99),
(1, 3, 2, 19.99),
(2, 2, 1, 1299.99),
(3, 4, 1, 49.99),
(3, 5, 3, 12.99),
(4, 6, 1, 29.99),
(4, 1, 1, 599.99);

SELECT o.order_id, u.user_name, o.order_date, SUM(oi.quantity * oi.price_at_order) AS total_amount
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, u.user_name, o.order_date
ORDER BY o.order_date;

SELECT p.product_id, p.product_name, c.category_name, p.price
FROM products p
JOIN categories c ON p.category_id = c.category_id
ORDER BY c.category_name, p.product_name;

SELECT c.category_name, COUNT(p.product_id) AS product_count
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_name
ORDER BY product_count DESC;

UPDATE products
SET price = 549.99
WHERE product_id = 1;

DELETE FROM orders
WHERE order_id = 2;

ALTER TABLE users
ADD COLUMN status VARCHAR(20) DEFAULT 'active';

UPDATE users
SET status = 'premium'
WHERE user_id = (
    SELECT user_id
    FROM (
        SELECT 
            o.user_id,
            SUM(oi.quantity * oi.price_at_order) AS total_amount
        FROM 
            orders o
        JOIN 
            order_items oi ON o.order_id = oi.order_id
        GROUP BY 
            o.user_id
        ORDER BY 
            total_amount DESC
        LIMIT 1
    ) AS max_order
);
