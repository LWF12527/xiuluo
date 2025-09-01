CREATE DATABASE Gym_management;
USE Gym_management;

-- ����������
CREATE TABLE gym (
  gym_id INT PRIMARY KEY,
  name VARCHAR(20) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address VARCHAR(100) NOT NULL,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL
);

-- ����������
CREATE TABLE coach (
  coach_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  gender ENUM('Male', 'Female') NOT NULL,
  birthdate DATE NOT NULL,
  coach_type ENUM('Regular', 'Premium') NOT NULL,
  gym_id INT,
  FOREIGN KEY (gym_id) REFERENCES gym(gym_id)
);

-- �����γ̱�
CREATE TABLE course (
  course_id INT PRIMARY KEY,
  name VARCHAR(20) NOT NULL,
  description VARCHAR(255) NOT NULL,
  price DECIMAL(8, 2) NOT NULL,
  max_capacity INT NOT NULL,
  coach_id INT,
  gym_id INT,
  FOREIGN KEY (coach_id) REFERENCES coach(coach_id),
  FOREIGN KEY (gym_id) REFERENCES gym(gym_id)
);

-- ������Ա��
CREATE TABLE member (
  member_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  gender ENUM('Male', 'Female') NOT NULL,
  birthdate DATE NOT NULL,
  member_type ENUM('Regular', 'Premium') NOT NULL
);

-- ��������γ̱�
CREATE TABLE course_purchase (
  purchase_id INT PRIMARY KEY AUTO_INCREMENT,
  member_id INT,
  course_id INT,
  purchase_date TIMESTAMP NOT NULL,
  price DECIMAL(8, 2) NOT NULL,
  FOREIGN KEY (member_id) REFERENCES member(member_id),
  FOREIGN KEY (course_id) REFERENCES course(course_id)
);

-- �����������������Զ�����ʱ���
DELIMITER //
CREATE TRIGGER course_purchase_insert_trigger
BEFORE INSERT ON course_purchase
FOR EACH ROW
BEGIN
  SET NEW.purchase_date = NOW();
END //
DELIMITER ;

-- ������ͼ���鿴�µ���ѧԱ
CREATE VIEW course_purchase_view AS
SELECT c.course_id, c.name AS course_name, c.description, c.price, c.max_capacity, m.member_id, m.username, m.phone, m.gender, m.birthdate, m.member_type
FROM course c
JOIN course_purchase cp ON c.course_id = cp.course_id
JOIN member m ON cp.member_id = m.member_id;


-- ��coach���gym_id�����������
CREATE INDEX idx_coach_gym_id ON coach (gym_id);

-- ��course���coach_id�����������
CREATE INDEX idx_course_coach_id ON course (coach_id);


-- ���뽡������
INSERT INTO gym (gym_id, name, phone, address, username, password)
VALUES
(1, 'Gym A', '1234567890', '123 Main St', 'admin1', 'password1'),
(2, 'Gym B', '9876543210', '456 Elm St', 'admin2', 'password2'),
(3, 'Gym C', '5555555555', '789 Oak St', 'admin3', 'password3'),
(4, 'Gym D', '9999999999', '321 Pine St', 'admin4', 'password4'),
(5, 'Gym E', '1111111111', '654 Maple St', 'admin5', 'password5');

-- �����������
INSERT INTO coach (username, password, phone, gender, birthdate, coach_type, gym_id)
VALUES
('Coach1', 'password1', '1234567890', 'Male', '1980-05-15', 'Regular', 1),
('Coach2', 'password2', '9876543210', 'Female', '1983-10-20', 'Premium', 2),
('Coach3', 'password3', '5555555555', 'Male', '1975-12-01', 'Regular', 3),
('Coach4', 'password4', '9999999999', 'Female', '1988-07-05', 'Premium', 4),
('Coach5', 'password5', '1111111111', 'Male', '1991-09-25', 'Regular', 5);

-- ����γ�����
INSERT INTO course (course_id, name, description, price, max_capacity, coach_id, gym_id)
VALUES
(1, 'Yoga Class', 'A relaxing yoga class for all levels', 20.00, 15, 1, 1),
(2, 'Spin Class', 'An intense indoor cycling workout', 15.00, 10, 2, 2),
(3, 'Zumba Class', 'A fun and energetic dance fitness class', 12.00, 20, 3, 3),
(4, 'Pilates Class', 'A low-impact exercise method to improve flexibility and strength', 18.00, 12, 4, 4),
(5, 'Bootcamp Class', 'A high-intensity workout combining cardio and strength training', 25.00, 15, 5, 5);

-- �����Ա����
INSERT INTO member (username, password, phone, gender, birthdate, member_type)
VALUES
('JohnDoe', 'password1', '1234567890', 'Male', '1990-01-01', 'Regular'),
('JaneSmith', 'password2', '9876543210', 'Female', '1995-05-10', 'Regular'),
('MikeJohnson', 'password3', '5555555555', 'Male', '1985-09-15', 'Premium'),
('EmilyDavis', 'password4', '9999999999', 'Female', '1998-07-20', 'Premium'),
('DavidWilson', 'password5', '1111111111', 'Male', '1992-03-30', 'Regular');

-- ���빺��γ�����
INSERT INTO course_purchase (member_id, course_id, purchase_date, price)
VALUES
(1, 1, '2024-05-01 10:00:00', 20.00),
(2, 3, '2024-05-02 14:30:00', 12.00),
(3, 2, '2024-05-03 17:45:00', 15.00),
(4, 4, '2024-05-04 09:15:00', 18.00),
(5, 5, '2024-05-05 16:00:00', 25.00);
