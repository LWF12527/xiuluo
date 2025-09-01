/*
 Navicat Premium Data Transfer

 Source Server         : abc
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : studentmanage

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 16/06/2023 18:46:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 专业表
-- ----------------------------
DROP TABLE IF EXISTS `专业表`;
CREATE TABLE `专业表`  (
  `专业名称` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `学院编号` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`专业名称`) USING BTREE,
  INDEX `学院编号`(`学院编号`) USING BTREE,
  CONSTRAINT `专业表_ibfk_1` FOREIGN KEY (`学院编号`) REFERENCES `学院表` (`学院编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 专业表
-- ----------------------------
INSERT INTO `专业表` VALUES ('电子信息工程', 1);
INSERT INTO `专业表` VALUES ('计算机科学与技术', 1);
INSERT INTO `专业表` VALUES ('化学工程', 2);
INSERT INTO `专业表` VALUES ('机械工程', 2);
INSERT INTO `专业表` VALUES ('英语', 3);

-- ----------------------------
-- Table structure for 学生成绩表
-- ----------------------------
DROP TABLE IF EXISTS `学生成绩表`;
CREATE TABLE `学生成绩表`  (
  `学号` int(0) NOT NULL,
  `课程编号` int(0) NOT NULL,
  `成绩` float NULL DEFAULT NULL,
  `考试次数` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`学号`, `课程编号`) USING BTREE,
  INDEX `课程编号`(`课程编号`) USING BTREE,
  INDEX `I_Dlq01_achievement`(`学号`, `课程编号`) USING BTREE,
  CONSTRAINT `学生成绩表_ibfk_1` FOREIGN KEY (`学号`) REFERENCES `学生档案表` (`学号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `学生成绩表_ibfk_2` FOREIGN KEY (`课程编号`) REFERENCES `课程名表` (`课程编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 学生成绩表
-- ----------------------------
INSERT INTO `学生成绩表` VALUES (1, 1, 80, 1);
INSERT INTO `学生成绩表` VALUES (1, 2, 75, 1);
INSERT INTO `学生成绩表` VALUES (2, 1, 90, 1);
INSERT INTO `学生成绩表` VALUES (2, 2, 85, 1);
INSERT INTO `学生成绩表` VALUES (3, 1, 70, 1);

-- ----------------------------
-- Table structure for 学生档案表
-- ----------------------------
DROP TABLE IF EXISTS `学生档案表`;
CREATE TABLE `学生档案表`  (
  `学号` int(0) NOT NULL,
  `姓名` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `性别` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `出生日期` date NULL DEFAULT NULL,
  `政治面貌` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `班级编号` int(0) NULL DEFAULT NULL,
  `毕业学校` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`学号`) USING BTREE,
  INDEX `班级编号`(`班级编号`) USING BTREE,
  CONSTRAINT `学生档案表_ibfk_1` FOREIGN KEY (`班级编号`) REFERENCES `班级表` (`班级编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 学生档案表
-- ----------------------------
INSERT INTO `学生档案表` VALUES (1, '张三', '男', '2000-01-01', '党员', 1, '高中A');
INSERT INTO `学生档案表` VALUES (2, '李四', '女', '2001-02-03', '团员', 1, '高中B');
INSERT INTO `学生档案表` VALUES (3, '王五', '男', '2002-03-05', '群众', 2, '高中C');
INSERT INTO `学生档案表` VALUES (4, '赵六', '女', '2003-04-07', '党员', 2, '高中D');
INSERT INTO `学生档案表` VALUES (5, '刘七', '男', '2004-05-09', '党员', 3, '高中E');

-- ----------------------------
-- Table structure for 学院表
-- ----------------------------
DROP TABLE IF EXISTS `学院表`;
CREATE TABLE `学院表`  (
  `学院编号` int(0) NOT NULL,
  `学院名` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`学院编号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 学院表
-- ----------------------------
INSERT INTO `学院表` VALUES (1, '计算机与信息学院');
INSERT INTO `学院表` VALUES (2, '工程学院');
INSERT INTO `学院表` VALUES (3, '外语学院');

-- ----------------------------
-- Table structure for 教师表
-- ----------------------------
DROP TABLE IF EXISTS `教师表`;
CREATE TABLE `教师表`  (
  `教师编号` int(0) NOT NULL,
  `课程编号` int(0) NULL DEFAULT NULL,
  `班级编号` int(0) NULL DEFAULT NULL,
  `授课地点` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `职称` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`教师编号`) USING BTREE,
  INDEX `课程编号`(`课程编号`) USING BTREE,
  INDEX `班级编号`(`班级编号`) USING BTREE,
  CONSTRAINT `教师表_ibfk_1` FOREIGN KEY (`课程编号`) REFERENCES `课程名表` (`课程编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `教师表_ibfk_2` FOREIGN KEY (`班级编号`) REFERENCES `班级表` (`班级编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 教师表
-- ----------------------------
INSERT INTO `教师表` VALUES (1, 1, 1, '教室A', '副教授');
INSERT INTO `教师表` VALUES (2, 2, 1, '教室B', '讲师');
INSERT INTO `教师表` VALUES (3, 3, 2, '教室C', '教授');
INSERT INTO `教师表` VALUES (4, 4, 2, '教室D', '副教授');
INSERT INTO `教师表` VALUES (5, 5, 3, '教室E', '讲师');

-- ----------------------------
-- Table structure for 班级表
-- ----------------------------
DROP TABLE IF EXISTS `班级表`;
CREATE TABLE `班级表`  (
  `班级编号` int(0) NOT NULL,
  `班级名称` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `人数` int(0) NULL DEFAULT NULL,
  `专业编号` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`班级编号`) USING BTREE,
  INDEX `专业编号`(`专业编号`) USING BTREE,
  CONSTRAINT `班级表_ibfk_1` FOREIGN KEY (`专业编号`) REFERENCES `专业表` (`专业名称`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 班级表
-- ----------------------------
INSERT INTO `班级表` VALUES (1, '计算机科学与技术1班', 30, '计算机科学与技术');
INSERT INTO `班级表` VALUES (2, '计算机科学与技术2班', 28, '计算机科学与技术');
INSERT INTO `班级表` VALUES (3, '电子信息工程1班', 25, '电子信息工程');
INSERT INTO `班级表` VALUES (4, '电子信息工程2班', 27, '电子信息工程');
INSERT INTO `班级表` VALUES (5, '机械工程1班', 26, '机械工程');

-- ----------------------------
-- Table structure for 课程名表
-- ----------------------------
DROP TABLE IF EXISTS `课程名表`;
CREATE TABLE `课程名表`  (
  `课程编号` int(0) NOT NULL,
  `课程名` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `课程类别` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `学分` float NULL DEFAULT NULL,
  PRIMARY KEY (`课程编号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 课程名表
-- ----------------------------
INSERT INTO `课程名表` VALUES (1, '高等数学', '必修课', 4);
INSERT INTO `课程名表` VALUES (2, '线性代数', '必修课', 3);
INSERT INTO `课程名表` VALUES (3, '物理实验', '选修课', 2);
INSERT INTO `课程名表` VALUES (4, '化学实验', '选修课', 2);
INSERT INTO `课程名表` VALUES (5, '英语口语', '选修课', 2);

-- ----------------------------
-- View structure for graduation_certificate
-- ----------------------------
DROP VIEW IF EXISTS `graduation_certificate`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `graduation_certificate` AS select `s`.`学号` AS `学号`,`s`.`姓名` AS `姓名`,avg(`sc`.`成绩`) AS `平均分`,max(`sc`.`成绩`) AS `最高分`,min(`sc`.`成绩`) AS `最低分`,`c`.`班级名称` AS `班级名称`,`z`.`专业名称` AS `专业名称` from (((`学生档案表` `s` join `学生成绩表` `sc` on((`s`.`学号` = `sc`.`学号`))) join `班级表` `c` on((`s`.`班级编号` = `c`.`班级编号`))) join `专业表` `z` on((`c`.`专业编号` = `z`.`专业名称`))) group by `s`.`学号`,`s`.`姓名`,`c`.`班级名称`,`z`.`专业名称` having (min(`sc`.`成绩`) >= 60);

-- ----------------------------
-- Triggers structure for table 专业表
-- ----------------------------
DROP TRIGGER IF EXISTS `更新班级表专业编号`;
delimiter ;;
CREATE TRIGGER `更新班级表专业编号` AFTER UPDATE ON `专业表` FOR EACH ROW BEGIN
    UPDATE 班级表
    SET 专业编号 = NEW.专业名称
    WHERE 专业编号 = OLD.专业名称;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
