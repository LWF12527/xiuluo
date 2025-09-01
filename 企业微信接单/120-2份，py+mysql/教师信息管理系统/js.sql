-- 创建数据库
CREATE DATABASE TeacherManagementSystem;
USE TeacherManagementSystem;

-- 创建部门表
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY, -- 部门ID
    DepartmentName VARCHAR(100) NOT NULL,       -- 部门名称
    DepartmentHead VARCHAR(100),                -- 部门负责人姓名
    EstablishedYear YEAR                        -- 部门成立年份
);

-- 创建教师表
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,   -- 教师ID
    TeacherName VARCHAR(100) NOT NULL,          -- 教师姓名
    Gender ENUM('Male', 'Female') NOT NULL,     -- 性别
    DateOfBirth DATE,                           -- 出生日期
    DepartmentID INT,                           -- 所属部门ID
    Email VARCHAR(100),                         -- 邮箱
    PhoneNumber VARCHAR(15),                    -- 电话号码
    HireDate DATE,                              -- 入职日期
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
        ON DELETE SET NULL                      -- 若部门被删除，设置为空
        ON UPDATE CASCADE                       -- 部门更新时同步更新
);

-- 创建课程表
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,    -- 课程ID
    CourseName VARCHAR(100) NOT NULL,           -- 课程名称
    CreditHours INT NOT NULL,                   -- 学分
    TeacherID INT,                              -- 授课教师ID
    DepartmentID INT,                           -- 所属部门ID
    Semester VARCHAR(50),                       -- 学期信息
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
        ON DELETE SET NULL                      -- 若教师被删除，设置为空
        ON UPDATE CASCADE,                      -- 教师更新时同步更新
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
        ON DELETE SET NULL                      -- 若部门被删除，设置为空
        ON UPDATE CASCADE                       -- 部门更新时同步更新
);

-- 插入示例数据到部门表
INSERT INTO Departments (DepartmentName, DepartmentHead, EstablishedYear)
VALUES 
('Computer Science', 'Dr. Alice Johnson', 1990),
('Mathematics', 'Dr. Bob Smith', 1985),
('Physics', 'Dr. Carol Lee', 2000);

-- 插入示例数据到教师表
INSERT INTO Teachers (TeacherName, Gender, DateOfBirth, DepartmentID, Email, PhoneNumber, HireDate)
VALUES
('John Doe', 'Male', '1980-05-15', 1, 'johndoe@school.edu', '123-456-7890', '2010-08-01'),
('Jane Smith', 'Female', '1985-07-20', 2, 'janesmith@school.edu', '234-567-8901', '2012-09-15'),
('Michael Brown', 'Male', '1975-12-10', 3, 'michaelbrown@school.edu', '345-678-9012', '2005-06-30');

-- 插入示例数据到课程表
INSERT INTO Courses (CourseName, CreditHours, TeacherID, DepartmentID, Semester)
VALUES
('Introduction to Programming', 3, 1, 1, 'Fall 2024'),
('Advanced Mathematics', 4, 2, 2, 'Spring 2024'),
('Quantum Physics', 3, 3, 3, 'Fall 2024');

-- 查询数据示例
-- 查询教师及其所在部门信息
SELECT 
    T.TeacherID, T.TeacherName, T.Gender, T.Email, D.DepartmentName
FROM 
    Teachers T
LEFT JOIN 
    Departments D ON T.DepartmentID = D.DepartmentID;

-- 查询课程及其相关教师和部门信息
SELECT 
    C.CourseID, C.CourseName, C.CreditHours, T.TeacherName AS Teacher, D.DepartmentName AS Department
FROM 
    Courses C
LEFT JOIN 
    Teachers T ON C.TeacherID = T.TeacherID
LEFT JOIN 
    Departments D ON C.DepartmentID = D.DepartmentID;
