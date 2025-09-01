-- 创建考勤数据库
CREATE DATABASE attendance;

-- 使用考勤数据库
USE attendance;


-- Create Employee table
CREATE TABLE Employee (
  EmployeeID INT AUTO_INCREMENT  PRIMARY KEY,
  Name VARCHAR(50),
  Department VARCHAR(50),
  Position VARCHAR(50)
);

-- Create AttendanceType table
CREATE TABLE AttendanceType (
  AttendanceTypeID INT AUTO_INCREMENT  PRIMARY KEY,
  AttendanceTypeName VARCHAR(50)
);

-- Create Attendance table
CREATE TABLE Attendance (
  AttendanceID INT AUTO_INCREMENT  PRIMARY KEY,
  Date DATE,
  EmployeeID INT,
  AttendanceTypeID INT,
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
  FOREIGN KEY (AttendanceTypeID) REFERENCES AttendanceType(AttendanceTypeID)
);

-- 创建一个视图，显示考勤情况
CREATE VIEW AttendanceView AS
SELECT A.AttendanceID, A.Date, A. AttendanceTypeID, A.EmployeeID, E.Name, E.Department, E.Position
FROM Attendance A
JOIN Employee E ON A.EmployeeID = E.EmployeeID;


-- 创建触发器，在插入员工考勤记录时自动将日期设置为当前日期
CREATE TRIGGER InsertAttendanceDate
BEFORE INSERT ON Attendance
FOR EACH ROW
BEGIN
  SET NEW.Date = CURDATE();
END;

-- 创建一个存储过程，用于根据员工工号查询其考勤记录
CREATE PROCEDURE GetAttendanceByEmployeeID(IN empID INT)
BEGIN
  SELECT *
  FROM Attendance
  WHERE EmployeeID = empID;
END;

	-- 向考勤类型表插入数据
INSERT INTO AttendanceType (AttendanceTypeID, AttendanceTypeName)
VALUES (1, '旷工'), (2, '迟到'), (3, '早退'), (4, '请假');

-- 向 Employee 表插入数据
INSERT INTO Employee (EmployeeID, Name, Department, Position)
VALUES (1, 'John Doe', 'Sales', 'Sales Representative'),
       (2, 'Jane Smith', 'Marketing', 'Marketing Manager'),
       (3, 'Mike Johnson', 'IT', 'IT Specialist'),
       (4, 'Emily Brown', 'Finance', 'Financial Analyst'),
       (5, 'David Lee', 'HR', 'HR Manager');

-- 向 Attendance 表插入数据
INSERT INTO Attendance (AttendanceID, Date, EmployeeID, AttendanceTypeID)
VALUES (1, '2024-01-01', 1, 1),
       (2, '2024-01-02', 2, 2),
       (3, '2024-01-03', 3, 3),
       (4, '2024-01-04', 4, 4),
       (5, '2024-01-05', 5, 1),
       (6, '2024-01-06', 1, 2),
       (7, '2024-01-07', 2, 3),
       (8, '2024-01-08', 3, 4),
       (9, '2024-01-09', 4, 1),
       (10, '2024-01-10', 5, 2);
