SELECT 
    o.order_id,
    u.username,
    o.order_date,
    SUM(oi.price_at_order * oi.quantity) AS total_amount
FROM 
    orders o
JOIN 
    users u ON o.user_id = u.user_id
JOIN 
    order_items oi ON o.order_id = oi.order_id
GROUP BY 
    o.order_id, u.username, o.order_date
ORDER BY 
    o.order_date DESC;

SELECT 
    p.product_id,
    p.name AS product_name,
    p.price,
    c.name AS category_name
FROM 
    products p
LEFT JOIN 
    categories c ON p.category_id = c.category_id
ORDER BY 
    c.name, p.name;

SELECT 
    c.name AS category_name,
    COUNT(p.product_id) AS product_count
FROM 
    categories c
LEFT JOIN 
    products p ON c.category_id = p.category_id
GROUP BY 
    c.name
ORDER BY 
    product_count DESC;


UPDATE products
SET price = 84999.99
WHERE product_id = 1;


DELETE FROM orders
WHERE order_id = 5;

ALTER TABLE users
ADD COLUMN status VARCHAR(20) DEFAULT 'активный';


UPDATE users
SET status = 'VIP'
WHERE user_id = (
    SELECT o.user_id
    FROM orders o
    JOIN (
        SELECT 
            order_id, 
            SUM(price_at_order * quantity) AS order_total
        FROM order_items
        GROUP BY order_id
    ) ot ON o.order_id = ot.order_id
    ORDER BY ot.order_total DESC
    LIMIT 1
);
