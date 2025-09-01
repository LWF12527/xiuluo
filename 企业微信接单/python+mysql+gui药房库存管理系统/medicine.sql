drop database if exists medicine;
create database if not exists medicine;
use medicine;

-- ����ҩƷ��
CREATE TABLE drug (
                      id INT PRIMARY KEY AUTO_INCREMENT,
                      name VARCHAR(255) NOT NULL,
                      manufacturer VARCHAR(255) NOT NULL,
                      price DECIMAL(10, 2) NOT NULL,
                      dosage_form VARCHAR(255) NOT NULL,
                      specification VARCHAR(255) NOT NULL
);

-- ����ҩƷ�����
CREATE TABLE drug_category (
                               id INT PRIMARY KEY AUTO_INCREMENT,
                               name VARCHAR(255) NOT NULL
);

-- ����ҩƷ���������
CREATE TABLE drug_category_relation (
                                        drug_id INT NOT NULL,
                                        category_id INT NOT NULL,
                                        PRIMARY KEY (drug_id, category_id),
                                        FOREIGN KEY (drug_id) REFERENCES drug(id),
                                        FOREIGN KEY (category_id) REFERENCES drug_category(id)
);

-- ����ҩƷ���۱�
CREATE TABLE drug_sale (
                           id INT PRIMARY KEY AUTO_INCREMENT,
                           drug_id INT NOT NULL,
                           sale_date DATE NOT NULL,
                           sale_quantity INT NOT NULL,
                           sale_price DECIMAL(10, 2) NOT NULL,
                           FOREIGN KEY (drug_id) REFERENCES drug(id)
);

-- ����ҩƷ������
CREATE TABLE drug_purchase (
                               id INT PRIMARY KEY AUTO_INCREMENT,
                               drug_id INT NOT NULL,
                               purchase_date DATE NOT NULL,
                               purchase_quantity INT NOT NULL,
                               purchase_price DECIMAL(10, 2) NOT NULL,
                               FOREIGN KEY (drug_id) REFERENCES drug(id)
);

-- ����ҩƷ����
CREATE TABLE drug_inventory (
                                id INT PRIMARY KEY AUTO_INCREMENT,
                                drug_id INT NOT NULL,
                                inventory_quantity INT NOT NULL,
                                FOREIGN KEY (drug_id) REFERENCES drug(id)
);


-- ����ҩƷ����
INSERT INTO drug (name, manufacturer, price, dosage_form, specification) VALUES
                                                                             ('��Ī����', 'ʯҩ����', 10.00, 'Ƭ��', '0.25g*12Ƭ/��'),
                                                                             ('ͷ�߿���', 'ʯҩ����', 20.00, 'Ƭ��', '0.5g*12Ƭ/��'),
                                                                             ('�����ʲ�Ƭ', 'ͬ����', 5.00, 'Ƭ��', '0.3g*24Ƭ/��'),
                                                                             ('����������', '����ͬ����', 15.00, '������', '10g*10��/��'),
                                                                             ('�п�', '����ҩҵ', 8.00, 'Ƭ��', '0.1g*24Ƭ/��'),
                                                                             ('����ͨ', '�ݶ�', 30.00, 'Ƭ��', '20mg*14Ƭ/��'),
                                                                             ('ǿ������¶', '����ͬ����', 12.00, '�ڷ�Һ��', '10ml*12֧/��'),
                                                                             ('ʹ����', 'ͬ����', 15.00, 'Ƭ��', '0.3g*12Ƭ/��'),
                                                                             ('���ϰ�ҩ', '���ϰ�ҩ����', 8.00, '�����', '6��'),
                                                                             ('��������Ƭ', '����ͬ����', 6.00, 'Ƭ��', '0.3g*12Ƭ/��');

-- ����ҩƷ��������
INSERT INTO drug_category (name) VALUES
                                     ('������'),
                                     ('��ðҩ'),
                                     ('����ҩ'),
                                     ('ֹʹҩ'),
                                     ('������ʹҩ'),
                                     ('����ҩ'),
                                     ('����ҩ'),
                                     ('�����'),
                                     ('�ڷ�Һ��'),
                                     ('������');

-- ����ҩƷ�����������
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

-- ����ҩƷ��������
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

-- ����ҩƷ��������
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

-- ����ҩƷ�������
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
