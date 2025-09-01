/*
 Navicat Premium Data Transfer

 Source Server         : examxx
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : examxx

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 05/05/2023 08:43:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

create database examxx;
use examxx;
-- ----------------------------
-- Table structure for et_comment
-- ----------------------------
DROP TABLE IF EXISTS `et_comment`;
CREATE TABLE `et_comment`  (
  `comment_id` int(0) NOT NULL AUTO_INCREMENT,
  `question_id` int(0) NOT NULL,
  `index_id` int(0) NOT NULL,
  `user_id` int(0) NOT NULL,
  `content_msg` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `quoto_id` int(0) NOT NULL DEFAULT 0,
  `re_id` int(0) NOT NULL DEFAULT 0,
  `create_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`comment_id`) USING BTREE,
  INDEX `fk_q_id`(`question_id`) USING BTREE,
  INDEX `fk_u_id`(`user_id`) USING BTREE,
  CONSTRAINT `fk_q_id` FOREIGN KEY (`question_id`) REFERENCES `et_question` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_u_id` FOREIGN KEY (`user_id`) REFERENCES `et_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_comment
-- ----------------------------

-- ----------------------------
-- Table structure for et_exam_paper
-- ----------------------------
DROP TABLE IF EXISTS `et_exam_paper`;
CREATE TABLE `et_exam_paper`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `duration` int(0) NOT NULL COMMENT '试卷考试时间',
  `total_point` int(0) NULL DEFAULT 0,
  `pass_point` int(0) NULL DEFAULT 0,
  `group_id` int(0) NOT NULL COMMENT '班组ID',
  `is_visible` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否所有用户可见，默认为0',
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '试卷状态， 0未完成 -> 1已完成 -> 2已发布 -> 3通过审核 （已发布和通过审核的无法再修改）',
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `summary` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '试卷介绍',
  `is_subjective` tinyint(1) NULL DEFAULT NULL COMMENT '为1表示为包含主观题的试卷，需阅卷',
  `answer_sheet` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '试卷答案，用答题卡的结构保存',
  `creator` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人的账号',
  `paper_type` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '0 真题 1 模拟 2 专家',
  `field_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '试卷' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_exam_paper
-- ----------------------------

-- ----------------------------
-- Table structure for et_field
-- ----------------------------
DROP TABLE IF EXISTS `et_field`;
CREATE TABLE `et_field`  (
  `field_id` int(0) NOT NULL AUTO_INCREMENT,
  `field_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `memo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` decimal(1, 0) NOT NULL DEFAULT 1 COMMENT '1 正常 0 废弃',
  PRIMARY KEY (`field_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_field
-- ----------------------------
INSERT INTO `et_field` VALUES (1, '计算机科学与技术', '计算机科学与技术', 1);

-- ----------------------------
-- Table structure for et_group
-- ----------------------------
DROP TABLE IF EXISTS `et_group`;
CREATE TABLE `et_group`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `group_level_id` int(0) NOT NULL COMMENT '班组级别',
  `parent` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `group_level_id`(`group_level_id`) USING BTREE,
  INDEX `parent`(`parent`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班组' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_group
-- ----------------------------

-- ----------------------------
-- Table structure for et_knowledge_point
-- ----------------------------
DROP TABLE IF EXISTS `et_knowledge_point`;
CREATE TABLE `et_knowledge_point`  (
  `point_id` int(0) NOT NULL AUTO_INCREMENT,
  `point_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `field_id` int(0) NOT NULL,
  `memo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` decimal(1, 0) NULL DEFAULT 1 COMMENT '1:正常 0：废弃',
  PRIMARY KEY (`point_id`) USING BTREE,
  INDEX `fk_knowledge_field`(`field_id`) USING BTREE,
  CONSTRAINT `et_knowledge_point_ibfk_1` FOREIGN KEY (`field_id`) REFERENCES `et_field` (`field_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_knowledge_point
-- ----------------------------
INSERT INTO `et_knowledge_point` VALUES (1, '前端', 1, '前端', 1);
INSERT INTO `et_knowledge_point` VALUES (2, '后端', 1, '后端', 1);
INSERT INTO `et_knowledge_point` VALUES (3, '算法', 1, '算法', 1);
INSERT INTO `et_knowledge_point` VALUES (4, 'AI', 1, 'AI', 1);

-- ----------------------------
-- Table structure for et_news
-- ----------------------------
DROP TABLE IF EXISTS `et_news`;
CREATE TABLE `et_news`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `titile` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` int(0) NOT NULL COMMENT '创建人',
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `is_expire` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否过期',
  `type` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0 新闻， 1 系统信息',
  `group_id` int(0) NOT NULL DEFAULT -1 COMMENT '此系统属于哪个组',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `et_news_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `et_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_news
-- ----------------------------

-- ----------------------------
-- Table structure for et_practice_paper
-- ----------------------------
DROP TABLE IF EXISTS `et_practice_paper`;
CREATE TABLE `et_practice_paper`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `duration` int(0) NOT NULL COMMENT '试卷考试时间',
  `total_point` int(0) NULL DEFAULT 0,
  `pass_point` int(0) NULL DEFAULT 0,
  `group_id` int(0) NOT NULL COMMENT '班组ID',
  `is_visible` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否所有用户可见，默认为0',
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '试卷状态， 0未完成 -> 1已完成 -> 2已发布 -> 3通过审核 （已发布和通过审核的无法再修改）',
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `summary` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '试卷介绍',
  `is_subjective` tinyint(1) NULL DEFAULT NULL COMMENT '为1表示为包含主观题的试卷，需阅卷',
  `answer_sheet` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '试卷答案，用答题卡的结构保存',
  `creator` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人的账号',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '试卷' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_practice_paper
-- ----------------------------

-- ----------------------------
-- Table structure for et_question
-- ----------------------------
DROP TABLE IF EXISTS `et_question`;
CREATE TABLE `et_question`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `question_type_id` int(0) NOT NULL COMMENT '题型',
  `duration` int(0) NULL DEFAULT NULL COMMENT '试题考试时间',
  `points` int(0) NULL DEFAULT NULL,
  `group_id` int(0) NULL DEFAULT NULL COMMENT '班组ID',
  `is_visible` tinyint(1) NOT NULL DEFAULT 0 COMMENT '试题可见性',
  `create_time` timestamp(0) NULL DEFAULT NULL,
  `creator` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'admin' COMMENT '创建者',
  `last_modify` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `answer` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expose_times` int(0) NOT NULL DEFAULT 2,
  `right_times` int(0) NOT NULL DEFAULT 1,
  `wrong_times` int(0) NOT NULL DEFAULT 1,
  `difficulty` int(0) NOT NULL DEFAULT 1,
  `analysis` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `reference` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `examing_point` varchar(5000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `keyword` varchar(5000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `question_type_id`(`question_type_id`) USING BTREE,
  INDEX `et_question_ibfk_5`(`creator`) USING BTREE,
  CONSTRAINT `et_question_ibfk_1` FOREIGN KEY (`question_type_id`) REFERENCES `et_question_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '试题' ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for et_question_2_point
-- ----------------------------
DROP TABLE IF EXISTS `et_question_2_point`;
CREATE TABLE `et_question_2_point`  (
  `question_2_point_id` int(0) NOT NULL AUTO_INCREMENT,
  `question_id` int(0) NULL DEFAULT NULL,
  `point_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`question_2_point_id`) USING BTREE,
  INDEX `fk_question_111`(`question_id`) USING BTREE,
  INDEX `fk_point_111`(`point_id`) USING BTREE,
  CONSTRAINT `et_question_2_point_ibfk_1` FOREIGN KEY (`point_id`) REFERENCES `et_knowledge_point` (`point_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `et_question_2_point_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `et_question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 129 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_question_2_point
-- ----------------------------
INSERT INTO `et_question_2_point` VALUES (21, 21, 1);
INSERT INTO `et_question_2_point` VALUES (31, 31, 1);
INSERT INTO `et_question_2_point` VALUES (32, 32, 1);
INSERT INTO `et_question_2_point` VALUES (33, 33, 1);
INSERT INTO `et_question_2_point` VALUES (34, 34, 1);
INSERT INTO `et_question_2_point` VALUES (35, 35, 1);
INSERT INTO `et_question_2_point` VALUES (36, 36, 1);
INSERT INTO `et_question_2_point` VALUES (37, 37, 1);
INSERT INTO `et_question_2_point` VALUES (38, 38, 1);
INSERT INTO `et_question_2_point` VALUES (39, 39, 1);
INSERT INTO `et_question_2_point` VALUES (40, 40, 1);
INSERT INTO `et_question_2_point` VALUES (41, 41, 1);
INSERT INTO `et_question_2_point` VALUES (42, 42, 1);
INSERT INTO `et_question_2_point` VALUES (44, 44, 1);
INSERT INTO `et_question_2_point` VALUES (45, 45, 1);
INSERT INTO `et_question_2_point` VALUES (66, 66, 3);
INSERT INTO `et_question_2_point` VALUES (67, 67, 3);
INSERT INTO `et_question_2_point` VALUES (68, 68, 3);
INSERT INTO `et_question_2_point` VALUES (69, 69, 3);
INSERT INTO `et_question_2_point` VALUES (70, 70, 3);
INSERT INTO `et_question_2_point` VALUES (71, 71, 3);
INSERT INTO `et_question_2_point` VALUES (72, 72, 3);
INSERT INTO `et_question_2_point` VALUES (73, 73, 3);
INSERT INTO `et_question_2_point` VALUES (74, 74, 3);
INSERT INTO `et_question_2_point` VALUES (75, 75, 3);
INSERT INTO `et_question_2_point` VALUES (76, 76, 3);
INSERT INTO `et_question_2_point` VALUES (77, 77, 3);
INSERT INTO `et_question_2_point` VALUES (78, 78, 3);
INSERT INTO `et_question_2_point` VALUES (97, 97, 3);
INSERT INTO `et_question_2_point` VALUES (100, 100, 3);
INSERT INTO `et_question_2_point` VALUES (101, 101, 3);
INSERT INTO `et_question_2_point` VALUES (102, 102, 3);
INSERT INTO `et_question_2_point` VALUES (103, 103, 3);
INSERT INTO `et_question_2_point` VALUES (105, 105, 3);
INSERT INTO `et_question_2_point` VALUES (106, 106, 3);
INSERT INTO `et_question_2_point` VALUES (108, 108, 3);
INSERT INTO `et_question_2_point` VALUES (121, 121, 3);
INSERT INTO `et_question_2_point` VALUES (122, 122, 3);
INSERT INTO `et_question_2_point` VALUES (123, 123, 3);
INSERT INTO `et_question_2_point` VALUES (124, 124, 3);
INSERT INTO `et_question_2_point` VALUES (125, 125, 3);
INSERT INTO `et_question_2_point` VALUES (126, 126, 3);
INSERT INTO `et_question_2_point` VALUES (127, 127, 3);
INSERT INTO `et_question_2_point` VALUES (128, 128, 3);
INSERT INTO `et_question_2_point` VALUES (129, 29, 3);
INSERT INTO `et_question_2_point` VALUES (130, 4, 4);
INSERT INTO `et_question_2_point` VALUES (131, 5, 4);
INSERT INTO `et_question_2_point` VALUES (132, 1, 4);
INSERT INTO `et_question_2_point` VALUES (133, 3, 4);
INSERT INTO `et_question_2_point` VALUES (134, 6, 4);
INSERT INTO `et_question_2_point` VALUES (135, 2, 4);
INSERT INTO `et_question_2_point` VALUES (136, 7, 4);
INSERT INTO `et_question_2_point` VALUES (137, 8, 4);
INSERT INTO `et_question_2_point` VALUES (138, 9, 4);
INSERT INTO `et_question_2_point` VALUES (139, 10, 4);
INSERT INTO `et_question_2_point` VALUES (140, 11, 3);
INSERT INTO `et_question_2_point` VALUES (141, 20, 3);
INSERT INTO `et_question_2_point` VALUES (142, 19, 3);
INSERT INTO `et_question_2_point` VALUES (143, 18, 3);
INSERT INTO `et_question_2_point` VALUES (144, 17, 3);
INSERT INTO `et_question_2_point` VALUES (145, 16, 3);
INSERT INTO `et_question_2_point` VALUES (146, 15, 3);
INSERT INTO `et_question_2_point` VALUES (147, 14, 3);
INSERT INTO `et_question_2_point` VALUES (148, 13, 3);
INSERT INTO `et_question_2_point` VALUES (149, 12, 3);
INSERT INTO `et_question_2_point` VALUES (150, 30, 3);
INSERT INTO `et_question_2_point` VALUES (151, 28, 3);
INSERT INTO `et_question_2_point` VALUES (152, 27, 3);
INSERT INTO `et_question_2_point` VALUES (153, 26, 3);
INSERT INTO `et_question_2_point` VALUES (154, 25, 3);
INSERT INTO `et_question_2_point` VALUES (155, 24, 3);
INSERT INTO `et_question_2_point` VALUES (156, 23, 3);
INSERT INTO `et_question_2_point` VALUES (157, 22, 3);
INSERT INTO `et_question_2_point` VALUES (158, 52, 4);
INSERT INTO `et_question_2_point` VALUES (159, 51, 4);
INSERT INTO `et_question_2_point` VALUES (160, 50, 3);
INSERT INTO `et_question_2_point` VALUES (161, 49, 2);
INSERT INTO `et_question_2_point` VALUES (162, 46, 1);
INSERT INTO `et_question_2_point` VALUES (163, 47, 3);
INSERT INTO `et_question_2_point` VALUES (164, 48, 2);
INSERT INTO `et_question_2_point` VALUES (165, 59, 4);
INSERT INTO `et_question_2_point` VALUES (166, 60, 4);
INSERT INTO `et_question_2_point` VALUES (167, 58, 4);
INSERT INTO `et_question_2_point` VALUES (168, 53, 4);
INSERT INTO `et_question_2_point` VALUES (169, 54, 4);
INSERT INTO `et_question_2_point` VALUES (170, 55, 4);
INSERT INTO `et_question_2_point` VALUES (171, 56, 4);
INSERT INTO `et_question_2_point` VALUES (172, 57, 4);
INSERT INTO `et_question_2_point` VALUES (173, 61, 4);
INSERT INTO `et_question_2_point` VALUES (174, 62, 4);
INSERT INTO `et_question_2_point` VALUES (175, 63, 3);
INSERT INTO `et_question_2_point` VALUES (176, 64, 3);
INSERT INTO `et_question_2_point` VALUES (177, 65, 3);
INSERT INTO `et_question_2_point` VALUES (179, 79, 1);
INSERT INTO `et_question_2_point` VALUES (180, 80, 1);
INSERT INTO `et_question_2_point` VALUES (182, 81, 1);
INSERT INTO `et_question_2_point` VALUES (183, 82, 1);
INSERT INTO `et_question_2_point` VALUES (184, 83, 1);
INSERT INTO `et_question_2_point` VALUES (185, 84, 1);
INSERT INTO `et_question_2_point` VALUES (186, 85, 1);
INSERT INTO `et_question_2_point` VALUES (187, 86, 1);
INSERT INTO `et_question_2_point` VALUES (188, 87, 1);
INSERT INTO `et_question_2_point` VALUES (189, 88, 1);
INSERT INTO `et_question_2_point` VALUES (190, 89, 1);
INSERT INTO `et_question_2_point` VALUES (191, 90, 1);
INSERT INTO `et_question_2_point` VALUES (192, 91, 1);
INSERT INTO `et_question_2_point` VALUES (193, 92, 1);
INSERT INTO `et_question_2_point` VALUES (194, 93, 1);
INSERT INTO `et_question_2_point` VALUES (195, 94, 2);
INSERT INTO `et_question_2_point` VALUES (196, 95, 2);
INSERT INTO `et_question_2_point` VALUES (197, 96, 3);
INSERT INTO `et_question_2_point` VALUES (200, 99, 3);
INSERT INTO `et_question_2_point` VALUES (201, 98, 3);
INSERT INTO `et_question_2_point` VALUES (202, 107, 1);
INSERT INTO `et_question_2_point` VALUES (203, 115, 1);
INSERT INTO `et_question_2_point` VALUES (204, 109, 1);
INSERT INTO `et_question_2_point` VALUES (206, 111, 1);
INSERT INTO `et_question_2_point` VALUES (207, 112, 1);
INSERT INTO `et_question_2_point` VALUES (208, 113, 1);
INSERT INTO `et_question_2_point` VALUES (209, 114, 1);
INSERT INTO `et_question_2_point` VALUES (210, 116, 1);
INSERT INTO `et_question_2_point` VALUES (211, 117, 1);
INSERT INTO `et_question_2_point` VALUES (212, 118, 1);
INSERT INTO `et_question_2_point` VALUES (214, 120, 1);
INSERT INTO `et_question_2_point` VALUES (216, 43, 3);
INSERT INTO `et_question_2_point` VALUES (217, 104, 2);
INSERT INTO `et_question_2_point` VALUES (218, 119, 3);
INSERT INTO `et_question_2_point` VALUES (219, 110, 2);

-- ----------------------------
-- Table structure for et_question_2_tag
-- ----------------------------
DROP TABLE IF EXISTS `et_question_2_tag`;
CREATE TABLE `et_question_2_tag`  (
  `question_tag_id` int(0) NOT NULL AUTO_INCREMENT,
  `question_id` int(0) NOT NULL,
  `tag_id` int(0) NOT NULL,
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `creator` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`question_tag_id`) USING BTREE,
  INDEX `fk_question_tag_tid`(`tag_id`) USING BTREE,
  INDEX `fk_question_tag_qid`(`question_id`) USING BTREE,
  CONSTRAINT `fk_question_tag_qid` FOREIGN KEY (`question_id`) REFERENCES `et_question` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_question_tag_tid` FOREIGN KEY (`tag_id`) REFERENCES `et_tag` (`tag_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_question_2_tag
-- ----------------------------

-- ----------------------------
-- Table structure for et_question_type
-- ----------------------------
DROP TABLE IF EXISTS `et_question_type`;
CREATE TABLE `et_question_type`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `subjective` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '试题类型' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_question_type
-- ----------------------------
INSERT INTO `et_question_type` VALUES (1, '单选题', 0);
INSERT INTO `et_question_type` VALUES (2, '多选题', 0);
INSERT INTO `et_question_type` VALUES (3, '判断题', 0);
INSERT INTO `et_question_type` VALUES (5, '简答题', 1);

-- ----------------------------
-- Table structure for et_r_user_role
-- ----------------------------
DROP TABLE IF EXISTS `et_r_user_role`;
CREATE TABLE `et_r_user_role`  (
  `user_id` int(0) NOT NULL COMMENT '用户ID',
  `role_id` int(0) NOT NULL COMMENT '角色ID',
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `et_r_user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `et_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户_角色 关联表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_r_user_role
-- ----------------------------
INSERT INTO `et_r_user_role` VALUES (4, 1);
INSERT INTO `et_r_user_role` VALUES (5, 3);

-- ----------------------------
-- Table structure for et_reference
-- ----------------------------
DROP TABLE IF EXISTS `et_reference`;
CREATE TABLE `et_reference`  (
  `reference_id` int(0) NOT NULL AUTO_INCREMENT,
  `reference_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` decimal(10, 0) NOT NULL DEFAULT 1 COMMENT '1 正常 0 废弃',
  PRIMARY KEY (`reference_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_reference
-- ----------------------------

-- ----------------------------
-- Table structure for et_role
-- ----------------------------
DROP TABLE IF EXISTS `et_role`;
CREATE TABLE `et_role`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `authority` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '角色表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_role
-- ----------------------------
INSERT INTO `et_role` VALUES (1, 'ROLE_ADMIN', '超级管理员', 'admin');
INSERT INTO `et_role` VALUES (2, 'ROLE_TEACHER', '教师', 'teacher');
INSERT INTO `et_role` VALUES (3, 'ROLE_STUDENT', '学员', 'student');

-- ----------------------------
-- Table structure for et_tag
-- ----------------------------
DROP TABLE IF EXISTS `et_tag`;
CREATE TABLE `et_tag`  (
  `tag_id` int(0) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `creator` int(0) NOT NULL,
  `is_private` tinyint(1) NOT NULL DEFAULT 0,
  `memo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tag_id`) USING BTREE,
  INDEX `fk_tag_creator`(`creator`) USING BTREE,
  CONSTRAINT `fk_tag_creator` FOREIGN KEY (`creator`) REFERENCES `et_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_tag
-- ----------------------------
INSERT INTO `et_tag` VALUES (4, '较难题', '2023-05-04 19:15:13', 4, 0, '错误率较高');
INSERT INTO `et_tag` VALUES (5, '简单题', '2023-05-04 19:15:18', 4, 0, '基本能对的');

-- ----------------------------
-- Table structure for et_user
-- ----------------------------
DROP TABLE IF EXISTS `et_user`;
CREATE TABLE `et_user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'PK',
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '账号',
  `truename` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '真实姓名',
  `password` char(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `add_date` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `expire_date` timestamp(0) NULL DEFAULT NULL,
  `add_by` int(0) NULL DEFAULT NULL COMMENT '创建人',
  `enabled` tinyint(1) NULL DEFAULT 0 COMMENT '激活状态：0-未激活 1-激活',
  `field_id` int(0) NOT NULL,
  `last_login_time` timestamp(0) NULL DEFAULT NULL,
  `login_time` timestamp(0) NULL DEFAULT NULL,
  `province` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `department` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_user
-- ----------------------------
INSERT INTO `et_user` VALUES (4, 'admin', NULL, '260acbffd3c30786febc29d7dd71a9880a811e77', '1@1.1', NULL, '2023-05-05 08:36:48', NULL, NULL, 1, 1, '2023-05-05 08:03:42', '2023-05-05 08:36:49', NULL, '2', '3');
INSERT INTO `et_user` VALUES (5, 'user01', NULL, 'b313c806131f17b53d83d8bfecb5f0f7b68486fb', 'no@no.no', NULL, '2023-05-05 08:26:06', NULL, NULL, 1, 1, NULL, '2023-05-05 08:26:07', NULL, NULL, NULL);

-- ----------------------------
-- Table structure for et_user_exam_history
-- ----------------------------
DROP TABLE IF EXISTS `et_user_exam_history`;
CREATE TABLE `et_user_exam_history`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `exam_paper_id` int(0) NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `answer_sheet` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `duration` int(0) NOT NULL,
  `point_get` float(10, 1) NOT NULL DEFAULT 0.0,
  `submit_time` timestamp(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_user_exam_history
-- ----------------------------

-- ----------------------------
-- Table structure for et_user_question_history_t
-- ----------------------------
DROP TABLE IF EXISTS `et_user_question_history_t`;
CREATE TABLE `et_user_question_history_t`  (
  `user_question_hist_id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `user_question_hist` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `modify_time` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`user_question_hist_id`) USING BTREE,
  UNIQUE INDEX `idx_u_q_hist_userid`(`user_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of et_user_question_history_t
-- ----------------------------

-- ----------------------------
-- Table structure for t_c3p0
-- ----------------------------
DROP TABLE IF EXISTS `t_c3p0`;
CREATE TABLE `t_c3p0`  (
  `a` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_c3p0
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
