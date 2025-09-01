
CREATE DATABASE BUS_mag;
use  BUS_mag;
-- 创建车辆表
CREATE TABLE vehicle (
                         id INT PRIMARY KEY AUTO_INCREMENT,
                         departure VARCHAR(50) NOT NULL,
                         destination VARCHAR(50) NOT NULL,
                         departure_time DATETIME NOT NULL,
                         arrival_time DATETIME NOT NULL,
                         vehicle_type VARCHAR(50) NOT NULL,
                         ticket_price DECIMAL(8, 2) NOT NULL,
                         max_capacity INT NOT NULL,
                         ticket_status INT DEFAULT 0
);

-- 创建用户表
CREATE TABLE user (
                      id INT PRIMARY KEY AUTO_INCREMENT,
                      username VARCHAR(50) NOT NULL,
                      password VARCHAR(50) NOT NULL,
                      email VARCHAR(50) NOT NULL,
                      phone VARCHAR(20) NOT NULL
);

-- 创建车票表
CREATE TABLE ticket (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        user_id INT NOT NULL,
                        vehicle_id INT NOT NULL,
                        purchase_time DATETIME NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES user(id),
                        FOREIGN KEY (vehicle_id) REFERENCES vehicle(id)
);

-- 创建管理员表
CREATE TABLE admin (
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       username VARCHAR(50) NOT NULL,
                       password VARCHAR(50) NOT NULL
);


-- 向车辆表(vehicle)插入数据：

INSERT INTO vehicle (departure, destination, departure_time, arrival_time, vehicle_type, ticket_price, max_capacity, ticket_status)
VALUES
    ('City A', 'City B', '2024-06-05 08:00:00', '2024-06-05 12:00:00', 'Bus', 10.50, 50, 0),
    ('City B', 'City C', '2024-06-05 13:00:00', '2024-06-05 16:00:00', 'Train', 25.00, 100, 0),
    ('City C', 'City D', '2024-06-06 09:00:00', '2024-06-06 14:00:00', 'Bus', 15.75, 60, 0),
    ('City D', 'City E', '2024-06-06 15:30:00', '2024-06-06 18:30:00', 'Train', 30.00, 80, 0),
    ('City E', 'City F', '2024-06-07 11:00:00', '2024-06-07 15:00:00', 'Bus', 12.50, 70, 0);


-- 向用户表(user)插入数据：

INSERT INTO user (username, password, email, phone)
VALUES
    ('user1', '123456', 'user1@example.com', '1234567890'),
    ('user2', '123456', 'user2@example.com', '9876543210'),
    ('user3', '123456', 'user3@example.com', '5555555555'),
    ('user4', '123456', 'user4@example.com', '1111111111'),
    ('user5', '123456', 'user5@example.com', '9999999999');

-- 向车票表(ticket)插入数据：
INSERT INTO ticket (user_id, vehicle_id, purchase_time)
VALUES
    (1, 1, '2024-06-05 07:30:00'),
    (2, 3, '2024-06-06 08:45:00'),
    (3, 2, '2024-06-06 10:15:00'),
    (4, 4, '2024-06-07 14:30:00'),
    (5, 5, '2024-06-07 09:00:00');

-- 向管理员表(admin)插入数据：
INSERT INTO admin (username, password)
VALUES
    ('admin1', '123456'),
    ('admin2', '123456'),
    ('admin3', '123456');

