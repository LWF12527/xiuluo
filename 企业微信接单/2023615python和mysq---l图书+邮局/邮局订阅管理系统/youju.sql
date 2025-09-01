drop database if exists youju;
create database if not exists youju;
use youju;
-- ����������
CREATE TABLE IF NOT EXISTS newspapers (
                                          id INT AUTO_INCREMENT PRIMARY KEY,
                                          name VARCHAR(255),
                                          price FLOAT
    );

-- �����û���
CREATE TABLE IF NOT EXISTS users (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     name VARCHAR(255),
                                     address VARCHAR(255)
    );

-- �������ı�
CREATE TABLE IF NOT EXISTS subscriptions (
                                             id INT AUTO_INCREMENT PRIMARY KEY,
                                             user_id INT,
                                             newspaper_id INT,
                                             date DATE,
                                             FOREIGN KEY (user_id) REFERENCES users(id),
                                             FOREIGN KEY (newspaper_id) REFERENCES newspapers(id)
    );

-- ��������¼��
CREATE TABLE IF NOT EXISTS stock (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     newspaper_id INT,
                                     quantity INT,
                                     FOREIGN KEY (newspaper_id) REFERENCES newspapers(id)
    );

-- �������ż�¼��
CREATE TABLE IF NOT EXISTS distribution (
                                            id INT AUTO_INCREMENT PRIMARY KEY,
                                            user_id INT,
                                            newspaper_id INT,
                                            quantity INT,
                                            FOREIGN KEY (user_id) REFERENCES users(id),
                                            FOREIGN KEY (newspaper_id) REFERENCES newspapers(id)
    );



-- �������������
INSERT INTO newspapers (name, price) VALUES
                                         ('����1', 10.99),
                                         ('����2', 9.99),
                                         ('����3', 8.99),
                                         ('����4', 7.99),
                                         ('����5', 6.99);

-- �û����������
INSERT INTO users (name, address) VALUES
                                      ('�û�1', '��ַ1'),
                                      ('�û�2', '��ַ2'),
                                      ('�û�3', '��ַ3'),
                                      ('�û�4', '��ַ4'),
                                      ('�û�5', '��ַ5');

-- ���ı��������
INSERT INTO subscriptions (user_id, newspaper_id, date) VALUES
                                                            (1, 1, '2023-01-01'),
                                                            (2, 2, '2023-01-02'),
                                                            (3, 3, '2023-01-03'),
                                                            (4, 4, '2023-01-04'),
                                                            (5, 5, '2023-01-05');

-- ����¼���������
INSERT INTO stock (newspaper_id, quantity) VALUES
                                               (1, 100),
                                               (2, 200),
                                               (3, 300),
                                               (4, 400),
                                               (5, 500);

-- ���ż�¼���������
INSERT INTO distribution (user_id, newspaper_id, quantity) VALUES
                                                               (1, 1, 10),
                                                               (2, 2, 20),
                                                               (3, 3, 30),
                                                               (4, 4, 40),
                                                               (5, 5, 50);
