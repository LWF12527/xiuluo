-- 创建数据库
CREATE DATABASE factory_inventory_management;

-- 选择数据库
USE factory_inventory_management;

-- 创建仓库表
CREATE TABLE warehouses (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_name VARCHAR(255) NOT NULL,
    warehouse_phone VARCHAR(20),
    warehouse_address VARCHAR(255)
);

-- 创建零件表
CREATE TABLE parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    part_name VARCHAR(255) NOT NULL,
    specification VARCHAR(255),
    material_composition VARCHAR(255),
    unit_price DECIMAL(10, 2)  -- 添加 unit_price 列，用于查询价格
);

-- 创建经销商表
CREATE TABLE distributors (
    distributor_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20),
    legal_person VARCHAR(100),
    account_number VARCHAR(50)
);

-- 创建订单表
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_id INT,
    order_date DATE,
    order_responsible VARCHAR(255),
    FOREIGN KEY (distributor_id) REFERENCES distributors(distributor_id)
);

-- 创建订单零件关联表（一个订单可以包含多个零件）
CREATE TABLE order_parts (
    order_id INT,
    part_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    PRIMARY KEY (order_id, part_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (part_id) REFERENCES parts(part_id)
);

-- 创建仓库职工表
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    position VARCHAR(50), -- 如：仓库主任、保管员
    join_date DATE,
    warehouse_id INT,
    supervisor_id INT,  -- 指向领导的职工ID
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (supervisor_id) REFERENCES employees(employee_id) -- 自引用，领导与被领导关系
);

-- 创建仓库零件库存表（记录每个仓库中的零件库存量）
CREATE TABLE warehouse_inventory (
    warehouse_id INT,
    part_id INT,
    stock_quantity INT,
    PRIMARY KEY (warehouse_id, part_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (part_id) REFERENCES parts(part_id)
);

-- 创建仓库与职工的关联表（一个仓库可以有多个职工）
CREATE TABLE warehouse_employees (
    warehouse_id INT,
    employee_id INT,
    PRIMARY KEY (warehouse_id, employee_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- 插入仓库表数据 (warehouses)
INSERT INTO warehouses (warehouse_name, warehouse_phone, warehouse_address) VALUES
('仓库A', '010-12345678', '北京市朝阳区仓库A'),
('仓库B', '010-23456789', '北京市海淀区仓库B'),
('仓库C', '010-34567890', '北京市东城区仓库C'),
('仓库D', '010-45678901', '北京市西城区仓库D'),
('仓库E', '010-56789012', '北京市昌平区仓库E'),
('仓库F', '010-67890123', '北京市丰台区仓库F'),
('仓库G', '010-78901234', '北京市石景山区仓库G'),
('仓库H', '010-89012345', '北京市顺义区仓库H'),
('仓库I', '010-90123456', '北京市大兴区仓库I'),
('仓库J', '010-01234567', '北京市通州区仓库J');

-- 插入零件表数据 (parts)

INSERT INTO parts (part_name, specification, material_composition, unit_price) VALUES
('螺栓', 'M10x50', '不锈钢304', 5.25),
('垫圈', '外径20mm, 内径12mm', '黄铜', 2.75),
('轴承', '6203-2RS', '铬钢', 15.50),
('齿轮', '模数2.5, 24齿', '45#钢', 12.30),
('弹簧', '直径8mm, 自由高度30mm', '65Mn弹簧钢', 8.99),
('活塞', '直径50mm, 高度70mm', '铝合金', 35.00),
('阀门', 'DN25, PN16', '铸铁', 22.45),
('连杆', '长度150mm, 直径12mm', '合金钢', 45.75),
('皮带轮', '直径100mm, 宽度20mm', '灰口铸铁', 18.20),
('密封圈', '矩形截面, 外径50mm, 内径30mm', '氟橡胶', 4.50);

-- 插入经销商表数据 (distributors)
INSERT INTO distributors (distributor_name, address, phone, legal_person, account_number) VALUES
('经销商A', '上海市浦东新区A', '021-10000001', '法人A', '1234567890'),
('经销商B', '上海市黄浦区B', '021-10000002', '法人B', '2345678901'),
('经销商C', '深圳市南山区C', '0755-20000003', '法人C', '3456789012'),
('经销商D', '深圳市福田区D', '0755-20000004', '法人D', '4567890123'),
('经销商E', '广州市天河区E', '020-30000005', '法人E', '5678901234'),
('经销商F', '广州市越秀区F', '020-30000006', '法人F', '6789012345'),
('经销商G', '北京市朝阳区G', '010-40000007', '法人G', '7890123456'),
('经销商H', '北京市海淀区H', '010-40000008', '法人H', '8901234567'),
('经销商I', '杭州市西湖区I', '0571-50000009', '法人I', '9012345678'),
('经销商J', '杭州市下城区J', '0571-50000010', '法人J', '0123456789');
-- 插入订单表数据 (orders)
INSERT INTO orders (distributor_id, order_date, order_responsible) VALUES
(1, '2024-01-01', '负责人A'),
(2, '2024-01-02', '负责人B'),
(3, '2024-01-03', '负责人C'),
(4, '2024-01-04', '负责人D'),
(5, '2024-01-05', '负责人E'),
(6, '2024-01-06', '负责人F'),
(7, '2024-01-07', '负责人G'),
(8, '2024-01-08', '负责人H'),
(9, '2024-01-09', '负责人I'),
(10, '2024-01-10', '负责人J');
-- 插入订单零件关联表数据 (order_parts)
INSERT INTO order_parts (order_id, part_id, quantity, unit_price) VALUES
(1, 1, 10, 50.00),
(1, 2, 20, 40.00),
(2, 3, 15, 60.00),
(2, 4, 25, 30.00),
(3, 5, 30, 70.00),
(3, 6, 20, 80.00),
(4, 7, 25, 100.00),
(4, 8, 10, 200.00),
(5, 9, 50, 10.00),
(5, 10, 60, 15.00);
-- 插入职工表数据 (employees)
INSERT INTO employees (employee_name, position, warehouse_id, supervisor_id, join_date) VALUES
('杨晨', '仓库主任', 1, NULL,'2018-03-02'),
('职工B', '保管员', 1, 1,'2018-03-02'),
('职工C', '保管员', 2, 1,'2018-03-02'),
('职工D', '仓库主任', 2, NULL,'2018-03-02'),
('职工E', '保管员', 2, 4,'2018-03-02'),
('职工F', '仓库主任',2, 3,'2018-03-02'),
('职工G', '保管员', 3, 6,'2018-03-02'),
('职工H', '保管员', 4, 6,'2018-03-02'),
('职工I', '仓库主任',3, 4,'2018-03-02'),
('职工J', '保管员', 5, 8,'2018-03-02');
-- 插入仓库零件库存表数据 (warehouse_inventory)
INSERT INTO warehouse_inventory (warehouse_id, part_id, stock_quantity) VALUES
(1, 1, 100),
(1, 2, 200),
(2, 3, 150),
(2, 4, 250),
(3, 5, 300),
(3, 6, 400),
(4, 7, 500),
(4, 8, 100),
(5, 9, 600),
(5, 10, 700);

-- 插入仓库职工关联表数据 (warehouse_employees)
INSERT INTO warehouse_employees (warehouse_id, employee_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 9),
(5, 10);


-- 插入经销商表
INSERT INTO distributors (distributor_name, address, phone, legal_person, account_number)
VALUES
('Distributor A', 'Address A', '1234567890', 'Person A', 'A001'),
('Distributor B', 'Address B', '2345678901', 'Person B', 'B002'),
('Distributor C', 'Address C', '3456789012', 'Person C', 'C003');

-- 插入零件表
INSERT INTO parts (part_name, specification, material_composition, unit_price)
VALUES
('Part 1', 'Spec 1', 'Material A', 300),  -- 单价300
('Part 2', 'Spec 2', 'Material B', 200),  -- 单价200
('Part 3', 'Spec 3', 'Material C', 150),  -- 单价150
('Part 4', 'Spec 4', 'Material D', 500);  -- 单价500

-- 插入订单表
INSERT INTO orders (distributor_id, order_date, order_responsible)
VALUES
(1, '2018-11-01', 'Responsible A'),
(2, '2018-12-01', 'Responsible B'),
(3, '2018-10-20', 'Responsible C');

-- 插入订单零件关联表
INSERT INTO order_parts (order_id, part_id, quantity, unit_price)
VALUES
(1, 1, 40, 300),  -- 订单1, 零件1, 数量40
(1, 2, 30, 200),  -- 订单1, 零件2, 数量30
(2, 2, 50, 200),  -- 订单2, 零件2, 数量50
(2, 3, 60, 150),  -- 订单2, 零件3, 数量60
(3, 3, 10, 150),  -- 订单3, 零件3, 数量10
(3, 4, 20, 500);  -- 订单3, 零件4, 数量20
