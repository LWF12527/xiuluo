-- 创建数据库
CREATE DATABASE cs_management;

-- 选择数据库
USE cs_management;

-- 商品类别表
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- 类别ID，自增长
    category_name VARCHAR(255) NOT NULL  -- 类别名称，不能为空
);

-- 供应商表
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,  -- 供应商ID，自增长
    supplier_name VARCHAR(255) NOT NULL  -- 供应商名称，不能为空
);

-- 商品表
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- 商品ID，自增长
    product_name VARCHAR(255) NOT NULL,  -- 商品名称，不能为空
    category_id INT,  -- 商品类别ID，外键，关联categories表
    supplier_id INT,  -- 供应商ID，外键，关联suppliers表
    image_name VARCHAR(255),  -- 商品图片名称
    description TEXT,  -- 商品描述
    price DECIMAL(10, 2),  -- 商品价格，保留两位小数
    FOREIGN KEY (category_id) REFERENCES categories(category_id),  -- 外键约束：category_id 关联 categories 表
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)  -- 外键约束：supplier_id 关联 suppliers 表
);

-- 用户表
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- 用户ID，自增长
    username VARCHAR(255) NOT NULL,  -- 用户名，不能为空
    password VARCHAR(255) NOT NULL  -- 密码，不能为空
);

-- 地址表
CREATE TABLE addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,  -- 地址ID，自增长
    user_id INT,  -- 用户ID，外键，关联users表
    receiver_name VARCHAR(255),  -- 收件人姓名
    receiver_phone VARCHAR(15),  -- 收件人手机号
    address_details TEXT,  -- 详细地址
    FOREIGN KEY (user_id) REFERENCES users(user_id)  -- 外键约束：user_id 关联 users 表
);

-- 购物车表
CREATE TABLE cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,  -- 购物车ID，自增长
    user_id INT,  -- 用户ID，外键，关联users表
    product_id INT,  -- 商品ID，外键，关联products表
    quantity INT,  -- 商品数量
    FOREIGN KEY (user_id) REFERENCES users(user_id),  -- 外键约束：user_id 关联 users 表
    FOREIGN KEY (product_id) REFERENCES products(product_id)  -- 外键约束：product_id 关联 products 表
);

-- 订单表
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,  -- 订单ID，自增长
    user_id INT,  -- 用户ID，外键，关联users表
    order_number VARCHAR(255),  -- 订单编号
    order_date DATETIME,  -- 订单时间
    order_status VARCHAR(50),  -- 订单状态
    shipping_address_id INT,  -- 收货地址ID，外键，关联addresses表
    FOREIGN KEY (user_id) REFERENCES users(user_id),  -- 外键约束：user_id 关联 users 表
    FOREIGN KEY (shipping_address_id) REFERENCES addresses(address_id)  -- 外键约束：shipping_address_id 关联 addresses 表
);

-- 订单明细表
CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,  -- 订单明细ID，自增长
    order_id INT,  -- 订单ID，外键，关联orders表
    product_id INT,  -- 商品ID，外键，关联products表
    quantity INT,  -- 商品数量
    FOREIGN KEY (order_id) REFERENCES orders(order_id),  -- 外键约束：order_id 关联 orders 表
    FOREIGN KEY (product_id) REFERENCES products(product_id)  -- 外键约束：product_id 关联 products 表
);


INSERT INTO categories (category_name) VALUES
('电子产品'),
('家居用品'),
('服装'),
('食品'),
('化妆品'),
('图书'),
('运动器材'),
('玩具'),
('鞋类'),
('办公用品');

INSERT INTO suppliers (supplier_name) VALUES
('苹果公司'),
('三星电子'),
('索尼公司'),
('华为技术'),
('小米科技'),
('美的集团'),
('京东商城'),
('淘宝网'),
('网易公司'),
('微软公司');

INSERT INTO products (product_name, category_id, supplier_id, image_name, description, price) VALUES
('iPhone 14', 1, 1, 'iphone14.jpg', '苹果最新款智能手机', 6999.99),
('三星 Galaxy S23', 1, 2, 'galaxy_s23.jpg', '三星新款智能手机', 5899.99),
('Sony Headphones', 1, 3, 'sony_headphones.jpg', '索尼降噪耳机', 1299.99),
('华为 Mate 50', 1, 4, 'huawei_mate50.jpg', '华为旗舰智能手机', 7999.99),
('小米 12 Pro', 1, 5, 'xiaomi_12pro.jpg', '小米高性能智能手机', 4999.99),
('智能扫地机器人', 2, 6, 'robot_vacuum.jpg', '高效智能扫地机器人', 1699.99),
('LED 电视', 2, 6, 'led_tv.jpg', '超清LED电视', 2499.99),
('运动手环', 7, 7, 'sports_band.jpg', '健身运动手环', 399.99),
('儿童玩具车', 8, 8, 'toy_car.jpg', '适合儿童的遥控玩具车', 199.99),
('办公椅', 9, 9, 'office_chair.jpg', '舒适办公椅', 899.99);

INSERT INTO users (username, password) VALUES
('john_doe', 'password123'),
('jane_smith', 'mypassword'),
('alex_wang', 'qwerty'),
('lily_zhang', 'password456'),
('tom_liu', '123456'),
('lucy_yang', 'ilovemysql'),
('susan_lee', 'admin123'),
('george_tang', 'abc123'),
('kelly_zhao', 'letmein'),
('michael_liu', 'password789');

INSERT INTO addresses (user_id, receiver_name, receiver_phone, address_details) VALUES
(1, 'John Doe', '13800010001', '北京市朝阳区朝阳路123号'),
(2, 'Jane Smith', '13800010002', '上海市浦东新区浦东路456号'),
(3, 'Alex Wang', '13800010003', '广州市天河区体育东路789号'),
(4, 'Lily Zhang', '13800010004', '深圳市福田区中心街101号'),
(5, 'Tom Liu', '13800010005', '武汉市武昌区长春路202号'),
(6, 'Lucy Yang', '13800010006', '重庆市渝中区大坪街303号'),
(7, 'Susan Lee', '13800010007', '成都市锦江区春熙路404号'),
(8, 'George Tang', '13800010008', '西安市雁塔区大雁塔南路505号'),
(9, 'Kelly Zhao', '13800010009', '南京市鼓楼区中央路606号'),
(10, 'Michael Liu', '13800010010', '天津市和平区南京路707号');

INSERT INTO cart (user_id, product_id, quantity) VALUES
(1, 1, 2),  -- John Doe加入了2个iPhone 14
(1, 3, 1),  -- John Doe加入了1个Sony Headphones
(2, 2, 3),  -- Jane Smith加入了3个三星 Galaxy S23
(2, 4, 1),  -- Jane Smith加入了1个华为 Mate 50
(3, 5, 1),  -- Alex Wang加入了1个小米 12 Pro
(3, 6, 2),  -- Alex Wang加入了2个智能扫地机器人
(4, 7, 1),  -- Lily Zhang加入了1个LED 电视
(5, 8, 1),  -- Tom Liu加入了1个运动手环
(6, 9, 3),  -- Lucy Yang加入了3个儿童玩具车
(7, 10, 1);  -- Susan Lee加入了1个办公椅

INSERT INTO orders (user_id, order_number, order_date, order_status, shipping_address_id) VALUES
(1, 'ORD123456', NOW(), '已完成', 1),
(2, 'ORD123457', NOW(), '已完成', 2),
(3, 'ORD123458', NOW(), '待发货', 3),
(4, 'ORD123459', NOW(), '已取消', 4),
(5, 'ORD123460', NOW(), '待支付', 5),
(6, 'ORD123461', NOW(), '已完成', 6),
(7, 'ORD123462', NOW(), '已完成', 7),
(8, 'ORD123463', NOW(), '待发货', 8),
(9, 'ORD123464', NOW(), '已完成', 9),
(10, 'ORD123465', NOW(), '已取消', 10);

INSERT INTO order_details (order_id, product_id, quantity) VALUES
(1, 1, 2),  -- 订单ORD123456包含2个iPhone 14
(1, 3, 1),  -- 订单ORD123456包含1个Sony Headphones
(2, 2, 3),  -- 订单ORD123457包含3个三星 Galaxy S23
(2, 4, 1),  -- 订单ORD123457包含1个华为 Mate 50
(3, 5, 1),  -- 订单ORD123458包含1个小米 12 Pro
(3, 6, 2),  -- 订单ORD123458包含2个智能扫地机器人
(4, 7, 1),  -- 订单ORD123459包含1个LED 电视
(5, 8, 1),  -- 订单ORD123460包含1个运动手环
(6, 9, 3),  -- 订单ORD123461包含3个儿童玩具车
(7, 10, 1);  -- 订单ORD123462包含1个办公椅
