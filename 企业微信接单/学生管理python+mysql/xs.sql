-- 创建学生管理系统数据库
CREATE DATABASE StudentManagementSystem;

-- 使用该数据库
USE StudentManagementSystem;

-- 1. 用户信息表
CREATE TABLE UserInfo (
    user_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '用户编号',
    username VARCHAR(50) NOT NULL COMMENT '用户名',
    password VARCHAR(255) NOT NULL COMMENT '用户密码',
    role ENUM('admin', 'teacher', 'student') NOT NULL COMMENT '用户角色（类型）'
) COMMENT '用户信息表';

-- 2. 学生信息表
CREATE TABLE StudentInfo (
    student_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '学生编号',
    name VARCHAR(50) NOT NULL COMMENT '姓名',
    gender ENUM('male', 'female') NOT NULL COMMENT '性别',
    age INT NOT NULL COMMENT '年龄',
    contact_info VARCHAR(50) COMMENT '联系方式'
) COMMENT '学生信息表';

-- 3. 专业表
CREATE TABLE Major (
    major_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '专业编号',
    major_name VARCHAR(100) NOT NULL COMMENT '专业名称'
) COMMENT '专业表';

-- 4. 科目（课程）表
CREATE TABLE Course (
    course_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '课程id',
    course_name VARCHAR(100) NOT NULL COMMENT '课程名称',
    major_id INT NOT NULL COMMENT '所属专业编号',
    FOREIGN KEY (major_id) REFERENCES Major(major_id)
) COMMENT '科目（课程）表';

-- 5. 分数表
CREATE TABLE Score (
    score_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '分数id',
    student_id INT NOT NULL COMMENT '学生id',
    course_id INT NOT NULL COMMENT '课程id',
    score DECIMAL(5,2) NOT NULL COMMENT '分数',
    score_type ENUM('midterm', 'final', 'assignment', 'quiz') NOT NULL COMMENT '分数类型',
    FOREIGN KEY (student_id) REFERENCES StudentInfo(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
) COMMENT '分数表';

-- 1. 插入用户信息表测试数据
INSERT INTO UserInfo (username, password, role)
VALUES 
('admin', 'admin123', 'admin'),
('teacher1', 'teacher123', 'teacher'),
('student1', 'student123', 'student'),
('student2', 'student456', 'student'),
('teacher2', 'teacher456', 'teacher');

-- 2. 插入学生信息表测试数据
INSERT INTO StudentInfo (name, gender, age, contact_info)
VALUES 
('张三', 'male', 20, '1234567890'),
('李四', 'female', 19, '0987654321'),
('王五', 'male', 22, '1122334455'),
('赵六', 'female', 21, '5566778899'),
('孙七', 'male', 23, '6677889900');

-- 3. 插入专业表测试数据
INSERT INTO Major (major_name)
VALUES 
('计算机科学'),
('信息技术'),
('电子工程'),
('数学与应用数学'),
('物理学');

-- 4. 插入课程表测试数据
INSERT INTO Course (course_name, major_id)
VALUES 
('程序设计基础', 1),
('数据结构', 1),
('电路原理', 3),
('线性代数', 4),
('大学物理', 5);

-- 5. 插入分数表测试数据
INSERT INTO Score (student_id, course_id, score, score_type)
VALUES 
(1, 1, 85.5, 'midterm'),
(2, 1, 90.0, 'final'),
(3, 2, 88.0, 'assignment'),
(4, 3, 92.5, 'quiz'),
(5, 4, 87.0, 'midterm');

