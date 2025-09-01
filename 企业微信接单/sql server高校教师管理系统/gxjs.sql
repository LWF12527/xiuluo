-- 创建数据库
-- CREATE DATABASE gxjs;
-- Use gxjs;

-- 创建教师表
CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender CHAR(1),
    birth_date DATE,
    department VARCHAR(100)
);

-- 创建课程表
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 创建成绩表
CREATE TABLE Grade (
    grade_id INT IDENTITY PRIMARY KEY, -- 使用 IDENTITY 自动生成 grade_id
    teacher_id INT,
    student_id INT,
    course_id INT,
    score DECIMAL(5, 2),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- 创建考勤表
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY,
    teacher_id INT,
    date DATE,
    attendance_status VARCHAR(20),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);
-- 查询某个特定课程的所有教师信息
SELECT T.* 
FROM Teacher T
INNER JOIN Course C ON T.teacher_id = C.teacher_id
WHERE C.course_name = '特定课程名';

-- 插入新教师信息的存储过程
CREATE PROCEDURE InsertTeacher
    @p_teacher_id INT,
    @p_name VARCHAR(100),
    @p_gender CHAR(1),
    @p_birth_date DATE,
    @p_department VARCHAR(100)
AS
BEGIN
    INSERT INTO Teacher (teacher_id, name, gender, birth_date, department)
    VALUES (@p_teacher_id, @p_name, @p_gender, @p_birth_date, @p_department);
END;
GO

-- 更新教师信息的存储过程
CREATE PROCEDURE UpdateTeacher
    @p_teacher_id INT,
    @p_name VARCHAR(100),
    @p_gender CHAR(1),
    @p_birth_date DATE,
    @p_department VARCHAR(100)
AS
BEGIN
    UPDATE Teacher
    SET name = @p_name, 
        gender = @p_gender, 
        birth_date = @p_birth_date, 
        department = @p_department
    WHERE teacher_id = @p_teacher_id;
END;
GO

-- 当教师被删除时，自动将该教师教授的所有课程的教师ID设置为NULL（假设没有教师替代）
CREATE TRIGGER trg_delete_teacher
ON Teacher
AFTER DELETE
AS
BEGIN
    UPDATE Course
    SET teacher_id = NULL
    WHERE teacher_id IN (SELECT deleted.teacher_id FROM deleted);
END;
GO
-- 当成绩被录入时，检查分数是否在合理范围内（例如0到100之间），如果不是，则阻止插入
CREATE TRIGGER trg_check_grade
ON Grade
INSTEAD OF INSERT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM inserted WHERE score < 0 OR score > 100)
    BEGIN
        RAISERROR ('Score must be between 0 and 100', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    -- 如果所有插入的成绩都在合理范围内，则继续执行插入操作
    INSERT INTO Grade (student_id, course_id, score)
    SELECT student_id, course_id, score
    FROM inserted;
END;
GO


-- 插入教师表数据
INSERT INTO Teacher (teacher_id, name, gender, birth_date, department)
VALUES 
(1, '张老师', 'M', '1980-05-12', '计算机科学与技术'),
(2, '李老师', 'F', '1985-08-20', '数学与应用数学'),
(3, '王老师', 'M', '1990-03-15', '电子工程'),
(4, '赵老师', 'F', '1982-11-05', '信息管理与信息系统'),
(5, '钱老师', 'M', '1975-02-25', '物理学');

-- 插入课程表数据
INSERT INTO Course (course_id, course_name, credits, teacher_id)
VALUES 
(1, '数据库原理', 3, 1), 
(2, '高等数学', 4, 2),
(3, '信号与系统', 3, 3),
(4, '管理学基础', 3, 4),
(5, '量子物理', 4, 5);

-- 插入成绩表数据
INSERT INTO Grade (teacher_id, student_id, course_id, score)
VALUES 
(1, 101, 1, 95.5),
(2, 102, 2, 88.0),
(3, 103, 3, 75.5),
(4, 104, 4, 90.0),
(5, 105, 5, 85.0);


-- 插入考勤表数据
INSERT INTO Attendance (attendance_id, teacher_id, date, attendance_status)
VALUES 
(1, 1, '2024-09-01', '出勤'),
(2, 2, '2024-09-02', '缺席'),
(3, 3, '2024-09-03', '迟到'),
(4, 4, '2024-09-04', '出勤'),
(5, 5, '2024-09-05', '出勤');

