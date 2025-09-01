-- 创建数据库
CREATE DATABASE OnlineRecruitmentSystem;
USE OnlineRecruitmentSystem;

-- 创建 Users 表
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role ENUM('求职者', '招聘者') NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- 创建 Jobs 表
CREATE TABLE Jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 创建 Applications 表
CREATE TABLE Applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    job_id INT NOT NULL,
    application_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id)
);

-- SystemLogs 表来存储日志
CREATE TABLE SystemLogs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    log_type VARCHAR(50),
    description TEXT,
    log_date DATETIME
);

-- 插入用户
INSERT INTO Users (username, password, role, email)
VALUES 
('alice', 'password123', '求职者', 'alice@example.com'),
('bob', 'password456', '招聘者', 'bob@example.com');

-- 插入职位
INSERT INTO Jobs (job_title, description, company_name, user_id)
VALUES
('Software Engineer', 'Develop and maintain software solutions.', 'TechCorp', 2),
('Product Manager', 'Lead product development teams.', 'TechCorp', 2);

-- 插入职位申请
INSERT INTO Applications (user_id, job_id, application_date)
VALUES
(1, 1, CURDATE()),
(1, 2, CURDATE());


-- 在 Users 表中添加索引
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);

-- 在 Jobs 表中添加索引
CREATE INDEX idx_job_title ON Jobs(job_title);
CREATE INDEX idx_company_name ON Jobs(company_name);

-- 在 Applications 表中添加索引
CREATE INDEX idx_application_date ON Applications(application_date);
CREATE INDEX idx_user_job ON Applications(user_id, job_id);

-- 求职者视图：查看申请记录及职位详情
CREATE VIEW ApplicantApplications AS
SELECT 
    a.application_id,
    u.username AS applicant_name,
    j.job_title,
    j.company_name,
    a.application_date
FROM Applications a
JOIN Users u ON a.user_id = u.user_id
JOIN Jobs j ON a.job_id = j.job_id
WHERE u.role = '求职者';

-- 招聘者视图：查看职位及申请详情
CREATE VIEW RecruiterJobs AS
SELECT 
    j.job_id,
    j.job_title,
    j.company_name,
    COUNT(a.application_id) AS total_applications
FROM Jobs j
LEFT JOIN Applications a ON j.job_id = a.job_id
GROUP BY j.job_id, j.job_title, j.company_name;

-- 用户视图：展示所有用户信息，隐藏密码
CREATE VIEW UserInfo AS
SELECT 
    user_id,
    username,
    role,
    email
FROM Users;


-- 触发器 1：在用户注册时自动记录时间
CREATE TRIGGER trg_user_registration
AFTER INSERT ON Users
FOR EACH ROW
BEGIN
    INSERT INTO SystemLogs (log_type, description, log_date)
    VALUES ('User Registration', CONCAT('New user registered: ', NEW.username), NOW());
END;

-- 触发器 2：记录职位申请操作
CREATE TRIGGER trg_application_creation
AFTER INSERT ON Applications
FOR EACH ROW
BEGIN
    INSERT INTO SystemLogs (log_type, description, log_date)
    VALUES ('Job Application', 
            CONCAT('User ', NEW.user_id, ' applied for Job ', NEW.job_id), 
            NOW());
END;

-- 触发器 3：禁止删除用户表中的管理员账号
CREATE TRIGGER trg_prevent_admin_deletion
BEFORE DELETE ON Users
FOR EACH ROW
BEGIN
    IF OLD.role = '管理员' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Admin account cannot be deleted.';
    END IF;
END;

-- 存储过程 1：插入职位
DELIMITER $$

CREATE PROCEDURE AddJob(
    IN job_title VARCHAR(100),
    IN description TEXT,
    IN company_name VARCHAR(100),
    IN user_id INT
)
BEGIN
    INSERT INTO Jobs (job_title, description, company_name, user_id)
    VALUES (job_title, description, company_name, user_id);

    -- 添加到日志
    INSERT INTO SystemLogs (log_type, description, log_date)
    VALUES ('Job Creation', CONCAT('Job created by user ID: ', user_id), NOW());
END $$

DELIMITER ;


-- 存储过程 2：统计求职者申请数量
DELIMITER $$

CREATE PROCEDURE GetApplicantStats(
    IN applicant_id INT
)
BEGIN
    SELECT 
        u.username AS applicant_name,
        COUNT(a.application_id) AS total_applications
    FROM Applications a
    JOIN Users u ON a.user_id = u.user_id
    WHERE u.user_id = applicant_id
    GROUP BY u.username;
END $$

DELIMITER ;
