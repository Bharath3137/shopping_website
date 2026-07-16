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