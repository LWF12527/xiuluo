SHOW DATABASES;

SHOW CREATE DATABASE stuinfo_db;


USE stuinfo_db;

CREATE TABLE tb_stu (
    Sid VARCHAR(8) PRIMARY KEY,          -- 学号，主键
    Sname VARCHAR(20) NOT NULL,          -- 姓名，不允许为空
    Ssex VARCHAR(2) NOT NULL DEFAULT '男', -- 性别，不允许为空，默认值为‘男’
    Sclass VARCHAR(10),                  -- 班级
    Sdep VARCHAR(20),                    -- 学院
    Snation VARCHAR(20),                 -- 民族
    Spolitics VARCHAR(4),                -- 政治面貌
    Sbirthday DATE                       -- 出生日期
);

USE stuinfo_db;

-- 将 tb_stu 表改名为 stu_tb
RENAME TABLE tb_stu TO stu_tb;

USE stuinfo_db;

-- 在 stu_tb 表中创建唯一索引 Id_name_index
CREATE UNIQUE INDEX Id_name_index ON stu_tb (Sid, Sname);

UPDATE grade_tb
SET ALgrade = (Dgra * 0.4) + (Egra * 0.6);

SELECT Sid, 
       SUM(ALgrade) AS TotalScore, 
       ROUND(AVG(ALgrade), 2) AS AverageScore
FROM grade_tb
GROUP BY Sid;

SELECT g.Sid, s.Sname, s.Sclass, g.Cnum, g.ALgrade
FROM grade_tb g
JOIN stu_tb s ON g.Sid = s.Sid
WHERE g.ALgrade > 85;


DELIMITER $$

CREATE PROCEDURE pro_stu()
BEGIN
    SELECT Sid, Sname, Sclass, Sdep
    FROM stu_tb
    WHERE Sdep = '信息学院';
END $$

DELIMITER ;
