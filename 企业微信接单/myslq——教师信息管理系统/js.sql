
-- ### 创建数据库 ###
CREATE DATABASE TeacherInfoManagement;
USE TeacherInfoManagement;

-- ### 创建表 ###
CREATE TABLE Teacher (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender ENUM('Male', 'Female') NOT NULL,
    Department VARCHAR(100),
    HireDate DATE,
    INDEX (Department)
);

CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    TeacherID INT,
    Credits INT,
    INDEX (CourseName),
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID) ON DELETE SET NULL
);

CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    AdvisorID INT,
    Major VARCHAR(100),
    EnrollmentDate DATE,
    FOREIGN KEY (AdvisorID) REFERENCES Teacher(TeacherID) ON DELETE SET NULL
);

-- ### 视图 ###
CREATE VIEW TeacherCourseView AS
SELECT 
    Teacher.TeacherID, 
    Teacher.Name AS TeacherName, 
    Course.CourseName, 
    Course.Credits
FROM 
    Teacher
LEFT JOIN 
    Course ON Teacher.TeacherID = Course.TeacherID;

-- ### 存储过程 ###
DELIMITER //
CREATE PROCEDURE AddTeacher (
    IN p_Name VARCHAR(100),
    IN p_Gender ENUM('Male', 'Female'),
    IN p_Department VARCHAR(100),
    IN p_HireDate DATE
)
BEGIN
    INSERT INTO Teacher (Name, Gender, Department, HireDate)
    VALUES (p_Name, p_Gender, p_Department, p_HireDate);
END //
DELIMITER ;

-- ### 触发器 ###
DELIMITER //
CREATE TRIGGER UpdateCourseCredits AFTER UPDATE ON Course
FOR EACH ROW
BEGIN
    IF NEW.Credits <> OLD.Credits THEN
        INSERT INTO LogTable (Action, ActionDate, Details)
        VALUES ('Update Credits', NOW(), CONCAT('Updated course ', NEW.CourseID, ' credits from ', OLD.Credits, ' to ', NEW.Credits));
    END IF;
END //
DELIMITER ;

-- ### 增、删、改、查操作 ###
-- 插入数据
INSERT INTO Teacher (Name, Gender, Department, HireDate) 
VALUES ('Alice', 'Female', 'Mathematics', '2020-08-15');

INSERT INTO Course (CourseName, TeacherID, Credits) 
VALUES ('Calculus', 1, 4);

INSERT INTO Student (Name, AdvisorID, Major, EnrollmentDate) 
VALUES ('Bob', 1, 'Engineering', '2021-09-01');

-- 查询数据
SELECT * FROM Teacher;
SELECT * FROM TeacherCourseView;

-- 更新数据
UPDATE Teacher 
SET Department = 'Computer Science' 
WHERE TeacherID = 1;

-- 删除数据
DELETE FROM Student WHERE StudentID = 1;

-- ### 索引优化 ###
-- 对高频查询列添加索引
CREATE INDEX idx_TeacherName ON Teacher(Name);
CREATE INDEX idx_CourseName ON Course(CourseName);

-- 日志表（供触发器使用）
CREATE TABLE LogTable (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    Action VARCHAR(100),
    ActionDate DATETIME,
    Details TEXT
);
