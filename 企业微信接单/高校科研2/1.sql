-- 创建数据库
CREATE DATABASE ResearchManagementSystem;
GO

USE ResearchManagementSystem;
GO

-- 创建部门表
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY IDENTITY(1,1), -- 部门编号
    DepartmentName NVARCHAR(100) NOT NULL      -- 部门名称
);

-- 创建职务与职称表
CREATE TABLE Positions (
    PositionID INT PRIMARY KEY IDENTITY(1,1), -- 职务/职称编号
    PositionName NVARCHAR(100) NOT NULL      -- 职务/职称名称
);

-- 创建教师信息表
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY IDENTITY(1,1),   -- 教师编号
    TeacherName NVARCHAR(100) NOT NULL,       -- 教师姓名
    DepartmentID INT NOT NULL,                -- 所属部门编号
    PositionID INT NOT NULL,                  -- 职务/职称编号
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID), -- 外键关联部门表
    FOREIGN KEY (PositionID) REFERENCES Positions(PositionID)        -- 外键关联职务表
);

-- 创建科研项目信息表
CREATE TABLE ResearchProjects (
    ProjectID INT PRIMARY KEY IDENTITY(1,1),  -- 项目编号
    ProjectName NVARCHAR(200) NOT NULL,      -- 项目名称
    TeacherID INT NOT NULL,                  -- 负责人教师编号
    DepartmentID INT NOT NULL,               -- 所属部门编号
    Status NVARCHAR(50) DEFAULT '未验收',     -- 验收标志，默认为“未验收”
    SubmissionDate DATE NOT NULL,            -- 申报日期
    ApprovalDate DATE,                       -- 审批日期
    AcceptanceDate DATE,                     -- 验收日期
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID), -- 外键关联教师表
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)  -- 外键关联部门表
);

-- 插入默认值到 Positions 表
INSERT INTO Positions (PositionName)
VALUES ('教授'), ('副教授'), ('讲师'), ('助教');

-- 插入默认值到 Departments 表
INSERT INTO Departments (DepartmentName)
VALUES ('计算机学院'), ('电子信息学院'), ('机械工程学院');

-- 创建触发器：项目验收后，自动更新验收标志为“验收通过”
CREATE TRIGGER trg_UpdateAcceptanceStatus
ON ResearchProjects
AFTER UPDATE
AS
BEGIN
    IF UPDATE(AcceptanceDate) -- 如果更新了验收日期
    BEGIN
        UPDATE ResearchProjects
        SET Status = '验收通过'
        WHERE AcceptanceDate IS NOT NULL AND Status = '未验收';
    END
END;

-- 创建存储过程：统计每个院系科研项目的申报和完成数量
CREATE PROCEDURE usp_GetResearchProjectStats
AS
BEGIN
    SELECT 
        d.DepartmentName AS 院系名称,
        COUNT(CASE WHEN rp.Status = '未验收' THEN 1 END) AS 未完成项目数,
        COUNT(CASE WHEN rp.Status = '验收通过' THEN 1 END) AS 完成项目数
    FROM Departments d
    LEFT JOIN ResearchProjects rp ON d.DepartmentID = rp.DepartmentID
    GROUP BY d.DepartmentName;
END;

-- 示例：调用存储过程
EXEC usp_GetResearchProjectStats;

-- 测试数据插入
-- 插入教师信息
INSERT INTO Teachers (TeacherName, DepartmentID, PositionID)
VALUES 
('张三', 1, 1),
('李四', 2, 2),
('王五', 3, 3);

-- 插入科研项目信息
INSERT INTO ResearchProjects (ProjectName, TeacherID, DepartmentID, SubmissionDate)
VALUES
('人工智能研究', 1, 1, '2024-01-01'),
('大数据分析', 2, 2, '2024-02-01'),
('机器人开发', 3, 3, '2024-03-01');

-- 示例：更新验收日期
UPDATE ResearchProjects
SET AcceptanceDate = '2024-06-01'
WHERE ProjectID = 1;

-- 示例：查看科研项目表
SELECT * FROM ResearchProjects;

-- 示例：调用统计存储过程
EXEC usp_GetResearchProjectStats;

INSERT INTO Departments (DepartmentName)
VALUES 
('计算机学院'),
('电子信息学院'),
('机械工程学院'),
('土木工程学院'),
('管理学院'),
('经济学院'),
('化学学院'),
('法学院'),
('外国语学院'),
('医学院');

INSERT INTO Positions (PositionName)
VALUES 
('教授'),
('副教授'),
('讲师'),
('助教'),
('研究员'),
('高级工程师'),
('工程师'),
('助理研究员'),
('博士后'),
('实习教师');

INSERT INTO Teachers (TeacherName, DepartmentID, PositionID)
VALUES 
('张三', 1, 1),
('李四', 2, 2),
('王五', 3, 3),
('赵六', 4, 4),
('孙七', 5, 5),
('周八', 6, 6),
('吴九', 7, 7),
('郑十', 8, 8),
('王十一', 9, 9),
('冯十二', 10, 10);

INSERT INTO ResearchProjects (ProjectName, TeacherID, DepartmentID, SubmissionDate)
VALUES 
('人工智能研究', 1, 1, '2024-01-01'),
('大数据分析', 2, 2, '2024-02-01'),
('机器人开发', 3, 3, '2024-03-01'),
('土木工程优化', 4, 4, '2024-04-01'),
('供应链管理', 5, 5, '2024-05-01'),
('区域经济研究', 6, 6, '2024-06-01'),
('新型化学材料', 7, 7, '2024-07-01'),
('刑法案例分析', 8, 8, '2024-08-01'),
('语言翻译技术', 9, 9, '2024-09-01'),
('癌症基因研究', 10, 10, '2024-10-01');

