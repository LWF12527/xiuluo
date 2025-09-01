/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : stuinfo_db

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 16/12/2024 21:10:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for grade_tb
-- ----------------------------
DROP TABLE IF EXISTS `grade_tb`;
CREATE TABLE `grade_tb`  (
  `ID` int NOT NULL DEFAULT 0,
  `Sid` varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Cnum` int NULL DEFAULT NULL,
  `Tnum` varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `Dgra` float NULL DEFAULT NULL,
  `Egra` float NULL DEFAULT NULL,
  `ALgrade` float NULL DEFAULT NULL,
  `Remarks` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of grade_tb
-- ----------------------------
INSERT INTO `grade_tb` VALUES (1, '20231001', 8801, '2023-1', 85, 88, 86.8, '优秀');
INSERT INTO `grade_tb` VALUES (2, '20231003', 6601, '2023-1', 60, 45, 51, NULL);
INSERT INTO `grade_tb` VALUES (3, '20221002', 8802, '2023-2', 82, 70, 74.8, NULL);
INSERT INTO `grade_tb` VALUES (4, '20231005', 6602, '2202-2', 82, 62, 70, NULL);
INSERT INTO `grade_tb` VALUES (5, '20231005', 7701, '2023-2', 95, 93, 93.8, '优秀');
INSERT INTO `grade_tb` VALUES (6, '20231001', 7702, '2023-2', 89, 85, 86.6, '优秀');
INSERT INTO `grade_tb` VALUES (7, '20231003', 8801, '2023-1', 70, 56, 61.6, NULL);
INSERT INTO `grade_tb` VALUES (8, '20221002', 6601, '2023-1', 45, 76, 63.6, NULL);

-- ----------------------------
-- Table structure for stu_tb
-- ----------------------------
DROP TABLE IF EXISTS `stu_tb`;
CREATE TABLE `stu_tb`  (
  `Sid` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Sname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Ssex` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '男',
  `Sclass` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Sdep` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Snation` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Spolitics` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Sbirthday` date NULL DEFAULT NULL,
  PRIMARY KEY (`Sid`) USING BTREE,
  UNIQUE INDEX `Id_name_index`(`Sid` ASC, `Sname` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu_tb
-- ----------------------------
INSERT INTO `stu_tb` VALUES ('20221002', '张轩', '男', '大数据1班', '信息学院', '汉族', '团员', '2002-01-10');
INSERT INTO `stu_tb` VALUES ('20231001', '刘丽', '女', NULL, '信息学院', '汉族', '团员', '2004-05-03');
INSERT INTO `stu_tb` VALUES ('20231003', '王明伟', '男', '自动化控制1班', '计算机学院', '壮族', NULL, '2003-02-23');
INSERT INTO `stu_tb` VALUES ('20231005', '李澜', '女', '人工智能2班', '信息学院', '壮族', '党员', '2005-08-20');

-- ----------------------------
-- Procedure structure for pro_stu
-- ----------------------------
DROP PROCEDURE IF EXISTS `pro_stu`;
delimiter ;;
CREATE PROCEDURE `pro_stu`()
BEGIN
    SELECT Sid, Sname, Sclass, Sdep
    FROM stu_tb
    WHERE Sdep = '信息学院';
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
