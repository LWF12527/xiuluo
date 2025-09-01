DROP DATABASE if EXISTS entrepreneurship_management;
CREATE DATABASE if not EXISTS entrepreneurship_management;
use entrepreneurship_management;

-- 创建项目等级表
CREATE TABLE project_levels (
  level_id INT PRIMARY KEY,
  level_name VARCHAR(50)
);

-- 创建项目类型表
CREATE TABLE project_types (
  type_id INT PRIMARY KEY,
  type_name VARCHAR(50)
);

-- 创建项目信息表
CREATE TABLE project_info (
  project_id INT PRIMARY KEY,
  project_name VARCHAR(100),
  level_id INT,
  type_id INT,
  start_date DATE,
  leader VARCHAR(50),
  participants VARCHAR(255),
  budget DECIMAL(10, 2),
  proposal TEXT,
  FOREIGN KEY (level_id) REFERENCES project_levels(level_id),
  FOREIGN KEY (type_id) REFERENCES project_types(type_id)
);

-- 创建过程管理表
CREATE TABLE process_management (
  project_id INT,
  expenditure DECIMAL(10, 2),
  mid_term_check VARCHAR(50),
  final_status VARCHAR(50),
  FOREIGN KEY (project_id) REFERENCES project_info(project_id)
);


-- 插入项目等级表数据
INSERT INTO project_levels (level_id, level_name)
VALUES
(1, '重要'),
(2, '一般'),
(3, '紧急'),
(4, '普通'),
(5, '特殊');

-- 插入项目类型表数据
INSERT INTO project_types (type_id, type_name)
VALUES
(1, '科研项目'),
(2, '社会实践'),
(3, '创业项目'),
(4, '志愿服务'),
(5, '文化艺术');

-- 插入项目信息表数据
INSERT INTO project_info (project_id, project_name, level_id, type_id, start_date, leader, participants, budget, proposal)
VALUES
(1, '科研项目A', 1, 1, '2023-01-01', '张三', '李四,王五', 10000.00, '项目A的研究内容和目标...'),
(2, '社会实践项目B', 2, 2, '2023-02-01', '李四', '张三,王五', 8000.00, '项目B的实践地点和计划...'),
(3, '创业项目C', 3, 3, '2023-03-01', '王五', '张三,李四', 12000.00, '项目C的商业模式和发展...'),
(4, '志愿服务项目D', 4, 4, '2023-04-01', '赵六', '张三,李四,王五', 6000.00, '项目D的服务对象和计划...'),
(5, '文化艺术项目E', 5, 5, '2023-05-01', '钱七', '张三,李四,王五', 15000.00, '项目E的艺术形式和展示...');

-- 插入过程管理表数据
INSERT INTO process_management (project_id, expenditure, mid_term_check, final_status)
VALUES
(1, 8000.00, '中期检查合格', '已完成'),
(2, 5000.00, '中期检查不合格', '进行中'),
(3, 10000.00, '中期检查合格', '已完成'),
(4, 3000.00, '中期检查不合格', '进行中'),
(5, 12000.00, '中期检查合格', '已完成');
