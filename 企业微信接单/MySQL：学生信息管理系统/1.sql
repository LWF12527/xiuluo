-- 1. 创建数据库
CREATE DATABASE student_management_system;
USE student_management_system;
-- 2. 创建学生信息表（students）
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,    -- 学生ID，主键
    name VARCHAR(50) NOT NULL,                     -- 学生姓名
    gender CHAR(1) NOT NULL,                       -- 性别 M: 男, F: 女
    birthdate DATE NOT NULL,                       -- 出生日期
    phone VARCHAR(15),                             -- 联系电话
    email VARCHAR(50),                             -- 邮箱
    address VARCHAR(100),                          -- 地址
    enrollment_date DATE NOT NULL,                 -- 入学日期
    major VARCHAR(50) NOT NULL,                    -- 专业
    status CHAR(1) NOT NULL                        -- 学生状态 A: 在读, G: 毕业, D: 休学
);
INSERT INTO students (name, gender, birthdate, phone, email, address, enrollment_date, major, status) 
VALUES 
('张三', 'M', '2005-01-15', '13800138000', 'zhangsan@example.com', '成都市武侯区', '2023-09-01', '计算机科学', 'A'),
('李四', 'F', '2004-11-10', '13800138001', 'lisi@example.com', '成都市青羊区', '2022-09-01', '软件工程', 'A'),
('王五', 'M', '2005-02-20', '13800138002', 'wangwu@example.com', '成都市锦江区', '2023-09-01', '电子工程', 'A'),
('赵六', 'F', '2004-05-30', '13800138003', 'zhaoliu@example.com', '成都市高新区', '2021-09-01', '网络工程', 'A'),
('孙七', 'M', '2005-07-25', '13800138004', 'sunqi@example.com', '成都市成华区', '2023-09-01', '人工智能', 'A');

-- 3. 创建课程信息表（courses）
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,     -- 课程ID，主键
    course_name VARCHAR(100) NOT NULL,             -- 课程名称
    course_code VARCHAR(20) UNIQUE NOT NULL,       -- 课程代码，唯一
    course_credit INT NOT NULL,                    -- 课程学分
    course_teacher VARCHAR(50),                    -- 授课教师
    semester VARCHAR(20),                          -- 学期（如：2024-2025 秋季学期）
    department VARCHAR(50)                         -- 所属学院
);
INSERT INTO courses (course_name, course_code, course_credit, course_teacher, semester, department) 
VALUES
('数据结构', 'CS101', 3, '李教授', '2024-2025 秋季学期', '计算机科学与技术'),
('操作系统', 'CS102', 4, '王教授', '2024-2025 秋季学期', '计算机科学与技术'),
('电路原理', 'EE101', 3, '张教授', '2024-2025 秋季学期', '电子工程'),
('数据库原理', 'CS103', 3, '赵教授', '2024-2025 春季学期', '计算机科学与技术'),
('人工智能基础', 'AI101', 4, '孙教授', '2024-2025 秋季学期', '人工智能');
-- 4. 创建选课记录表（course_enrollment）
CREATE TABLE course_enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,  -- 选课记录ID，主键
    student_id INT NOT NULL,                       -- 学生ID，外键
    course_id INT NOT NULL,                        -- 课程ID，外键
    enrollment_date DATE NOT NULL,                 -- 选课日期
    grade DECIMAL(5, 2),                           -- 成绩（可为空）
    status CHAR(1) NOT NULL,                       -- 选课状态 P: 已选, D: 已退
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
INSERT INTO course_enrollment (student_id, course_id, enrollment_date, grade, status) 
VALUES
(1, 1, '2024-09-01', NULL, 'P'),
(1, 2, '2024-09-01', NULL, 'P'),
(2, 1, '2023-09-01', NULL, 'P'),
(3, 3, '2024-09-01', NULL, 'P'),
(4, 2, '2024-09-01', NULL, 'P');
-- 5. 创建成绩表（grades）
CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,       -- 成绩ID，主键
    student_id INT NOT NULL,                       -- 学生ID，外键
    course_id INT NOT NULL,                        -- 课程ID，外键
    score DECIMAL(5, 2) NOT NULL,                  -- 成绩
    grade_date DATE NOT NULL,                      -- 成绩录入日期
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
INSERT INTO grades (student_id, course_id, score, grade_date) 
VALUES
(1, 1, 90.5, '2024-12-01'),
(1, 2, 85.0, '2024-12-01'),
(2, 1, 88.0, '2023-12-01'),
(3, 3, 92.0, '2024-12-01'),
(4, 2, 78.5, '2024-12-01');
-- 6. 创建出勤记录表（attendance）
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,  -- 出勤记录ID，主键
    student_id INT NOT NULL,                       -- 学生ID，外键
    course_id INT NOT NULL,                        -- 课程ID，外键
    date DATE NOT NULL,                            -- 出勤日期
    status CHAR(1) NOT NULL,                       -- 出勤状态 P: 出席, A: 缺席, L: 迟到
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
INSERT INTO attendance (student_id, course_id, date, status) 
VALUES
(1, 1, '2024-09-10', 'P'),
(1, 2, '2024-09-10', 'P'),
(2, 1, '2023-09-10', 'P'),
(3, 3, '2024-09-10', 'A'),
(4, 2, '2024-09-10', 'P');
-- 7. 创建教师信息表（teachers）
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,     -- 教师ID，主键
    name VARCHAR(50) NOT NULL,                      -- 教师姓名
    gender CHAR(1) NOT NULL,                        -- 性别 M: 男, F: 女
    phone VARCHAR(15),                              -- 联系电话
    email VARCHAR(50),                              -- 邮箱
    department VARCHAR(50),                         -- 所属学院
    courses_taught TEXT                             -- 所授课程（课程ID列表）
);
INSERT INTO teachers (name, gender, phone, email, department, courses_taught) 
VALUES
('李教授', 'M', '13900139000', 'li@example.com', '计算机科学与技术', 'CS101, CS102'),
('王教授', 'M', '13900139001', 'wang@example.com', '计算机科学与技术', 'CS102'),
('张教授', 'M', '13900139002', 'zhang@example.com', '电子工程', 'EE101'),
('赵教授', 'F', '13900139003', 'zhao@example.com', '计算机科学与技术', 'CS103'),
('孙教授', 'M', '13900139004', 'sun@example.com', '人工智能', 'AI101');
-- 8. 创建学生课程成绩汇总表（student_course_summary）
CREATE TABLE student_course_summary (
    student_id INT PRIMARY KEY,                     -- 学生ID，外键
    total_courses INT NOT NULL,                      -- 总选修课程数
    total_credits INT NOT NULL,                      -- 总学分
    average_grade DECIMAL(5, 2),                     -- 平均成绩
    gpa DECIMAL(5, 2),                               -- GPA
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
INSERT INTO student_course_summary (student_id, total_courses, total_credits, average_grade, gpa) 
VALUES
(1, 2, 7, 87.75, 3.5),
(2, 1, 3, 88.0, 3.6),
(3, 1, 3, 92.0, 3.8),
(4, 2, 6, 83.25, 3.2),
(5, 2, 7, 85.0, 3.4);
