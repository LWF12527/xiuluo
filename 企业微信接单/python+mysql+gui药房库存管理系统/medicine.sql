drop database if exists medicine;
create database if not exists medicine;
use medicine;

-- 创建药品表
CREATE TABLE drug (
                      id INT PRIMARY KEY AUTO_INCREMENT,
                      name VARCHAR(255) NOT NULL,
                      manufacturer VARCHAR(255) NOT NULL,
                      price DECIMAL(10, 2) NOT NULL,
                      dosage_form VARCHAR(255) NOT NULL,
                      specification VARCHAR(255) NOT NULL
);

-- 创建药品分类表
CREATE TABLE drug_category (
                               id INT PRIMARY KEY AUTO_INCREMENT,
                               name VARCHAR(255) NOT NULL
);

-- 创建药品分类关联表
CREATE TABLE drug_category_relation (
                                        drug_id INT NOT NULL,
                                        category_id INT NOT NULL,
                                        PRIMARY KEY (drug_id, category_id),
                                        FOREIGN KEY (drug_id) REFERENCES drug(id),
                                        FOREIGN KEY (category_id) REFERENCES drug_category(id)
);

-- 创建药品销售表
CREATE TABLE drug_sale (
                           id INT PRIMARY KEY AUTO_INCREMENT,
                           drug_id INT NOT NULL,
                           sale_date DATE NOT NULL,
                           sale_quantity INT NOT NULL,
                           sale_price DECIMAL(10, 2) NOT NULL,
                           FOREIGN KEY (drug_id) REFERENCES drug(id)
);

-- 创建药品进货表
CREATE TABLE drug_purchase (
                               id INT PRIMARY KEY AUTO_INCREMENT,
                               drug_id INT NOT NULL,
                               purchase_date DATE NOT NULL,
                               purchase_quantity INT NOT NULL,
                               purchase_price DECIMAL(10, 2) NOT NULL,
                               FOREIGN KEY (drug_id) REFERENCES drug(id)
);

-- 创建药品库存表
CREATE TABLE drug_inventory (
                                id INT PRIMARY KEY AUTO_INCREMENT,
                                drug_id INT NOT NULL,
                                inventory_quantity INT NOT NULL,
                                FOREIGN KEY (drug_id) REFERENCES drug(id)
);


-- 插入药品数据
INSERT INTO drug (name, manufacturer, price, dosage_form, specification) VALUES
                                                                             ('阿莫西林', '石药集团', 10.00, '片剂', '0.25g*12片/盒'),
                                                                             ('头孢克洛', '石药集团', 20.00, '片剂', '0.5g*12片/盒'),
                                                                             ('复方甘草片', '同仁堂', 5.00, '片剂', '0.3g*24片/盒'),
                                                                             ('板蓝根颗粒', '北京同仁堂', 15.00, '颗粒剂', '10g*10袋/盒'),
                                                                             ('感康', '九州药业', 8.00, '片剂', '0.1g*24片/盒'),
                                                                             ('开博通', '拜耳', 30.00, '片剂', '20mg*14片/盒'),
                                                                             ('强力枇杷露', '北京同仁堂', 12.00, '口服液剂', '10ml*12支/盒'),
                                                                             ('痛经宁', '同仁堂', 15.00, '片剂', '0.3g*12片/盒'),
                                                                             ('云南白药', '云南白药集团', 8.00, '贴膏剂', '6贴'),
                                                                             ('黄连上清片', '北京同仁堂', 6.00, '片剂', '0.3g*12片/盒');

-- 插入药品分类数据
INSERT INTO drug_category (name) VALUES
                                     ('抗生素'),
                                     ('感冒药'),
                                     ('消炎药'),
                                     ('止痛药'),
                                     ('解热镇痛药'),
                                     ('咳嗽药'),
                                     ('调节药'),
                                     ('贴膏剂'),
                                     ('口服液剂'),
                                     ('颗粒剂');

-- 插入药品分类关联数据
INSERT INTO drug_category_relation (drug_id, category_id) VALUES
                                                              (1, 1),
                                                              (2, 1),
                                                              (3, 3),
                                                              (4, 2),
                                                              (5, 2),
                                                              (6, 5),
                                                              (7, 6),
                                                              (8, 4),
                                                              (9, 8),
                                                              (10, 1);

-- 插入药品销售数据
INSERT INTO drug_sale (drug_id, sale_date, sale_quantity, sale_price) VALUES
                                                                          (1, '2023-06-01', 10, 15.00),
                                                                          (2, '2023-06-01', 20, 30.00),
                                                                          (3, '2023-06-02', 5, 10.00),
                                                                          (4, '2023-06-02', 8, 20.00),
                                                                          (5, '2023-06-03', 15, 12.00),
                                                                          (6, '2023-06-03', 6, 40.00),
                                                                          (7, '2023-06-04', 12, 18.00),
                                                                          (8, '2023-06-04', 10, 25.00),
                                                                          (9, '2023-06-05', 20, 6.00),
                                                                          (10, '2023-06-05', 5, 8.00);

-- 插入药品进货数据
INSERT INTO drug_purchase (drug_id, purchase_date, purchase_quantity, purchase_price) VALUES
                                                                                          (1, '2023-05-20', 100, 8.00),
                                                                                          (2, '2023-05-20', 50, 15.00),
                                                                                          (3, '2023-05-21', 200, 3.00),
                                                                                          (4, '2023-05-21', 80, 10.00),
                                                                                          (5, '2023-05-22', 150, 5.00),
                                                                                          (6, '2023-05-22', 30, 25.00),
                                                                                          (7, '2023-05-23', 60, 8.00),
                                                                                          (8, '2023-05-23', 40, 20.00),
                                                                                          (9, '2023-05-24', 100, 2.00),
                                                                                          (10, '2023-05-24', 50, 4.00);

-- 插入药品库存数据
INSERT INTO drug_inventory (drug_id, inventory_quantity) VALUES
                                                             (1, 80),
                                                             (2, 30),
                                                             (3, 150),
                                                             (4, 72),
                                                             (5, 135),
                                                             (6, 24),
                                                             (7, 48),
                                                             (8, 30),
                                                             (9, 80),
                                                             (10, 40);
