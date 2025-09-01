-- 创建数据库
drop database if exists stu;
create database if not exists stu;
use stu;

-- 创建学生信息表：

CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       gender VARCHAR(10),
       score INT,
       age INT
   );


-- 写入5条不同的数据：

INSERT INTO students (name, gender, score, age) VALUES
       ('张三', '男', 80, 18),
       ('李四', '男', 75, 19),
       ('王五', '女', 90, 20),
       ('赵六', '男', 70, 21),
       ('钱七', '女', 85, 22);

--. 查询所有的男生数据：

SELECT name, age FROM students WHERE gender = '男';


-- 查询及格学生成绩信息：

SELECT * FROM students WHERE score >= 60;


-- 按照学生的分数进行排序：

SELECT * FROM students ORDER BY score;


-- 将所有女生年龄增加一岁：

UPDATE students SET age = age + 1 WHERE gender = '女';
