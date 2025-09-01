CREATE DATABASE IF NOT EXISTS  STU;

USE STU;
-- 创建院系表
CREATE TABLE departments (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(50)
);

-- 创建专业表
CREATE TABLE majors (
  major_id INT PRIMARY KEY,
  major_name VARCHAR(50),
  department_id INT,
  FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 创建班级表
CREATE TABLE classes (
  class_id INT PRIMARY KEY,
  class_name VARCHAR(50),
  department_id INT,
  FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 创建课程表
CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(50)
);

-- 创建学生表
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  gender ENUM('男', '女'),
  class_id INT,
  major_id INT,
  FOREIGN KEY (class_id) REFERENCES classes(class_id),
  FOREIGN KEY (major_id) REFERENCES majors(major_id)
);

-- 创建成绩表
CREATE TABLE scores (
  score_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  score DECIMAL(5, 2),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- 创建奖惩信息表
CREATE TABLE rewards_punishments (
  rp_id INT PRIMARY KEY,
  student_id INT,
  description VARCHAR(100),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 创建视图，查询学生信息
CREATE VIEW student_info AS
SELECT s.student_id, s.name, c.class_name, m.major_name, d.department_name
FROM students s
JOIN classes c ON s.class_id = c.class_id
JOIN majors m ON s.major_id = m.major_id
JOIN departments d ON m.department_id = d.department_id;

-- 创建存储过程，查询指定学生的成绩单
DELIMITER //
CREATE PROCEDURE get_student_scores(IN student_id INT)
BEGIN
  SELECT s.name, c.course_name, sc.score
  FROM students s
  JOIN scores sc ON s.student_id = sc.student_id
  JOIN courses c ON sc.course_id = c.course_id
  WHERE s.student_id = student_id;
END //
DELIMITER ;

-- 创建触发器，自动修改班级学生人数
DELIMITER //
CREATE TRIGGER update_class_student_count_insert
AFTER INSERT ON students
FOR EACH ROW
BEGIN
  UPDATE classes
  SET student_count = student_count + 1
  WHERE class_id = NEW.class_id;
END //
DELIMITER ;

-- 创建触发器，自动修改班级学生人数
DELIMITER //
CREATE TRIGGER update_class_student_count_delete
AFTER DELETE ON students
FOR EACH ROW
BEGIN
  UPDATE classes
  SET student_count = student_count - 1
  WHERE class_id = OLD.class_id;
END //
DELIMITER ;

-- 创建触发器，自动修改班级学生人数
DELIMITER //
CREATE TRIGGER update_class_student_count_update
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
  IF OLD.class_id != NEW.class_id THEN
    UPDATE classes
    SET student_count = student_count - 1
    WHERE class_id = OLD.class_id;
    
    UPDATE classes
    SET student_count = student_count + 1
    WHERE class_id = NEW.class_id;
  END IF;
END //
DELIMITER ;

-- 建立参照完整性约束
ALTER TABLE students
ADD CONSTRAINT fk_class_id
FOREIGN KEY (class_id) REFERENCES classes(class_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE students
ADD CONSTRAINT fk_major_id
FOREIGN KEY (major_id) REFERENCES majors(major_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE classes
ADD CONSTRAINT fk_department_id
FOREIGN KEY (department_id) REFERENCES departments(department_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE majors
ADD CONSTRAINT fk_department_id
FOREIGN KEY (department_id) REFERENCES departments(department_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE scores
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id) REFERENCES students(student_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE scores
ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id) REFERENCES courses(course_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE rewards_punishments
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id) REFERENCES students(student_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
