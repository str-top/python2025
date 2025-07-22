DROP TABLE if EXISTS products;
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT not null unique,
quantity INTEGER not null
 );

INSERT INTO products(name, quantity) VALUES ('Dasha', 10);
INSERT INTO products(name, quantity) VALUES ('Pasha', 10);

SELECT * FROM products;
