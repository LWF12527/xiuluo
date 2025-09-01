use yg;

-- 创建部门表：
CREATE TABLE department (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);


-- 创建员工表：
CREATE TABLE employee (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  position VARCHAR(50),
  department_id INT,
  salary DECIMAL(10, 2),
  hire_date DATE,
  FOREIGN KEY (department_id) REFERENCES department(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- 向部门表插入数据
INSERT INTO department (id, name)
VALUES
(1, '技术部'),
(2, '销售部'),
(3, '设计部'),
(4, '财务部');

-- 向员工表插入数据
INSERT INTO employee (id, name, age, position, department_id, salary, hire_date)
VALUES
(1, '张三', 28, '经理', 1, 5000.00, '2020-01-01'),
(2, '李四', 25, '助理', 2, 3000.00, '2020-02-15'),
(3, '王五', 30, '工程师', 1, 4000.00, '2020-03-10'),
(4, '赵六', 32, '销售员', 3, 3500.00, '2020-04-20'),
(5, '陈七', 27, '技术支持', 2, 3200.00, '2020-05-05'),
(6, '刘八', 29, '项目经理', 1, 5500.00, '2020-06-12'),
(7, '朱九', 26, '设计师', 3, 3800.00, '2020-07-25'),
(8, '杨十', 31, '财务主管', 4, 4500.00, '2020-08-08'),
(9, '周十一', 24, '人力资源', 4, 3200.00, '2020-09-18'),
(10, '吴十二', 33, '市场专员', 3, 3000.00, '2020-10-30');



-- 创建员工表的索引
CREATE INDEX idx_employee_name ON employee (name);
-- 创建部门表的索引
CREATE INDEX idx_department_name ON department (name);


-- 触发器：在插入新员工时，自动更新部门表中的员工数量。
CREATE TRIGGER update_employee_count
AFTER INSERT ON employee
FOR EACH ROW
BEGIN
    UPDATE department
    SET employee_count = employee_count + 1
    WHERE id = NEW.department_id;
END;

-- 触发器：在更新员工表中的薪水字段时，自动计算并更新员工表中的平均薪水。
CREATE TRIGGER update_average_salary
AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
    DECLARE total_salary DECIMAL(10, 2);
    DECLARE total_employees INT;
    DECLARE average_salary DECIMAL(10, 2);
    
    SELECT SUM(salary) INTO total_salary FROM employee;
    SELECT COUNT(*) INTO total_employees FROM employee;
    
    SET average_salary = total_salary / total_employees;
    
    UPDATE employee
    SET average_salary = average_salary;
END;



-- 创建视图
CREATE VIEW employee_department AS
SELECT e.id, e.name, e.age, e.position, d.name AS department_name, e.salary, e.hire_date
FROM employee e
JOIN department d ON e.department_id = d.id;