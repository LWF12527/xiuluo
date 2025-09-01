/*
 Navicat Premium Data Transfer

 Source Server         : 1209
 Source Server Type    : MySQL
 Source Server Version : 50562
 Source Host           : localhost:3306
 Source Schema         : score_db

 Target Server Type    : MySQL
 Target Server Version : 50562
 File Encoding         : 65001

 Date: 09/12/2024 09:30:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for grade_tb
-- ----------------------------
DROP TABLE IF EXISTS `grade_tb`;
CREATE TABLE `grade_tb`  (
  `ID` int(11) NOT NULL DEFAULT 0,
  `Sid` varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Cnum` int(6) NULL DEFAULT NULL,
  `Tnum` varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `Dgra` float NULL DEFAULT NULL,
  `Egra` float NULL DEFAULT NULL,
  `ALgrade` float NULL DEFAULT NULL,
  `Remarks` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of grade_tb
-- ----------------------------
INSERT INTO `grade_tb` VALUES (1, '20231001', 8801, '2023-1', 85, 88, NULL, '优秀');
INSERT INTO `grade_tb` VALUES (2, '20231003', 6601, '2023-1', 60, 45, NULL, NULL);
INSERT INTO `grade_tb` VALUES (3, '20221002', 8802, '2023-2', 82, 70, NULL, NULL);
INSERT INTO `grade_tb` VALUES (4, '20231005', 6602, '2202-2', 82, 62, NULL, NULL);
INSERT INTO `grade_tb` VALUES (5, '20231005', 7701, '2023-2', 95, 93, NULL, '优秀');
INSERT INTO `grade_tb` VALUES (6, '20231001', 7702, '2023-2', 89, 85, NULL, '优秀');
INSERT INTO `grade_tb` VALUES (7, '20231003', 8801, '2023-1', 70, 56, NULL, NULL);
INSERT INTO `grade_tb` VALUES (8, '20221002', 6601, '2023-1', 45, 76, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
