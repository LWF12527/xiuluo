-- 创建数据库
CREATE DATABASE access_control_system;
USE access_control_system;


-- 用户表 
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(100) NOT NULL, 
    phone VARCHAR(15) UNIQUE
);
-- 门禁设备表 
CREATE TABLE access_devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY, 
    location VARCHAR(255) NOT NULL
);
-- 访问记录表 
CREATE TABLE access_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT NOT NULL, 
    device_id INT NOT NULL, 
    access_time DATETIME DEFAULT CURRENT_TIMESTAMP, 
    access_result ENUM('SUCCESS', 'FAILURE') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (device_id) REFERENCES access_devices(device_id)
);

INSERT INTO users (name, phone) 
VALUES 
('张三', '13800138000'),
('李四', '13800138001'),
('王五', '13800138002');

INSERT INTO access_devices (location) 
VALUES 
('一号大门'), 
('二号大门'), 
('停车场入口');

INSERT INTO access_logs (user_id, device_id, access_result) 
VALUES 
(1, 1, 'SUCCESS'), 
(2, 2, 'FAILURE'), 
(3, 3, 'SUCCESS');


-- 为 access_logs 表中的 user_id 和 device_id 创建索引
CREATE INDEX idx_user_id ON access_logs (user_id);
CREATE INDEX idx_device_id ON access_logs (device_id);

-- 创建访问记录详细信息视图
CREATE VIEW access_logs_view AS
SELECT 
    al.log_id, 
    u.name AS user_name, 
    ad.location AS device_location, 
    al.access_time, 
    al.access_result
FROM 
    access_logs al
JOIN 
    users u ON al.user_id = u.user_id
JOIN 
access_devices ad ON al.device_id = ad.device_id;


-- 创建存储过程：查询用户访问历史
DELIMITER //
CREATE PROCEDURE get_user_access_history(IN input_user_id INT)
BEGIN
    SELECT 
        al.log_id, 
        u.name AS user_name, 
        ad.location AS device_location, 
        al.access_time, 
        al.access_result
    FROM 
        access_logs al
    JOIN 
        users u ON al.user_id = u.user_id
    JOIN 
        access_devices ad ON al.device_id = ad.device_id
    WHERE 
        al.user_id = input_user_id;
END;
//
DELIMITER ;
