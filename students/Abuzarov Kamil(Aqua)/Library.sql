-- Добавим CHECK ограничения для валидации данных
ALTER TABLE products ADD CONSTRAINT positive_price CHECK (price > 0);
ALTER TABLE order_items ADD CONSTRAINT positive_quantity CHECK (quantity > 0);

-- Добавим индекс для часто используемых полей
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_products_price ON products(price);

-- Добавим NOT NULL ограничения
ALTER TABLE customers ALTER COLUMN name SET NOT NULL;
ALTER TABLE products ALTER COLUMN product_name SET NOT NULL;
ALTER TABLE orders ALTER COLUMN order_date SET NOT NULL;



-- 11. Ежемесячная статистика продаж
SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    COUNT(DISTINCT o.id) AS orders_count,
    SUM(p.price * oi.quantity) AS total_revenue
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY year, month
ORDER BY year, month;

-- 12. Покупатели с самой дорогой покупкой
SELECT 
    c.name,
    MAX(p.price * oi.quantity) AS max_purchase_amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY c.name
ORDER BY max_purchase_amount DESC;

-- 13. Товары в корзине (количество в заказах)
SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_ordered,
    COUNT(DISTINCT o.id) AS orders_count
FROM products p
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
GROUP BY p.product_name
ORDER BY total_ordered DESC;

-- 14. Дата последнего заказа для каждого покупателя
SELECT 
    c.name,
    MAX(o.order_date) AS last_order_date
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.name;

-- 15. Процент от общей выручки по каждому товару
WITH product_revenue AS (
    SELECT 
        p.product_name,
        SUM(p.price * oi.quantity) AS revenue
    FROM products p
    JOIN order_items oi ON p.id = oi.product_id
    GROUP BY p.product_name
),
total_revenue AS (
    SELECT SUM(revenue) AS total FROM product_revenue
)
SELECT 
    pr.product_name,
    pr.revenue,
    ROUND((pr.revenue / tr.total) * 100, 2) AS percentage
FROM product_revenue pr, total_revenue tr
ORDER BY pr.revenue DESC;
