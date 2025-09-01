drop database if exists bookstore;
CREATE DATABASE if not exists bookstore;
USE bookstore;
CREATE TABLE books (
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       title VARCHAR(255) NOT NULL,
                       author VARCHAR(255) NOT NULL,
                       price DECIMAL(10, 2) NOT NULL,
                       stock INT NOT NULL
);
CREATE TABLE suppliers (
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           name VARCHAR(255) NOT NULL,
                           contact VARCHAR(255) NOT NULL
);
CREATE TABLE purchases (
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           book_id INT NOT NULL,
                           supplier_id INT NOT NULL,
                           quantity INT NOT NULL,
                           purchase_date DATE NOT NULL,
                           FOREIGN KEY (book_id) REFERENCES books(id),
                           FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);
CREATE TABLE returns (
                         id INT AUTO_INCREMENT PRIMARY KEY,
                         book_id INT NOT NULL,
                         quantity INT NOT NULL,
                         return_date DATE NOT NULL,
                         FOREIGN KEY (book_id) REFERENCES books(id)
);
CREATE TABLE sales (
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       book_id INT NOT NULL,
                       quantity INT NOT NULL,
                       sale_date DATE NOT NULL,
                       FOREIGN KEY (book_id) REFERENCES books(id)
);


-- 向books表插入10条数据：
INSERT INTO books (title, author, price, stock)
VALUES
('Book 1', 'Author 1', 10.99, 50),
('Book 2', 'Author 2', 15.99, 30),
('Book 3', 'Author 3', 12.99, 20),
('Book 4', 'Author 4', 9.99, 40),
('Book 5', 'Author 5', 14.99, 25),
('Book 6', 'Author 6', 11.99, 35),
('Book 7', 'Author 7', 13.99, 45),
('Book 8', 'Author 8', 16.99, 15),
('Book 9', 'Author 9', 8.99, 55),
('Book 10', 'Author 10', 17.99, 10);

-- 向suppliers表插入10条数据：
INSERT INTO suppliers (name, contact)
VALUES
('Supplier 1', 'Contact 1'),
('Supplier 2', 'Contact 2'),
('Supplier 3', 'Contact 3'),
('Supplier 4', 'Contact 4'),
('Supplier 5', 'Contact 5'),
('Supplier 6', 'Contact 6'),
('Supplier 7', 'Contact 7'),
('Supplier 8', 'Contact 8'),
('Supplier 9', 'Contact 9'),
('Supplier 10', 'Contact 10');

-- 向purchases表插入10条数据：
INSERT INTO purchases (book_id, supplier_id, quantity, purchase_date)
VALUES
(1, 1, 5, '2023-06-01'),
(2, 2, 3, '2023-06-02'),
(3, 3, 2, '2023-06-03'),
(4, 4, 4, '2023-06-04'),
(5, 5, 6, '2023-06-05'),
(6, 6, 1, '2023-06-06'),
(7, 7, 8, '2023-06-07'),
(8, 8, 9, '2023-06-08'),
(9, 9, 7, '2023-06-09'),
(10, 10, 10, '2023-06-10');

-- 向returns表插入10条数据：
INSERT INTO returns (book_id, quantity, return_date)
VALUES
(1, 2, '2023-06-11'),
(2, 1, '2023-06-12'),
(3, 3, '2023-06-13'),
(4, 4, '2023-06-14'),
(5, 2, '2023-06-15'),
(6, 5, '2023-06-16'),
(7, 1, '2023-06-17'),
(8, 3, '2023-06-18'),
(9, 2, '2023-06-19'),
(10, 4, '2023-06-20');

-- 向sales表插入10条数据：
INSERT INTO sales (book_id, quantity, sale_date)
VALUES
(1, 3, '2023-06-01'),
(2, 2, '2023-06-02'),
(3, 4, '2023-06-03'),
(4, 5, '2023-06-04'),
(5, 1, '2023-06-05'),
(6, 2, '2023-06-06'),
(7, 3, '2023-06-07'),
(8, 4, '2023-06-08'),
(9, 2, '2023-06-09'),
(10, 1, '2023-06-10');



