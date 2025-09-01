drop database if exists youju;
create database if not exists youju;
use youju;
-- 创建报刊表
CREATE TABLE IF NOT EXISTS newspapers (
                                          id INT AUTO_INCREMENT PRIMARY KEY,
                                          name VARCHAR(255),
                                          price FLOAT
    );

-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     name VARCHAR(255),
                                     address VARCHAR(255)
    );

-- 创建订阅表
CREATE TABLE IF NOT EXISTS subscriptions (
                                             id INT AUTO_INCREMENT PRIMARY KEY,
                                             user_id INT,
                                             newspaper_id INT,
                                             date DATE,
                                             FOREIGN KEY (user_id) REFERENCES users(id),
                                             FOREIGN KEY (newspaper_id) REFERENCES newspapers(id)
    );

-- 创建入库记录表
CREATE TABLE IF NOT EXISTS stock (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     newspaper_id INT,
                                     quantity INT,
                                     FOREIGN KEY (newspaper_id) REFERENCES newspapers(id)
    );

-- 创建发放记录表
CREATE TABLE IF NOT EXISTS distribution (
                                            id INT AUTO_INCREMENT PRIMARY KEY,
                                            user_id INT,
                                            newspaper_id INT,
                                            quantity INT,
                                            FOREIGN KEY (user_id) REFERENCES users(id),
                                            FOREIGN KEY (newspaper_id) REFERENCES newspapers(id)
    );



-- 报刊表插入数据
INSERT INTO newspapers (name, price) VALUES
                                         ('报刊1', 10.99),
                                         ('报刊2', 9.99),
                                         ('报刊3', 8.99),
                                         ('报刊4', 7.99),
                                         ('报刊5', 6.99);

-- 用户表插入数据
INSERT INTO users (name, address) VALUES
                                      ('用户1', '地址1'),
                                      ('用户2', '地址2'),
                                      ('用户3', '地址3'),
                                      ('用户4', '地址4'),
                                      ('用户5', '地址5');

-- 订阅表插入数据
INSERT INTO subscriptions (user_id, newspaper_id, date) VALUES
                                                            (1, 1, '2023-01-01'),
                                                            (2, 2, '2023-01-02'),
                                                            (3, 3, '2023-01-03'),
                                                            (4, 4, '2023-01-04'),
                                                            (5, 5, '2023-01-05');

-- 入库记录表插入数据
INSERT INTO stock (newspaper_id, quantity) VALUES
                                               (1, 100),
                                               (2, 200),
                                               (3, 300),
                                               (4, 400),
                                               (5, 500);

-- 发放记录表插入数据
INSERT INTO distribution (user_id, newspaper_id, quantity) VALUES
                                                               (1, 1, 10),
                                                               (2, 2, 20),
                                                               (3, 3, 30),
                                                               (4, 4, 40),
                                                               (5, 5, 50);
