CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO users (name, email) VALUES
('Иван Иванов', 'ivan@mail.com'),
('Петр Петров', 'petr@mail.com'),
('Мария Сидорова', 'maria@mail.com');

INSERT INTO categories (name) VALUES
('Электроника'),
('Одежда'),
('Книги');

INSERT INTO products (name, price, category_id) VALUES
('Ноутбук', 50000.00, 1),
('Смартфон', 25000.00, 1),
('Футболка', 1500.00, 2),
('Джинсы', 3000.00, 2),
('Роман', 500.00, 3),
('Учебник', 800.00, 3);

INSERT INTO orders (user_id, order_date) VALUES
(1, '2024-01-15'),
(2, '2024-01-16'),
(3, '2024-01-17');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 3, 2),
(2, 2, 1),
(2, 4, 1),
(2, 6, 3),
(3, 5, 5),
(3, 3, 1);

SELECT 
    o.id as order_id,
    u.name as user_name,
    o.order_date,
    SUM(p.price * oi.quantity) as total_amount
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY o.id, u.name, o.order_date
ORDER BY o.id;


SELECT 
    p.name as product_name,
    c.name as category_name,
    p.price
FROM products p
JOIN categories c ON p.category_id = c.id
ORDER BY c.name, p.name;


SELECT 
    c.name as category_name,
    COUNT(p.id) as product_count
FROM categories c
LEFT JOIN products p ON c.id = p.category_id
GROUP BY c.name
ORDER BY product_count DESC;


UPDATE products SET price = 27000.00 WHERE id = 2;

DELETE FROM order_items WHERE order_id = 2;
DELETE FROM orders WHERE id = 2;

ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';

UPDATE users 
SET status = 'vip' 
WHERE id = (
    SELECT user_id FROM (
        SELECT o.user_id, SUM(p.price * oi.quantity) as total_spent
        FROM orders o
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
        GROUP BY o.user_id
        ORDER BY total_spent DESC
        LIMIT 1
    ) as user_totals
);
