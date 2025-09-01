drop database if EXISTS shoping;
create database if not EXISTS shoping;
use shoping;

-- 创建用户表
CREATE TABLE users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  gender ENUM('Male', 'Female') NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address VARCHAR(100) NOT NULL
);


-- 创建店铺表：

CREATE TABLE shops (
  shop_id INT PRIMARY KEY,
  shop_name VARCHAR(100) NOT NULL,
  address VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL
);


-- 创建商品表：

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100) NOT NULL,
  shop_id INT,
  stock INT default 0,
  price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (shop_id) REFERENCES shops(shop_id)
);


-- 创建订单表：

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  user_id INT,
  product_id INT,
  quantity INT NOT NULL,
  order_date DATE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- 向用户表插入数据
INSERT INTO users (user_id, username, password, gender, phone, address) VALUES
(1, 'user1', 'password1', 'Male', '1234567890', 'Address 1'),
(2, 'user2', 'password2', 'Female', '0987654321', 'Address 2'),
(3, 'user3', 'password3', 'Male', '1111111111', 'Address 3'),
(4, 'user4', 'password4', 'Female', '2222222222', 'Address 4'),
(5, 'user5', 'password5', 'Male', '3333333333', 'Address 5'),
(6, 'user6', 'password6', 'Female', '4444444444', 'Address 6'),
(7, 'user7', 'password7', 'Male', '5555555555', 'Address 7'),
(8, 'user8', 'password8', 'Female', '6666666666', 'Address 8'),
(9, 'user9', 'password9', 'Male', '7777777777', 'Address 9'),
(10, 'user10', 'password10', 'Female', '8888888888', 'Address 10');


-- 向店铺表插入数据
INSERT INTO shops (shop_id, shop_name, address, phone) VALUES
(1, 'Shop 1', 'Shop Address 1', 'Shop Phone 1'),
(2, 'Shop 2', 'Shop Address 2', 'Shop Phone 2'),
(3, 'Shop 3', 'Shop Address 3', 'Shop Phone 3'),
(4, 'Shop 4', 'Shop Address 4', 'Shop Phone 4'),
(5, 'Shop 5', 'Shop Address 5', 'Shop Phone 5'),
(6, 'Shop 6', 'Shop Address 6', 'Shop Phone 6'),
(7, 'Shop 7', 'Shop Address 7', 'Shop Phone 7'),
(8, 'Shop 8', 'Shop Address 8', 'Shop Phone 8'),
(9, 'Shop 9', 'Shop Address 9', 'Shop Phone 9'),
(10, 'Shop 10', 'Shop Address 10', 'Shop Phone 10');


-- 向商品表插入数据
INSERT INTO products (product_id, product_name, shop_id, price) VALUES
(1, 'Product 1', 1, 10.00),
(2, 'Product 2', 2, 20.00),
(3, 'Product 3', 3, 30.00),
(4, 'Product 4', 4, 40.00),
(5, 'Product 5', 5, 50.00),
(6, 'Product 6', 6, 60.00),
(7, 'Product 7', 7, 70.00),
(8, 'Product 8', 8, 80.00),
(9, 'Product 9', 9, 90.00),
(10, 'Product 10', 10, 100.00);


-- 向订单表插入数据
INSERT INTO orders (order_id, user_id, product_id, quantity, order_date) VALUES
(1, 1, 1, 2, '2023-06-01'),
(2, 2, 2, 1, '2023-06-02'),
(3, 3, 3, 3, '2023-06-03'),
(4, 4, 4, 2, '2023-06-04'),
(5, 5, 5, 1, '2023-06-05'),
(6, 6, 6, 3, '2023-06-06'),
(7, 7, 7, 2, '2023-06-07'),
(8, 8, 8, 1, '2023-06-08'),
(9, 9, 9, 3, '2023-06-09'),
(10, 10, 10, 2, '2023-06-10');

ALTER TABLE products
MODIFY COLUMN stock INT UNSIGNED NOT NULL DEFAULT 0;

ALTER TABLE users
MODIFY COLUMN password VARCHAR(12);

CREATE VIEW V_commodity AS
SELECT *
FROM products;

-- 添加用户adm
CREATE USER 'adm'@'localhost' IDENTIFIED BY '123';

-- 添加用户user001
CREATE USER 'user001'@'localhost' IDENTIFIED BY '333';

GRANT ALL PRIVILEGES ON shping.* TO 'adm'@'localhost';

GRANT SELECT ON shoping.products TO 'user001'@'localhost';


SELECT * FROM orders;

SELECT gender, COUNT(*) AS count FROM users GROUP BY gender;

SELECT u.username, p.product_name, o.quantity, u.address 
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN products p ON o.product_id = p.product_id;

SELECT order_id, SUM(quantity*price) AS total_value 
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY order_id;

CREATE TRIGGER update_stock AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE products
  SET stock = stock - NEW.quantity
  WHERE id = NEW.product_id;
END;

INSERT INTO orders (order_id, user_id, product_id, quantity, order_date)
VALUES (100, 3, 3, 2, '2023-06-18');
select  *  from  products  where  product_id=4

UPDATE products
SET stock = stock - 5
WHERE product_id = 4;



