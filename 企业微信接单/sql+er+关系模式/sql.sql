-- 创建学生数据库

drop database if exists student;
create database if not exists student;
use student;
-- 创建学生信息表
CREATE TABLE students (
                          id INT(11) NOT NULL AUTO_INCREMENT COMMENT '学生ID',
                          name VARCHAR(50) NOT NULL COMMENT '学生姓名',
                          gender VARCHAR(10) NOT NULL COMMENT '学生性别',
                          age INT(11) NOT NULL COMMENT '学生年龄',
                          phone VARCHAR(20) NOT NULL COMMENT '学生电话',
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '学生信息表';

-- 添加学生信息
INSERT INTO `students` (`name`, `gender`, `age`, `phone`) VALUES
                                                              ('张三', '男', 20, '13800123456'),
                                                              ('李四', '女', 19, '13900123456'),
                                                              ('王五', '男', 21, '13600123456'),
                                                              ('赵六', '女', 20, '13700123456'),
                                                              ('刘七', '男', 22, '13500123456');


-- 修改学生信息
UPDATE `students` SET `name`='李四', `gender`='女', `age`=21, `phone`='13900139000' WHERE `id`=1;

-- 查询学生信息
SELECT * FROM `students`;


-- 创建课程信息表
CREATE TABLE courses (
                         id INT(11) NOT NULL AUTO_INCREMENT COMMENT '课程ID',
                         name VARCHAR(50) NOT NULL COMMENT '课程名称',
                         teacher VARCHAR(50) NOT NULL COMMENT '授课教师',
                         credit INT(11) NOT NULL COMMENT '学分',
                         PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '课程信息表';


-- 插入课程信息
INSERT INTO `courses` (`name`, `teacher`, `credit`) VALUES
                                                        ('高等数学', '张老师', 4),
                                                        ('线性代数', '李老师', 3),
                                                        ('离散数学', '王老师', 3),
                                                        ('计算机组成原理', '赵老师', 4),
                                                        ('操作系统', '刘老师', 4);

-- 修改课程信息
UPDATE `courses` SET `name`='线性代数', `teacher`='李老师', `credit`=3 WHERE `id`=1;

-- 查询课程信息
SELECT * FROM `courses`;


-- 创建成绩表
CREATE TABLE scores (
                        id INT(11) NOT NULL AUTO_INCREMENT COMMENT '成绩ID',
                        student_id INT(11) NOT NULL COMMENT '学生ID',
                        course_id INT(11) NOT NULL COMMENT '课程ID',
                        score INT(11) NOT NULL COMMENT '成绩',
                        PRIMARY KEY (id),
                        FOREIGN KEY (student_id) REFERENCES students(id),
                        FOREIGN KEY (course_id) REFERENCES courses(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '成绩表';

-- 添加成绩信息
-- 插入成绩信息
INSERT INTO `scores` (`student_id`, `course_id`, `score`) VALUES
                                                              (1, 1, 80),
                                                              (1, 2, 90),
                                                              (2, 1, 85),
                                                              (2, 3, 78),
                                                              (3, 2, 92),
                                                              (3, 4, 88),
                                                              (4, 1, 76),
                                                              (4, 3, 82),
                                                              (5, 2, 70),
                                                              (5, 4, 90);


-- 修改成绩信息
UPDATE `scores` SET `score`=90 WHERE `id`=1;

-- 查询学生的成绩信息
SELECT `students`.`name`, `courses`.`name`, `scores`.`score` FROM `scores`
                                                                      INNER JOIN `students` ON `scores`.`student_id`=`students`.`id`
                                                                      INNER JOIN `courses` ON `scores`.`course_id`=`courses`.`id`
WHERE `students`.`name`='张三';

-- 查询课程的成绩信息
SELECT `students`.`name`, `courses`.`name`, `scores`.`score` FROM `scores`
                                                                      INNER JOIN `students` ON `scores`.`student_id`=`students`.`id`
                                                                      INNER JOIN `courses` ON `scores`.`course_id`=`courses`.`id`
WHERE `courses`.`name`='高等数学';

-- 查询所有学生的成绩信息
SELECT `students`.`name`, `courses`.`name`, `scores`.`score` FROM `scores`
                                                                      INNER JOIN `students` ON `scores`.`student_id`=`students`.`id`
                                                                      INNER JOIN `courses` ON `scores`.`course_id`=`courses`.`id`;

-- 统计学生的平均成绩和排名
SELECT `students`.`name`, AVG(`scores`.`score`) AS `avg_score`,
       (SELECT COUNT(*)+1 FROM (SELECT AVG(`score`) AS `avg_score` FROM `scores` GROUP BY `student_id`) AS `temp` WHERE `temp`.`avg_score` > AVG(`scores`.`score`)) AS `rank`
FROM `scores`
         INNER JOIN `students` ON `scores`.`student_id`=`students`.`id`
GROUP BY `student_id`
ORDER BY `avg_score` DESC;

-- 生成学生成绩报告单
SELECT `students`.`name`, `courses`.`name`, `scores`.`score`,
       CASE
           WHEN `scores`.`score` >= 90 THEN 4.0
           WHEN `scores`.`score` >= 85 THEN 3.7
           WHEN `scores`.`score` >= 82 THEN 3.3
           WHEN `scores`.`score` >= 78 THEN 3.0
           WHEN `scores`.`score` >= 75 THEN 2.7
           WHEN `scores`.`score` >= 72 THEN 2.3
           WHEN `scores`.`score` >= 68 THEN 2.0
           WHEN `scores`.`score` >= 64 THEN 1.5
           WHEN `scores`.`score` >= 60 THEN 1.0
           ELSE 0
           END AS `grade_point`
FROM `scores`
         INNER JOIN `students` ON `scores`.`student_id`=`students`.`id`
         INNER JOIN `courses` ON `scores`.`course_id`=`courses`.`id`