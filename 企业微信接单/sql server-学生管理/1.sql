CREATE DATABASE StudentManagement;
GO

USE StudentManagement;
GO

CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY(1,1), -- 学号（自动增长）
    Name NVARCHAR(50) NOT NULL,             -- 学生姓名
    Gender CHAR(1) CHECK (Gender IN ('M', 'F')), -- 性别（M: 男, F: 女）
    DateOfBirth DATE NOT NULL,              -- 出生日期
    Major NVARCHAR(50) NOT NULL,            -- 专业
    EnrollmentDate DATE NOT NULL,           -- 入学日期
    Contact NVARCHAR(20)                    -- 联系方式
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY IDENTITY(1,1), -- 课程编号（自动增长）
    CourseName NVARCHAR(100) NOT NULL,     -- 课程名称
    Credits INT CHECK (Credits > 0),       -- 学分
    Instructor NVARCHAR(50) NOT NULL       -- 授课教师
);

CREATE TABLE Grades (
    GradeID INT PRIMARY KEY IDENTITY(1,1), -- 成绩编号
    StudentID INT NOT NULL,               -- 学生编号（外键）
    CourseID INT NOT NULL,                -- 课程编号（外键）
    Score DECIMAL(5,2) CHECK (Score >= 0 AND Score <= 100), -- 分数
    GradeDate DATE NOT NULL,              -- 成绩录入日期
    CONSTRAINT FK_Grades_Student FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    CONSTRAINT FK_Grades_Course FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY IDENTITY(1,1), -- 考勤编号
    StudentID INT NOT NULL,                    -- 学生编号（外键）
    AttendanceDate DATE NOT NULL,              -- 考勤日期
    Status NVARCHAR(20) CHECK (Status IN ('Present', 'Absent', 'Late')), -- 考勤状态
    Remarks NVARCHAR(200),                     -- 备注
    CONSTRAINT FK_Attendance_Student FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),      -- 用户编号
    Username NVARCHAR(50) NOT NULL UNIQUE,    -- 用户名
    PasswordHash NVARCHAR(255) NOT NULL,      -- 加密的密码
    Role NVARCHAR(20) CHECK (Role IN ('Admin', 'Teacher', 'Student')) -- 用户角色
);

INSERT INTO Students (Name, Gender, DateOfBirth, Major, EnrollmentDate, Contact)
VALUES
('张三', 'M', '2002-05-12', '计算机科学', '2020-09-01', '123456789'),
('李四', 'F', '2003-08-21', '信息管理', '2021-09-01', '987654321');

INSERT INTO Courses (CourseName, Credits, Instructor)
VALUES
('数据库系统', 3, '王老师'),
('操作系统', 4, '李老师');

INSERT INTO Grades (StudentID, CourseID, Score, GradeDate)
VALUES
(1, 1, 85.5, '2023-06-15'),
(2, 2, 90.0, '2023-06-15');

INSERT INTO Attendance (StudentID, AttendanceDate, Status, Remarks)
VALUES
(1, '2023-12-01', 'Present', '按时到达'),
(2, '2023-12-01', 'Late', '迟到5分钟');

INSERT INTO Users (Username, PasswordHash, Role)
VALUES
('admin', 'hashed_password_1', 'Admin'),
('teacher1', 'hashed_password_2', 'Teacher'),
('student1', 'hashed_password_3', 'Student');

-- 用户视图
CREATE VIEW StudentGrades AS
SELECT 
    S.StudentID,
    S.Name AS StudentName,
    C.CourseName,
    G.Score,
    G.GradeDate
FROM 
    Grades G
INNER JOIN Students S ON G.StudentID = S.StudentID
INNER JOIN Courses C ON G.CourseID = C.CourseID;

-- 存储过程 添加学生信息
CREATE PROCEDURE AddStudent
    @Name NVARCHAR(50),
    @Gender CHAR(1),
    @DateOfBirth DATE,
    @Major NVARCHAR(50),
    @EnrollmentDate DATE,
    @Contact NVARCHAR(20)
AS
BEGIN
    INSERT INTO Students (Name, Gender, DateOfBirth, Major, EnrollmentDate, Contact)
    VALUES (@Name, @Gender, @DateOfBirth, @Major, @EnrollmentDate, @Contact);
END;

