-- 1. 创建数据库
CREATE DATABASE ResearchManagement;
GO

USE ResearchManagement;
GO

-- 2. 创建基础信息表（部门、职务、职称）
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY IDENTITY(1,1),
    DepartmentName NVARCHAR(100) NOT NULL
);

CREATE TABLE Position (
    PositionID INT PRIMARY KEY IDENTITY(1,1),
    PositionName NVARCHAR(100) NOT NULL
);

CREATE TABLE Title (
    TitleID INT PRIMARY KEY IDENTITY(1,1),
    TitleName NVARCHAR(100) NOT NULL
);

-- 3. 创建教师信息表
CREATE TABLE Teacher (
    TeacherID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL,
    DepartmentID INT FOREIGN KEY REFERENCES Department(DepartmentID),
    PositionID INT FOREIGN KEY REFERENCES Position(PositionID),
    TitleID INT FOREIGN KEY REFERENCES Title(TitleID)
);

-- 4. 创建科研项目表
CREATE TABLE ResearchProject (
    ProjectID INT PRIMARY KEY IDENTITY(1,1),
    ProjectName NVARCHAR(200) NOT NULL,
    TeacherID INT FOREIGN KEY REFERENCES Teacher(TeacherID),
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status NVARCHAR(50) DEFAULT '未验收', -- 默认值为未验收
    ApprovalStatus NVARCHAR(50) DEFAULT '未审批'
);

-- 5. 创建科研项目验收触发器
CREATE TRIGGER trg_UpdateProjectStatus
ON ResearchProject
AFTER UPDATE
AS
BEGIN
    IF UPDATE(Status)
    BEGIN
        UPDATE ResearchProject
        SET Status = '验收通过'
        WHERE Status = '验收中';
    END
END;
GO

-- 6. 创建存储过程：统计各院系科研项目的申报和完成数量
CREATE PROCEDURE sp_DeptProjectStats
AS
BEGIN
    SELECT d.DepartmentName,
           COUNT(CASE WHEN r.Status = '未验收' THEN 1 END) AS TotalSubmittedProjects,
           COUNT(CASE WHEN r.Status = '验收通过' THEN 1 END) AS TotalCompletedProjects
    FROM Department d
    LEFT JOIN Teacher t ON d.DepartmentID = t.DepartmentID
    LEFT JOIN ResearchProject r ON t.TeacherID = r.TeacherID
    GROUP BY d.DepartmentName;
END;
GO

-- 7. 插入示例数据
INSERT INTO Department (DepartmentName) VALUES ('计算机科学学院'), ('机械工程学院'), ('电子信息学院'), ('土木工程学院'), ('化学工程学院'), ('物理学院'), ('数学学院'), ('生命科学学院'), ('经济管理学院'), ('艺术学院');
INSERT INTO Position (PositionName) VALUES ('讲师'), ('副教授'), ('教授'), ('助理'), ('高级工程师'), ('主任'), ('副主任'), ('实验员'), ('助理教授'), ('研究员');
INSERT INTO Title (TitleName) VALUES ('助理研究员'), ('研究员'), ('高级研究员'), ('学科带头人'), ('实验技术专家'), ('副研究员'), ('博士后'), ('访问学者'), ('兼职教授'), ('特聘教授');

INSERT INTO Teacher (Name, DepartmentID, PositionID, TitleID) 
VALUES ('张三', 1, 1, 1), ('李四', 2, 2, 2), ('王五', 3, 3, 1), ('赵六', 4, 4, 3), ('孙七', 5, 5, 4), ('周八', 6, 6, 5), ('吴九', 7, 7, 6), ('郑十', 8, 8, 7), ('王小明', 9, 9, 8), ('李小华', 10, 10, 9);

INSERT INTO ResearchProject (ProjectName, TeacherID, StartDate, Status)
VALUES ('人工智能研究', 1, '2024-01-01', '未验收'),
       ('机械自动化项目', 2, '2023-06-01', '未验收'),
       ('物联网开发项目', 3, '2022-08-01', '验收中'),
       ('土木结构稳定性研究', 4, '2023-03-15', '未验收'),
       ('有机合成化学研究', 5, '2022-09-20', '未验收'),
       ('量子物理实验项目', 6, '2023-11-11', '验收中'),
       ('数学建模应用研究', 7, '2024-04-01', '未验收'),
       ('生物多样性保护研究', 8, '2023-05-10', '未验收'),
       ('经济发展与政策分析', 9, '2022-06-30', '未验收'),
       ('艺术设计创新项目', 10, '2024-02-15', '未验收');

-- 8. 创建视图，显示教师及其所属部门的科研项目
CREATE VIEW vw_TeacherProjects AS
SELECT t.TeacherID, t.Name AS 教师姓名, d.DepartmentName AS 所属部门, rp.ProjectName AS 科研项目名称, rp.Status AS 项目状态
FROM Teacher t
INNER JOIN Department d ON t.DepartmentID = d.DepartmentID
LEFT JOIN ResearchProject rp ON t.TeacherID = rp.TeacherID;

-- 9. 调用视图并打印结果
SELECT * FROM vw_TeacherProjects;

-- 10. 执行存储过程
EXEC sp_DeptProjectStats;
