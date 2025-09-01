-- 创建数据库
CREATE DATABASE IF NOT EXISTS WATER_SYS;
USE WATER_SYS;

-- 创建业务员表
CREATE TABLE salespersons (
    salesperson_id INT AUTO_INCREMENT PRIMARY KEY,  -- 业务员ID
    salesperson_name VARCHAR(100) NOT NULL          -- 业务员姓名
);

-- 创建客户信息表
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,  -- 客户ID
    customer_name VARCHAR(100) NOT NULL,         -- 客户名称
    customer_address VARCHAR(200),               -- 客户地址
    balance DECIMAL(10, 2) DEFAULT 0.00          -- 客户结余，默认0.00
);

-- 创建用水类别表
CREATE TABLE water_types (
    water_type_id INT AUTO_INCREMENT PRIMARY KEY, -- 用水类别ID
    water_type_name VARCHAR(100) NOT NULL          -- 用水类别名称
);

-- 创建客户用水信息表
CREATE TABLE water_usage (
    customer_id INT,                              -- 客户ID
    month VARCHAR(20) NOT NULL,                     -- 月份，格式：'xxxx年xx月'
    water_type_id INT,                            -- 用水类别ID
    water_amount DECIMAL(10, 2) NOT NULL,         -- 用水量
    PRIMARY KEY (customer_id, month, water_type_id), -- 复合主键，确保每个客户每月每种用水类别的记录唯一
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), -- 外键，指向客户信息表
    FOREIGN KEY (water_type_id) REFERENCES water_types(water_type_id) -- 外键，指向用水类别表
);

-- 创建客户费用管理表
CREATE TABLE customer_fees (
    customer_id INT,                              -- 客户ID
    month VARCHAR(20) NOT NULL,                     -- 月份，格式：'xxxx年xx月'
    fee DECIMAL(10, 2) NOT NULL,                   -- 水费金额
    fee_status ENUM('未收', '已收') DEFAULT '未收', -- 收费状态，默认未收
    PRIMARY KEY (customer_id, month),              -- 复合主键
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- 外键，指向客户信息表
);

-- 创建收费登记表
CREATE TABLE payment_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,    -- 收费记录ID
    customer_id INT,                              -- 客户ID
    month VARCHAR(20) NOT NULL,                     -- 月份，格式：'xxxx年xx月'
    due_fee DECIMAL(10, 2) NOT NULL,               -- 应收费用
    received_fee DECIMAL(10, 2) NOT NULL,          -- 实收费用
    salesperson_id INT,                           -- 业务员ID
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), -- 外键，指向客户信息表
    FOREIGN KEY (salesperson_id) REFERENCES salespersons(salesperson_id) -- 外键，指向业务员表
);

-- 插入业务员数据
INSERT INTO salespersons (salesperson_name)
VALUES
('张丽'),
('李娜'),
('王俊'),
('赵刚'),
('钱峰');

-- 插入客户数据
INSERT INTO customers (customer_name, customer_address, balance)
VALUES
('张三', '北京市朝阳区', 500.00),
('李四', '上海市浦东新区', 300.50),
('王五', '广州市天河区', 150.00),
('赵六', '深圳市南山区', 800.75),
('钱七', '天津市和平区', 200.00),
('孙八', '重庆市江北区', 600.20),
('周九', '成都市锦江区', 450.00),
('吴十', '武汉市洪山区', 350.75),
('郑十一', '南京市鼓楼区', 700.60),
('冯十二', '西安市雁塔区', 1000.00);

-- 插入用水类别数据
INSERT INTO water_types (water_type_name)
VALUES
('生活用水'),
('工业用水'),
('农业用水'),
('商业用水'),
('公共设施用水'),
('高层住宅用水'),
('低层住宅用水'),
('建筑工地用水'),
('污水处理用水'),
('绿化用水');

-- 插入客户用水数据
INSERT INTO water_usage (customer_id, month, water_type_id, water_amount)
VALUES
(1, '2024年01月', 1, 15.0),
(1, '2024年02月', 2, 100.0),
(2, '2024年01月', 1, 12.5),
(2, '2024年02月', 3, 50.0),
(3, '2024年01月', 1, 10.0),
(3, '2024年02月', 4, 25.0),
(4, '2024年01月', 1, 30.0),
(4, '2024年02月', 5, 40.0),
(5, '2024年01月', 2, 150.0),
(5, '2024年02月', 6, 200.0);

-- 插入客户费用数据
INSERT INTO customer_fees (customer_id, month, fee, fee_status)
VALUES
(1, '2024年01月', 50.00, '未收'),
(1, '2024年02月', 150.00, '未收'),
(2, '2024年01月', 40.00, '未收'),
(2, '2024年02月', 120.00, '未收'),
(3, '2024年01月', 30.00, '未收'),
(3, '2024年02月', 80.00, '未收'),
(4, '2024年01月', 70.00, '未收'),
(4, '2024年02月', 160.00, '未收'),
(5, '2024年01月', 180.00, '未收'),
(5, '2024年02月', 220.00, '未收');

-- 插入收费记录数据
INSERT INTO payment_records (customer_id, month, due_fee, received_fee, salesperson_id)
VALUES
(1, '2024年01月', 50.00, 50.00, 1),
(1, '2024年02月', 150.00, 150.00, 2),
(2, '2024年01月', 40.00, 40.00, 1),
(2, '2024年02月', 120.00, 120.00, 2),
(3, '2024年01月', 30.00, 30.00, 3),
(3, '2024年02月', 80.00, 80.00, 3),
(4, '2024年01月', 70.00, 70.00, 4),
(4, '2024年02月', 160.00, 160.00, 4),
(5, '2024年01月', 180.00, 180.00, 5),
(5, '2024年02月', 220.00, 220.00, 5);
