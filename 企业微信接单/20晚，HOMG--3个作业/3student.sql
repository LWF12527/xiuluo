-- �������ݿ�
drop database if exists stu;
create database if not exists stu;
use stu;

-- ����ѧ����Ϣ��

CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       gender VARCHAR(10),
       score INT,
       age INT
   );


-- д��5����ͬ�����ݣ�

INSERT INTO students (name, gender, score, age) VALUES
       ('����', '��', 80, 18),
       ('����', '��', 75, 19),
       ('����', 'Ů', 90, 20),
       ('����', '��', 70, 21),
       ('Ǯ��', 'Ů', 85, 22);

--. ��ѯ���е��������ݣ�

SELECT name, age FROM students WHERE gender = '��';


-- ��ѯ����ѧ���ɼ���Ϣ��

SELECT * FROM students WHERE score >= 60;


-- ����ѧ���ķ�����������

SELECT * FROM students ORDER BY score;


-- ������Ů����������һ�꣺

UPDATE students SET age = age + 1 WHERE gender = 'Ů';
