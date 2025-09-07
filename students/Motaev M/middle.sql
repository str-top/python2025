CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO users (name) VALUES
('Иван Иванов'),
('Мария Петрова'),
('Алексей Смирнов');

INSERT INTO categories (name) VALUES
('Электроника'),
('Книги'),
('Одежда');

INSERT INTO products (name, category_id, price) VALUES
('Смартфон', 1, 20000.00),
('Ноутбук', 1, 50000.00),
('Роман "Война и мир"', 2, 800.00),
('Футболка', 3, 1500.00),
('Джинсы', 3, 3000.00);

INSERT INTO orders (user_id, order_date) VALUES
(1, '2025-09-01'),
(2, '2025-09-02'),
(3, '2025-09-03');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 3, 2),
(2, 2, 1),
(2, 4, 3),
(3, 5, 2);

SELECT
    o.id AS order_id,
    u.name AS user_name,
    o.order_date,
    SUM(p.price * oi.quantity) AS total_amount
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON oi.product_id = p.id
GROUP BY o.id, u.name, o.order_date
ORDER BY o.id;

SELECT
    p.name AS product_name,
    c.name AS category_name
FROM products p
JOIN categories c ON p.category_id = c.id
ORDER BY p.name;

SELECT
    c.name AS category_name,
    COUNT(p.id) AS product_count
FROM categories c
LEFT JOIN products p ON p.category_id = c.id
GROUP BY c.id, c.name
ORDER BY c.name;

UPDATE products
SET price = 22000.00
WHERE name = 'Смартфон';

DELETE FROM order_items WHERE order_id = 2;
DELETE FROM orders WHERE id = 2;

ALTER TABLE users
ADD COLUMN status VARCHAR(20) DEFAULT 'active';

UPDATE users
SET status = 'vip'
WHERE id = (
    SELECT user_id FROM orders o
    JOIN (
        SELECT order_id, SUM(p.price * oi.quantity) AS total_amount
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        GROUP BY order_id
        ORDER BY total_amount DESC
        LIMIT 1
    ) AS max_order ON o.id = max_order.order_id
);
