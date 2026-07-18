use shopping_db;
CREATE TABLE products(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
ALTER TABLE products
ADD stock INT NOT NULL;
ALTER TABLE products
ADD category VARCHAR(100) NOT NULL;

INSERT INTO products(name, price, stock, category)
VALUES('Laptop', 90000, 10, 'Electronics');
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('Admin','Customer') NOT NULL
);

CREATE TABLE cart(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,

    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
CREATE TABLE orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE order_items(
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
select * from products;
use shopping_db;
select * from products;
INSERT INTO products(name,price,stock,category)
VALUES
('Mouse',500,100,'Electronics'),
('Keyboard',1500,50,'Electronics');

use shopping_db;
desc products;
select * from users;
INSERT INTO users(username, email, password, role)
VALUES(
'admin',
'admin@gmail.com',
'1234',
'Admin'
);
use shopping_db;
DELETE FROM cart
WHERE user_id = 1;
DELETE FROM order_items
WHERE order_id IN (
    SELECT id
    FROM orders
    WHERE user_id = 1
);
DELETE FROM orders
WHERE user_id = 1;
DELETE FROM users
WHERE id = 1;
UPDATE users
SET role = 'Admin'
WHERE email = 'admin@123.com';
