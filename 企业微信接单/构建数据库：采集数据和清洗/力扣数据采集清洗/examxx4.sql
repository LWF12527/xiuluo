-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: examxx
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `et_comment`
--

DROP TABLE IF EXISTS `et_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `question_id` int NOT NULL,
  `index_id` int NOT NULL,
  `user_id` int NOT NULL,
  `content_msg` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `quoto_id` int NOT NULL DEFAULT '0',
  `re_id` int NOT NULL DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`) USING BTREE,
  KEY `fk_q_id` (`question_id`) USING BTREE,
  KEY `fk_u_id` (`user_id`) USING BTREE,
  CONSTRAINT `fk_q_id` FOREIGN KEY (`question_id`) REFERENCES `et_question` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_u_id` FOREIGN KEY (`user_id`) REFERENCES `et_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_comment`
--

LOCK TABLES `et_comment` WRITE;
/*!40000 ALTER TABLE `et_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_exam_paper`
--

DROP TABLE IF EXISTS `et_exam_paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_exam_paper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `duration` int NOT NULL COMMENT '试卷考试时间',
  `total_point` int DEFAULT '0',
  `pass_point` int DEFAULT '0',
  `group_id` int NOT NULL COMMENT '班组ID',
  `is_visible` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否所有用户可见，默认为0',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '试卷状态， 0未完成 -> 1已完成 -> 2已发布 -> 3通过审核 （已发布和通过审核的无法再修改）',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `summary` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '试卷介绍',
  `is_subjective` tinyint(1) DEFAULT NULL COMMENT '为1表示为包含主观题的试卷，需阅卷',
  `answer_sheet` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '试卷答案，用答题卡的结构保存',
  `creator` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '创建人的账号',
  `paper_type` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '0 真题 1 模拟 2 专家',
  `field_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `group_id` (`group_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='试卷';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_exam_paper`
--

LOCK TABLES `et_exam_paper` WRITE;
/*!40000 ALTER TABLE `et_exam_paper` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_exam_paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_field`
--

DROP TABLE IF EXISTS `et_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_field` (
  `field_id` int NOT NULL AUTO_INCREMENT,
  `field_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `memo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `state` decimal(1,0) NOT NULL DEFAULT '1' COMMENT '1 正常 0 废弃',
  PRIMARY KEY (`field_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_field`
--

LOCK TABLES `et_field` WRITE;
/*!40000 ALTER TABLE `et_field` DISABLE KEYS */;
INSERT INTO `et_field` VALUES (1,'计算机科学与技术','计算机科学与技术',1);
/*!40000 ALTER TABLE `et_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_group`
--

DROP TABLE IF EXISTS `et_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `group_level_id` int NOT NULL COMMENT '班组级别',
  `parent` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `group_level_id` (`group_level_id`) USING BTREE,
  KEY `parent` (`parent`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='班组';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_group`
--

LOCK TABLES `et_group` WRITE;
/*!40000 ALTER TABLE `et_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_knowledge_point`
--

DROP TABLE IF EXISTS `et_knowledge_point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_knowledge_point` (
  `point_id` int NOT NULL AUTO_INCREMENT,
  `point_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `field_id` int NOT NULL,
  `memo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `state` decimal(1,0) DEFAULT '1' COMMENT '1:正常 0：废弃',
  PRIMARY KEY (`point_id`) USING BTREE,
  KEY `fk_knowledge_field` (`field_id`) USING BTREE,
  CONSTRAINT `et_knowledge_point_ibfk_1` FOREIGN KEY (`field_id`) REFERENCES `et_field` (`field_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_knowledge_point`
--

LOCK TABLES `et_knowledge_point` WRITE;
/*!40000 ALTER TABLE `et_knowledge_point` DISABLE KEYS */;
INSERT INTO `et_knowledge_point` VALUES (1,'前端',1,'前端',1),(2,'后端',1,'后端',1),(3,'算法',1,'算法',1),(4,'AI',1,'AI',1);
/*!40000 ALTER TABLE `et_knowledge_point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_news`
--

DROP TABLE IF EXISTS `et_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titile` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` int NOT NULL COMMENT '创建人',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `is_expire` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否过期',
  `type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0 新闻， 1 系统信息',
  `group_id` int NOT NULL DEFAULT '-1' COMMENT '此系统属于哪个组',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `user_id` (`user_id`) USING BTREE,
  CONSTRAINT `et_news_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `et_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_news`
--

LOCK TABLES `et_news` WRITE;
/*!40000 ALTER TABLE `et_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_practice_paper`
--

DROP TABLE IF EXISTS `et_practice_paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_practice_paper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `duration` int NOT NULL COMMENT '试卷考试时间',
  `total_point` int DEFAULT '0',
  `pass_point` int DEFAULT '0',
  `group_id` int NOT NULL COMMENT '班组ID',
  `is_visible` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否所有用户可见，默认为0',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '试卷状态， 0未完成 -> 1已完成 -> 2已发布 -> 3通过审核 （已发布和通过审核的无法再修改）',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `summary` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '试卷介绍',
  `is_subjective` tinyint(1) DEFAULT NULL COMMENT '为1表示为包含主观题的试卷，需阅卷',
  `answer_sheet` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '试卷答案，用答题卡的结构保存',
  `creator` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '创建人的账号',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `group_id` (`group_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='试卷';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_practice_paper`
--

LOCK TABLES `et_practice_paper` WRITE;
/*!40000 ALTER TABLE `et_practice_paper` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_practice_paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_question`
--

DROP TABLE IF EXISTS `et_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `question_type_id` int NOT NULL COMMENT '题型',
  `duration` int DEFAULT NULL COMMENT '试题考试时间',
  `points` int DEFAULT NULL,
  `group_id` int DEFAULT NULL COMMENT '班组ID',
  `is_visible` tinyint(1) NOT NULL DEFAULT '0' COMMENT '试题可见性',
  `create_time` timestamp NULL DEFAULT NULL,
  `creator` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'admin' COMMENT '创建者',
  `last_modify` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `answer` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expose_times` int NOT NULL DEFAULT '2',
  `right_times` int NOT NULL DEFAULT '1',
  `wrong_times` int NOT NULL DEFAULT '1',
  `difficulty` int NOT NULL DEFAULT '1',
  `analysis` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `reference` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `examing_point` varchar(5000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `keyword` varchar(5000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `question_type_id` (`question_type_id`) USING BTREE,
  KEY `et_question_ibfk_5` (`creator`) USING BTREE,
  CONSTRAINT `et_question_ibfk_1` FOREIGN KEY (`question_type_id`) REFERENCES `et_question_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=198 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='试题';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_question`
--

LOCK TABLES `et_question` WRITE;
/*!40000 ALTER TABLE `et_question` DISABLE KEYS */;
INSERT INTO `et_question` VALUES (1,'人工智能是一种可以让···','<QuestionContent>\n  <title>人工智能是一种可以让机器模仿人类思考和行为的技术</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(2,'人工智能可以用于替代···','<QuestionContent>\n  <title>人工智能可以用于替代人类</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(3,'人工智能可以解决复杂···','<QuestionContent>\n  <title>人工智能可以解决复杂的问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(4,'人工智能是一种可以模···','<QuestionContent>\n  <title>人工智能是一种可以模拟人类数据处理的技术</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(5,'人工智能可以用于替代···','<QuestionContent>\n  <title>人工智能可以用于替代人力</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(6,'人工智能可以用于识别···','<QuestionContent>\n  <title>人工智能可以用于识别模式和趋势</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(7,'人工智能可以改进人类···','<QuestionContent>\n  <title>人工智能可以改进人类的情感</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(8,'人工智能可以自动识别···','<QuestionContent>\n  <title>人工智能可以自动识别文本和图像</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(9,'人工智能可以应用于自···','<QuestionContent>\n  <title>人工智能可以应用于自动驾驶</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(10,'人工智能可以用于设计···','<QuestionContent>\n  <title>人工智能可以用于设计机器人</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(11,'快速排序算法是一种原···','<QuestionContent>\n  <title>快速排序算法是一种原地排序算法</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(12,'广度优先搜索算法可以···','<QuestionContent>\n  <title>广度优先搜索算法可以用于求解最短路径问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(13,'动态规划算法可以用于···','<QuestionContent>\n  <title>动态规划算法可以用于解决最小生成树问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(14,'二分搜索算法可以用于···','<QuestionContent>\n  <title>二分搜索算法可以用于有序数组查找</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(15,'贪心算法可以用于求解···','<QuestionContent>\n  <title>贪心算法可以用于求解最大流问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(16,'深度优先搜索算法可以···','<QuestionContent>\n  <title>深度优先搜索算法可以用于求解最小生成树问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(17,'KMP算法可以用于查···','<QuestionContent>\n  <title>KMP算法可以用于查找字符串的最长公共子串</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(18,'动态规划算法可以用于···','<QuestionContent>\n  <title>动态规划算法可以用于解决线性规划问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(19,'布隆过滤器可以用于解···','<QuestionContent>\n  <title>布隆过滤器可以用于解决最大优先队列问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(20,'并查集算法可以用于解···','<QuestionContent>\n  <title>并查集算法可以用于解决最短路径问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(21,'回溯算法可以用于解决···','<QuestionContent>\n  <title>回溯算法可以用于解决最小生成树问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(22,'随机森林算法可以用于···','<QuestionContent>\n  <title>随机森林算法可以用于解决线性规划问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(23,'快速傅里叶变换算法可···','<QuestionContent>\n  <title>快速傅里叶变换算法可以用于求解最大优先队列问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(24,'BF算法可以用于查找···','<QuestionContent>\n  <title>BF算法可以用于查找字符串的最长公共子串</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(25,'蒙特卡洛算法可以用于···','<QuestionContent>\n  <title>蒙特卡洛算法可以用于解决最小生成树问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(26,'快速傅里叶变换算法可···','<QuestionContent>\n  <title>快速傅里叶变换算法可以用于求解最短路径问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(27,'A*算法可以用于解决···','<QuestionContent>\n  <title>A*算法可以用于解决最大流问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(28,'元素替换算法可以用于···','<QuestionContent>\n  <title>元素替换算法可以用于求解最大优先队列问题</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(29,'布隆过滤器可以用于有···','<QuestionContent>\n  <title>布隆过滤器可以用于有序数组查找</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(30,'二叉搜索树算法可以用···','<QuestionContent>\n  <title>二叉搜索树算法可以用于查找字符串的最长公共子串</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(31,' 在 HTML5 中···','<QuestionContent>\n  <title> 在 HTML5 中， meta 标签可以用于指定 CSS 样式？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(32,' 在 CSS 文件中···','<QuestionContent>\n  <title> 在 CSS 文件中，使用属性选择器可以指定某个元素的父元素？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(33,' CSS3 中的网格···','<QuestionContent>\n  <title> CSS3 中的网格布局可以让网页元素更容易地实现响应式布局？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(34,' 在 Javascr···','<QuestionContent>\n  <title> 在 Javascript 中，变量的作用域仅限于函数内部？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(35,' Flash 可以用···','<QuestionContent>\n  <title> Flash 可以用于开发移动应用程序？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(36,' 在 HTML 文档···','<QuestionContent>\n  <title> 在 HTML 文档中，所有的标签都必须闭合？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(37,' 在 CSS 中，可···','<QuestionContent>\n  <title> 在 CSS 中，可以使用颜色代码来指定元素的颜色？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(38,' 在 JavaScr···','<QuestionContent>\n  <title> 在 JavaScript 中，每个函数都有自己的作用域？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(39,' 在 HTML5 中···','<QuestionContent>\n  <title> 在 HTML5 中，可以使用 canvas 标签来创建图形？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(40,' 在 CSS 中，可···','<QuestionContent>\n  <title> 在 CSS 中，可以使用绝对定位将元素定位在页面上？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(41,' 在Java中，St···','<QuestionContent>\n  <title> 在Java中，String类是一个典型的引用类型？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(42,' 在MySQL中，主···','<QuestionContent>\n  <title> 在MySQL中，主键和外键的作用是一样的？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(43,' 在C语言中，变量可···','<QuestionContent>\n  <title> 在C语言中，变量可以定义为常量？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(44,' 在Java中，接口···','<QuestionContent>\n  <title> 在Java中，接口可以实现方法？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(45,'js中，可以使用re···','<QuestionContent>\n  <title>js中，可以使用require()函数来加载模块？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(46,' 在Javascri···','<QuestionContent>\n  <title> 在Javascript中，可以使用for语句来实现while循环？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(47,' 在C++中，变量可···','<QuestionContent>\n  <title> 在C++中，变量可以用来存储函数？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','F',2,1,1,1,NULL,NULL,NULL,NULL),(48,' 在PHP中，可以使···','<QuestionContent>\n  <title> 在PHP中，可以使用echo语句来输出变量值？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(49,' 在MySQL中，可···','<QuestionContent>\n  <title> 在MySQL中，可以使用DROP语句来删除表？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(50,' 在Python中，···','<QuestionContent>\n  <title> 在Python中，可以使用break语句来跳出循环？</title>\n  <titleImg></titleImg>\n  <choiceList/>\n  <choiceImgList/>\n</QuestionContent>',3,NULL,1,NULL,0,NULL,'admin','2023-05-05 09:08:57','T',2,1,1,1,NULL,NULL,NULL,NULL),(51,'  对于计算机视觉，···','<QuestionContent>\n  <title>  对于计算机视觉，深度学习模型的最佳解决方案是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>机器学习</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>卷积神经网络</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>人工神经网络</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>决策树</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(52,' 对于机器翻译，使用···','<QuestionContent>\n  <title> 对于机器翻译，使用最流行的技术是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>统计机器翻译</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>基于规则机器翻译</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>基于深度学习机器翻译</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>基于计算机视觉机器翻译</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(53,' 以下关于神经网络的···','<QuestionContent>\n  <title> 以下关于神经网络的描述中，哪一项是正确的？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>神经网络采用层次结构</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>神经网络是基于规则的学习</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>神经网络可以模拟人的思维</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>神经网络可以解决复杂的任务</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(54,' 对于图形识别，最常···','<QuestionContent>\n  <title> 对于图形识别，最常用的技术是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>卷积神经网络</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>朴素贝叶斯分类器</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>随机森林</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>支持向量机</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(55,' 为了提高深度学习模···','<QuestionContent>\n  <title> 为了提高深度学习模型的性能，最有效的方法是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>增加层数</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>增加模型复杂度</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>增加训练数据量</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>减少层数</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(56,' 为了解决视觉问题，···','<QuestionContent>\n  <title> 为了解决视觉问题，最常用的技术是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>传统机器学习</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>深度学习</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>卷积神经网络</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>自动微分</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(57,' 对于自然语言处理，···','<QuestionContent>\n  <title> 对于自然语言处理，最常用的技术是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>深度学习</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>朴素贝叶斯</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>随机森林</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>语言模型</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(58,' 为了提高深度学习模···','<QuestionContent>\n  <title> 为了提高深度学习模型的预测性能，最有效的方法是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>增加层数</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>增加模型复杂度</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>增加训练数据量</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>减少层数</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(59,' 对于自然语言处理，···','<QuestionContent>\n  <title> 对于自然语言处理，最常用的算法是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>支持向量机</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>朴素贝叶斯</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>递归神经网络</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>随机森林</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(60,' 为了防止深度学习模···','<QuestionContent>\n  <title> 为了防止深度学习模型的过拟合，最有效的方法是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>增加训练数据量</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>数据增强</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>正则化</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>增加模型复杂度</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(61,' 在计算机视觉中，用···','<QuestionContent>\n  <title> 在计算机视觉中，用于从图像中提取特征的技术是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>目标检测</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>图像分割</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>特征提取</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>图像识别</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(62,' 在机器学习中，用于···','<QuestionContent>\n  <title> 在机器学习中，用于表示特征的数据结构是：</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>树</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>向量</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>列表</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>字典</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(63,'给定两个数组A和B，···','<QuestionContent>\n  <title>给定两个数组A和B，其中A的大小为m，B的大小为n，则下面哪个排序算法可以在最坏情况下达到O(m+n)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>插入排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(64,'给定一个无序整数数组···','<QuestionContent>\n  <title>给定一个无序整数数组A，其中元素范围从0到n-1，其中n是数组A的大小，下面哪个排序算法可以在最坏情况下达到O(n)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>计数排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(65,'给定一个数组A，其中···','<QuestionContent>\n  <title>给定一个数组A，其中元素范围从0到k，其中k是数组A的最大值，下面哪个排序算法可以在最坏情况下达到O(n)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>基数排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(66,'给定一个数组A，其中···','<QuestionContent>\n  <title>给定一个数组A，其中元素可以是任意整数，下面哪个排序算法可以在最坏情况下达到O(nlog n)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>插入排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(67,'给定一个数组A，其中···','<QuestionContent>\n  <title>给定一个数组A，其中元素可以是任意整数，下面哪个排序算法可以在最坏情况下达到O(n^2)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>插入排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(68,'给定一个有序数组A，···','<QuestionContent>\n  <title>给定一个有序数组A，下面哪个排序算法可以在最坏情况下达到O(n)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>折半查找</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(69,'给定一个有序数组A，···','<QuestionContent>\n  <title>给定一个有序数组A，下面哪个排序算法可以在最坏情况下达到O(log n)的时间复杂度？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>归并排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>二分查找</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(70,'给定一个有向图G，其···','<QuestionContent>\n  <title>给定一个有向图G，其中有n个顶点和m条边，下面哪个算法可以检测是否存在从某个顶点到另一个顶点的路径？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>广度优先搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>深度优先搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>图的连通性算法</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>图的最短路径算法</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(71,'给定一个有向图G，其···','<QuestionContent>\n  <title>给定一个有向图G，其中有n个顶点和m条边，下面哪个算法可以找出从某个指定的顶点到另一个指定顶点的最短路径？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>广度优先搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>深度优先搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>图的连通性算法</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>图的最短路径算法</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(72,'给定一个数组A和一个···','<QuestionContent>\n  <title>给定一个数组A和一个值x，下面哪个算法可以在最坏情况下找出x在A中出现的次数？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二分搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>二叉搜索树搜索</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>哈希表搜索</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(73,'给定一个数组A和一个···','<QuestionContent>\n  <title>给定一个数组A和一个值x，下面哪个算法可以在最坏情况下找出x在A中的位置？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二分搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>二叉搜索树搜索</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>哈希表搜索</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(74,'给定一个数组A，下面···','<QuestionContent>\n  <title>给定一个数组A，下面哪个算法可以在最坏情况下找出A中的最大值？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二叉搜索树搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>分治法</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>堆排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(75,'给定一个数组A，下面···','<QuestionContent>\n  <title>给定一个数组A，下面哪个算法可以在最坏情况下找出A中的第k小的元素？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二叉搜索树搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>快速选择</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>堆排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(76,'给定一个数组A，下面···','<QuestionContent>\n  <title>给定一个数组A，下面哪个算法可以在最坏情况下找出A中的第k大的元素？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二叉搜索树搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>快速选择</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>堆排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(77,'给定一个数组A，下面···','<QuestionContent>\n  <title>给定一个数组A，下面哪个算法可以在最坏情况下实现某种程度的平衡？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二叉搜索树</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>AVL树</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(78,'给定一个数组A，下面···','<QuestionContent>\n  <title>给定一个数组A，下面哪个算法可以在最坏情况下实现最优的查找性能？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>线性搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>二叉搜索树</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>跳表</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(79,' web前端开发的主···','<QuestionContent>\n  <title> web前端开发的主要语言是？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>HTML</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>JavaScript</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>CSS</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Java</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(80,' HTML文档的根元···','<QuestionContent>\n  <title> HTML文档的根元素是什么？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>&lt;body&gt;</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>&lt;head&gt;</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>&lt;html&gt;</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>&lt;title&gt;</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(81,' 以下哪个不是CSS···','<QuestionContent>\n  <title> 以下哪个不是CSS的特性？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>缩小文件大小</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>控制文档的外观</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>动态添加元素</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>增强用户体验</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(82,' 以下哪个不是Jav···','<QuestionContent>\n  <title> 以下哪个不是JavaScript的数据类型？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>字符串</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>数字</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>布尔</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>数组</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(83,' 以下哪个不是Jav···','<QuestionContent>\n  <title> 以下哪个不是JavaScript的保留字？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>type</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>var</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>new</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>super</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(84,' 以下哪个不是HTM···','<QuestionContent>\n  <title> 以下哪个不是HTML5新增的元素？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>&lt;video&gt;</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>&lt;form&gt;</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>&lt;canvas&gt;</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>&lt;audio&gt;</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(85,' 在CSS中，z-i···','<QuestionContent>\n  <title> 在CSS中，z-index属性用于？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>控制文字颜色</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>控制元素的显示顺序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>控制文字字体</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>控制元素的宽度</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(86,' 以下哪个不是Jav···','<QuestionContent>\n  <title> 以下哪个不是JavaScript的操作符？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>+</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>*</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>&</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>&&</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(87,' 以下哪个不是Jav···','<QuestionContent>\n  <title> 以下哪个不是JavaScript的内置函数？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>alert()</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>log()</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>prompt()</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>eval()</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(88,' 如何在JavaSc···','<QuestionContent>\n  <title> 如何在JavaScript中创建数组？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>[1,2,3];</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>Array(1,2,3);</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Array[1,2,3];</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Array();</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(89,' 以下哪个不是Jav···','<QuestionContent>\n  <title> 以下哪个不是JavaScript的数组方法？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>push()</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>slice()</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>typeof()</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>splice()</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(90,' 以下哪个不是CSS···','<QuestionContent>\n  <title> 以下哪个不是CSS选择器？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>#id</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>*</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>div</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>element</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(91,' 以下哪个不是HTM···','<QuestionContent>\n  <title> 以下哪个不是HTML5新增的特性？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>视频播放</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>拖放</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>动画</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>表单验证</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(92,' 以下哪个不是Jav···','<QuestionContent>\n  <title> 以下哪个不是JavaScript的内置对象？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>String</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>Number</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Date</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Array</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(93,' 如何在CSS中改变···','<QuestionContent>\n  <title> 如何在CSS中改变文本的大小？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>font-size</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>font-weight</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>color</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>font-family</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(94,' SQL语言中的SE···','<QuestionContent>\n  <title> SQL语言中的SELECT关键字用于？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>删除数据</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>插入数据</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>更新数据</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>检索数据</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(95,' 在HTTP协议中，···','<QuestionContent>\n  <title> 在HTTP协议中，GET方法用于？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>传输文件</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>请求数据</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>更新数据</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>发送响应</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(96,' 在C言语中，下面哪···','<QuestionContent>\n  <title> 在C言语中，下面哪个不是保留字？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>static</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>int</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>for</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>goto</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(97,' 在Linux系统中···','<QuestionContent>\n  <title> 在Linux系统中，下面哪个命令可以显示指定文件的内容？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>touch</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>ls</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>cat</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>cp</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(98,' 在Java语言中，···','<QuestionContent>\n  <title> 在Java语言中，下面哪个不是基本数据类型？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>int</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>float</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>String</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>boolean</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(99,' 下面哪种设计模式是···','<QuestionContent>\n  <title> 下面哪种设计模式是面向对象编程的核心？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>装饰器模式</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>观察者模式</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>工厂模式</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>单例模式</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(100,' 下列哪种数据库不属···','<QuestionContent>\n  <title> 下列哪种数据库不属于关系型数据库？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Oracle</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>MySQL</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>MongoDB</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Server</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(101,' 下列哪个不是Lin···','<QuestionContent>\n  <title> 下列哪个不是Linux系统的文件权限？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>write</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>read</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>execute</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>delete</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(102,' 以下哪一种语言不属···','<QuestionContent>\n  <title> 以下哪一种语言不属于静态类型语言？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Java</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>C++</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Python</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>JavaScript</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(103,' 哪个是用于控制多个···','<QuestionContent>\n  <title> 哪个是用于控制多个线程之间交替执行的机制？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>多线程</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>多进程</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>锁</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>管程</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','D',2,1,1,1,NULL,NULL,NULL,NULL),(104,' 哪个HTTP请求方···','<QuestionContent>\n  <title> 哪个HTTP请求方法用于向服务器发送新资源？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>POST</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>GET</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>PUT</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>DELETE</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','A',2,1,1,1,NULL,NULL,NULL,NULL),(105,' 以下哪一项不是反射···','<QuestionContent>\n  <title> 以下哪一项不是反射的特点？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>动态加载类</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>检查类的信息</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>实例化对象</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>调用对象的方法</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(106,' 哪个不是数据库事务···','<QuestionContent>\n  <title> 哪个不是数据库事务的特性？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>一致性</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>并发性</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>原子性</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>隔离性</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','B',2,1,1,1,NULL,NULL,NULL,NULL),(107,' 在JavaScri···','<QuestionContent>\n  <title> 在JavaScript中，下列哪个不是数据类型？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Number</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>String</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Class</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Boolean</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(108,' 在Linux系统中···','<QuestionContent>\n  <title> 在Linux系统中，下面哪个命令可以查看当前用户的权限？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>chmod</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>chown</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>whoami</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>sudo</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',1,NULL,2,NULL,0,NULL,'admin','2023-05-05 09:08:57','C',2,1,1,1,NULL,NULL,NULL,NULL),(109,' 以下哪些是 CSS···','<QuestionContent>\n  <title> 以下哪些是 CSS 动画（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>transition</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>animation</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>hover</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>transform</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、D',2,1,1,1,NULL,NULL,NULL,NULL),(110,' 以下哪些技术可以用···','<QuestionContent>\n  <title> 以下哪些技术可以用来实现跨域请求（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>iframe</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>JSONP</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>AJAX</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>WebSocket</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(111,' 关于响应式布局，以···','<QuestionContent>\n  <title> 关于响应式布局，以下哪些是正确的（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>可以根据用户设备的屏幕尺寸自动调整网页布局</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>请求次数</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>可以提高网页的搜索引擎优化</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>可以提高网页的载入速度</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、C',2,1,1,1,NULL,NULL,NULL,NULL),(112,' 如何使用 Java···','<QuestionContent>\n  <title> 如何使用 JavaScript 实现延迟加载（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>setTimeout()</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>setInterval()</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>属性</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>属性</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(113,' 以下哪些是 HTM···','<QuestionContent>\n  <title> 以下哪些是 HTML5 新增的元素（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>footer</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>nav</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>section</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>canvas</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(114,' 以下哪些是 Jav···','<QuestionContent>\n  <title> 以下哪些是 JavaScript 中的类型（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Number</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>Boolean</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Character</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Object</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、D',2,1,1,1,NULL,NULL,NULL,NULL),(115,' 关于 jQuery···','<QuestionContent>\n  <title> 关于 jQuery 的 Ajax 方法，以下哪些是正确的（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>get()</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>post()</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>put()</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>delete()</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B',2,1,1,1,NULL,NULL,NULL,NULL),(116,' 以下哪些是 CSS···','<QuestionContent>\n  <title> 以下哪些是 CSS 选择器（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>选择器</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>类选择器</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>属性选择器</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>伪类选择器</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(117,' 以下哪些是 Web···','<QuestionContent>\n  <title> 以下哪些是 Web 浏览器支持的新特性（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>HTML5</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>CSS3</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>JavaScript</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>PHP</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C',2,1,1,1,NULL,NULL,NULL,NULL),(118,' 以下哪些是浏览器渲···','<QuestionContent>\n  <title> 以下哪些是浏览器渲染网页的基本步骤（ ）</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>HTML</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>CSS</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>加载图片</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>JavaScript</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(119,' 选择正确的排序算法···','<QuestionContent>\n  <title> 选择正确的排序算法</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>快速排序</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>堆排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>插入排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>希尔排序</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、D',2,1,1,1,NULL,NULL,NULL,NULL),(120,' 下列算法中，属于动···','<QuestionContent>\n  <title> 下列算法中，属于动态规划算法的是？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>贪心算法</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>分治算法</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>线性规划</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>朴素贝叶斯</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C',2,1,1,1,NULL,NULL,NULL,NULL),(121,' 下列关于快速排序的···','<QuestionContent>\n  <title> 下列关于快速排序的描述，正确的有？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>是一种冒泡排序算法</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>是一种分治算法</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>由于不断交换数据，所以比较耗时</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>时间复杂度为O（n2）</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','B、D',2,1,1,1,NULL,NULL,NULL,NULL),(122,' 下列关于多源最短路···','<QuestionContent>\n  <title> 下列关于多源最短路径问题的算法，属于动态规划算法的是？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Floyd算法</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>A*算法</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Dijkstra算法</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>回溯算法</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、C',2,1,1,1,NULL,NULL,NULL,NULL),(123,' 关于组合数学算法，···','<QuestionContent>\n  <title> 关于组合数学算法，下列描述正确的是？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>只适用于解决搜索问题</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>只能解决有限组合问题</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>可以用于解决组合问题</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>时间复杂度是O（nlogn）</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','B、C',2,1,1,1,NULL,NULL,NULL,NULL),(124,' 下列算法中，属于搜···','<QuestionContent>\n  <title> 下列算法中，属于搜索算法的是？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>深度优先搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>广度优先搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>贪心算法</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>朴素贝叶斯</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B',2,1,1,1,NULL,NULL,NULL,NULL),(125,' 下列关于堆排序的描···','<QuestionContent>\n  <title> 下列关于堆排序的描述，正确的有？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>时间复杂度为O（nlogn）</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>不稳定排序</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>是一种选择排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>需要额外的辅助空间</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、D',2,1,1,1,NULL,NULL,NULL,NULL),(126,' 下列关于朴素贝叶斯···','<QuestionContent>\n  <title> 下列关于朴素贝叶斯算法的描述，正确的有？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>是一种搜索算法</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>用于多分类问题</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>支持在线学习</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>时间复杂度为O（n2）</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','B、C',2,1,1,1,NULL,NULL,NULL,NULL),(127,'在一个有向图中，什么···','<QuestionContent>\n  <title>在一个有向图中，什么算法可以找出图中的所有源点？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>深度优先搜索</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>广度优先搜索</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>拓扑排序</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Kruskal算法</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、C',2,1,1,1,NULL,NULL,NULL,NULL),(128,' 下列关于广度优先搜···','<QuestionContent>\n  <title> 下列关于广度优先搜索的描述，正确的有？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>不是一种动态规划算法</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>不能处理有向图</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>可以用于求解最短路径</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>时间复杂度为O（n）</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(129,' 以下哪些是人工智能···','<QuestionContent>\n  <title> 以下哪些是人工智能的应用？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>图像识别</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>自然语言处理</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>游戏开发</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>搜索引擎</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、D',2,1,1,1,NULL,NULL,NULL,NULL),(130,' 以下哪些是机器学习···','<QuestionContent>\n  <title> 以下哪些是机器学习的基本思想？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>无监督学习</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>强化学习</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>聚类分析</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>决策树</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(131,' 以下哪些是深度学习···','<QuestionContent>\n  <title> 以下哪些是深度学习技术？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>神经网络</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>卷积神经网络</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>受限玻尔兹曼机</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>集成学习</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C',2,1,1,1,NULL,NULL,NULL,NULL),(132,' 以下哪些是机器学习···','<QuestionContent>\n  <title> 以下哪些是机器学习的类型？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>监督学习</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>半监督学习</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>无监督学习</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>强化学习</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(133,' 以下哪些是机器学习···','<QuestionContent>\n  <title> 以下哪些是机器学习的常见算法？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>决策树</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>支持向量机</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>朴素贝叶斯</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>逻辑回归</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(134,' 以下哪些是自然语言···','<QuestionContent>\n  <title> 以下哪些是自然语言处理的应用？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>文本分类</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>文本摘要</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>语音识别</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>情感分析</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(135,' 以下哪些是人工智能···','<QuestionContent>\n  <title> 以下哪些是人工智能的发展阶段？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>模仿阶段</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>再现阶段</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>协同阶段</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>自主阶段</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(136,' 以下哪些是数据挖掘···','<QuestionContent>\n  <title> 以下哪些是数据挖掘的步骤？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>数据收集</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>特征工程</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>模型训练</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>模型评估</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(137,' 以下哪些是计算机视···','<QuestionContent>\n  <title> 以下哪些是计算机视觉的应用？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>图像分割</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>视频监控</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>目标检测</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>识别跟踪</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(138,' 以下哪些是模式识别···','<QuestionContent>\n  <title> 以下哪些是模式识别的方法？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>分类</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>回归</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>聚类</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>分层学习</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(139,' 以下哪些是Linu···','<QuestionContent>\n  <title> 以下哪些是Linux操作系统的特点？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>安全性好</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>免费开源</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>运行效率高</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>易于使用</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C ',2,1,1,1,NULL,NULL,NULL,NULL),(140,' 以下哪些是MySQ···','<QuestionContent>\n  <title> 以下哪些是MySQL数据库中常用数据类型？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Integer</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>Float</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Char</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Text</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(141,' 以下哪些是Web开···','<QuestionContent>\n  <title> 以下哪些是Web开发框架？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Angular</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>js</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Django</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>React</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(142,' 以下哪些是比较流行···','<QuestionContent>\n  <title> 以下哪些是比较流行的开发语言？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>Java</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>Python</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>C++</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>Go</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(143,' 以下哪些是Linu···','<QuestionContent>\n  <title> 以下哪些是Linux系统管理员的职责？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>管理系统文件</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>安装新软件</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>监控系统性能</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>维护系统安全</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(144,' 以下哪些是常用的编···','<QuestionContent>\n  <title> 以下哪些是常用的编程范式？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>命令式</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>函数式</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>面向对象</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>过程式</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(145,' 以下哪些是HTTP···','<QuestionContent>\n  <title> 以下哪些是HTTP协议支持的请求方法？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>GET</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>POST</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>PUT</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>DELETE</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(146,' 以下哪些是常用的数···','<QuestionContent>\n  <title> 以下哪些是常用的数据库？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>MongoDB</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>Oracle</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>PostgreSQL</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>MySQL</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(147,' 以下哪些是计算机网···','<QuestionContent>\n  <title> 以下哪些是计算机网络的网络拓扑结构？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>环形网络</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>树形网络</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>网状网络</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>星形网络</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','A、B、C、D ',2,1,1,1,NULL,NULL,NULL,NULL),(148,' 以下哪些是计算机网···','<QuestionContent>\n  <title> 以下哪些是计算机网络中的数据链路层协议？</title>\n  <titleImg></titleImg>\n  <choiceList>\n    <entry>\n      <string>A</string>\n      <string>TCP</string>\n    </entry>\n    <entry>\n      <string>B</string>\n      <string>IP</string>\n    </entry>\n    <entry>\n      <string>C</string>\n      <string>Ethernet</string>\n    </entry>\n    <entry>\n      <string>D</string>\n      <string>ARP</string>\n    </entry>\n  </choiceList>\n  <choiceImgList/>\n</QuestionContent>',2,NULL,3,NULL,0,NULL,'admin','2023-05-05 09:08:57','B、C、D',2,1,1,1,NULL,NULL,NULL,NULL),(149,' 请描述浏览器的跨域···','<QuestionContent>\n  <title> 请描述浏览器的跨域安全策略？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：浏览器的跨域安全策略（CORS）是一种浏览器机制，它允许Web应用程序从不同的域名（源）加载资源，而不受跨域限制。CORS可以阻止域之间的跨站点脚本攻击（XSS），防止未经授权的资源访问，并且可以确保网页的安全性。',2,1,1,1,NULL,NULL,NULL,NULL),(150,' 什么是HTTP缓存···','<QuestionContent>\n  <title> 什么是HTTP缓存？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：HTTP缓存是指浏览器和服务器之间用于存储响应资源的机制，此机制可以减少服务器和网络上的流量，提高网站的性能和加载速度。',2,1,1,1,NULL,NULL,NULL,NULL),(151,' 请解释一下你对AJ···','<QuestionContent>\n  <title> 请解释一下你对AJAX的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：AJAX（异步JavaScript和XML）是一种用于创建异步Web应用程序的技术，可以在不重新加载整个页面的情况下在Web页面中更新内容。它可以使Web应用程序更加流畅和响应，减少服务器的工作量，并使用XMLHttpRequest对象来与服务器进行通信。',2,1,1,1,NULL,NULL,NULL,NULL),(152,' 请解释一下你对路由···','<QuestionContent>\n  <title> 请解释一下你对路由的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：路由是将用户从一个URL路径转移到另一个URL路径的过程。它可以使您的Web应用程序更加灵活，可以处理多个路径，并且可以在不需要重新加载整个页面的情况下更新内容。',2,1,1,1,NULL,NULL,NULL,NULL),(153,' 请描述一下你对状态···','<QuestionContent>\n  <title> 请描述一下你对状态管理的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：状态管理是一种用于管理Web应用程序状态的技术，可以跟踪应用程序中的数据变化，并将数据存储在一个集中的地方，以便在整个应用程序中共享。状态管理可以提高应用程序的性能，并简化应用程序的开发。',2,1,1,1,NULL,NULL,NULL,NULL),(154,' 请描述一下你对We···','<QuestionContent>\n  <title> 请描述一下你对Web存储的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：Web存储是一种技术，可以在浏览器中存储数据，并用于在不连接到服务器的情况下持久保存应用程序数据。它可以让你缓存数据，并在后续会话中恢复，从而改善Web应用程序的性能。',2,1,1,1,NULL,NULL,NULL,NULL),(155,' 什么是前端性能优化···','<QuestionContent>\n  <title> 什么是前端性能优化？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：前端性能优化是一种技术，可以提高Web应用程序的性能，并缩短加载时间。它可以通过减少渲染时间，优化文件大小，添加缓存，消除不必要的资源请求等方式来实现。',2,1,1,1,NULL,NULL,NULL,NULL),(156,' 什么是浏览器的内存···','<QuestionContent>\n  <title> 什么是浏览器的内存泄漏？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：浏览器内存泄漏是指当Web应用程序获取内存时，无法正确释放它，从而导致浏览器无法重用空间，造成内存占用过多。',2,1,1,1,NULL,NULL,NULL,NULL),(157,' 请描述一下你对We···','<QuestionContent>\n  <title> 请描述一下你对Web安全的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：Web安全是指保护Web应用程序免受安全漏洞，木马，劫持，垃圾邮件，恶意软件，病毒和其他恶意行为的攻击的技术。它可以使用加密，身份验证，数据验证，安全代理和其他技术来确保Web应用程序的安全性。',2,1,1,1,NULL,NULL,NULL,NULL),(158,' 请描述一下你对设计···','<QuestionContent>\n  <title> 请描述一下你对设计模式的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：设计模式是一种可重复使用的解决方案，可以解决软件开发中常见的问题。它们可以帮助开发人员更快地解决问题，更好地管理代码，并将其重新用于不同的场景。',2,1,1,1,NULL,NULL,NULL,NULL),(159,' 请解释一下你对编程···','<QuestionContent>\n  <title> 请解释一下你对编程的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：编程是一种技术，可以使用一种编程语言（如JavaScript，Python等）来编写可以被计算机理解的代码，以便实现特定的功能。',2,1,1,1,NULL,NULL,NULL,NULL),(160,' 请描述一下你对AP···','<QuestionContent>\n  <title> 请描述一下你对API的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：API（应用程序编程接口）是提供给开发人员使用的接口，可以访问应用程序的功能，而无需直接访问应用程序的代码。它们可以用于创建更具交互性的应用程序，以及将应用程序与其他应用程序集成。',2,1,1,1,NULL,NULL,NULL,NULL),(161,' 请描述一下你对RE···','<QuestionContent>\n  <title> 请描述一下你对REST的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：REST（表现层状态转移）是一种Web服务的设计架构，可以让客户端和服务器之间进行交互，而不是使用更复杂的SOAP协议。它可以使用HTTP方法，如GET，POST，PUT和DELETE，来实现服务器上的资源操作。',2,1,1,1,NULL,NULL,NULL,NULL),(162,' 请描述你对自然语言···','<QuestionContent>\n  <title> 请描述你对自然语言处理（NLP）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：自然语言处理（NLP）是指用计算机程序来处理人类语言（例如英语，汉语等）的一类技术，它结合了计算机科学、语言学以及心理学的研究。NLP的主要目的是使计算机能够理解人类语言，从而帮助人们更好地与计算机进行交互。',2,1,1,1,NULL,NULL,NULL,NULL),(163,' 请描述你对机器学习···','<QuestionContent>\n  <title> 请描述你对机器学习的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：机器学习是一门研究计算机程序的学科，旨在通过研究已有的数据来学习，以便能够自动执行特定任务。机器学习技术可以让计算机程序从数据中自动分析出规律，从而提高程序的准确性和效率。',2,1,1,1,NULL,NULL,NULL,NULL),(164,' 请描述你对深度学习···','<QuestionContent>\n  <title> 请描述你对深度学习（DL）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：深度学习（DL）是一种机器学习技术，它利用多层神经网络（ANN）来模拟人类大脑中的学习过程，以解决复杂的计算问题。DL技术可以自动从大量数据中学习模式，并使用计算机模拟人类的学习过程，从而实现自动决策和行为。',2,1,1,1,NULL,NULL,NULL,NULL),(165,' 请描述你对计算机视···','<QuestionContent>\n  <title> 请描述你对计算机视觉（CV）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：计算机视觉（CV）是一门研究如何让计算机系统模拟人类视觉的学科，它结合了图像处理、计算机视觉、机器学习和模式识别等多个技术。CV可以用来处理视觉信息，从而帮助计算机系统识别出图像中的目标，并实现自动化的目标检测和分类。',2,1,1,1,NULL,NULL,NULL,NULL),(166,' 请描述你对模式识别···','<QuestionContent>\n  <title> 请描述你对模式识别的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：模式识别是一门研究如何让计算机系统从大量数据中自动识别特征的学科，它结合了信号处理、机器学习和计算机视觉等技术。模式识别旨在从数据中自动发现目标，并将其与之前的经验或知识进行比较，从而实现分类和识别。',2,1,1,1,NULL,NULL,NULL,NULL),(167,' 请描述你对人工智能···','<QuestionContent>\n  <title> 请描述你对人工智能（AI）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：人工智能（AI）是一门研究如何让计算机系统模拟人类智力的学科，它结合了计算机科学、软件工程、信息学等多个领域的研究。AI的主要目的是使计算机系统实现智能化，从而解决复杂的计算问题。',2,1,1,1,NULL,NULL,NULL,NULL),(168,' 请描述你对机器人学···','<QuestionContent>\n  <title> 请描述你对机器人学的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：机器人学是一门研究机器人技术的学科，它结合了机械工程、电气工程、计算机科学以及人工智能等多个技术。机器人学的主要目的是研究如何设计、制造和控制机器人，从而实现自动化的操作和任务完成。',2,1,1,1,NULL,NULL,NULL,NULL),(169,' 请描述你对知识工程···','<QuestionContent>\n  <title> 请描述你对知识工程（KE）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：知识工程（KE）是一门研究如何获取、组织、维护和利用有用信息的学科，它结合了计算机科学、数据库技术、人工智能以及逻辑学等多个技术。KE的主要目的是让计算机系统能够更加智能地获取、理解和利用有用的信息。',2,1,1,1,NULL,NULL,NULL,NULL),(170,' 请描述你对语音识别···','<QuestionContent>\n  <title> 请描述你对语音识别（SR）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：语音识别（SR）是一种计算机技术，它可以自动识别人类语音，并将其转换为文本或其他格式的数据。SR技术结合了信号处理、机器学习和语言学等技术，可以自动识别语音，从而实现智能化的语音交互。',2,1,1,1,NULL,NULL,NULL,NULL),(171,' 请描述你对文本挖掘···','<QuestionContent>\n  <title> 请描述你对文本挖掘的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：文本挖掘是一种计算机技术，它可以从大量文本数据中提取有用的信息，并自动分析文本内容。文本挖掘技术结合了计算机科学、数据挖掘、机器学习以及自然语言处理等技术，可以自动从文本数据中提取模式，从而实现智能化的文本分析。',2,1,1,1,NULL,NULL,NULL,NULL),(172,' 请描述你对强化学习···','<QuestionContent>\n  <title> 请描述你对强化学习（RL）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：强化学习（RL）是一种机器学习技术，它可以让计算机系统在没有明确的目标的情况下，通过不断的试错和反馈，从数据中学习有效的行为策略。RL技术可以为计算机系统提供更加灵活和弹性的行为方式，从而实现智能化的决策和控制。',2,1,1,1,NULL,NULL,NULL,NULL),(173,' 请描述你对智能软件···','<QuestionContent>\n  <title> 请描述你对智能软件开发的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：智能软件开发是一种计算机技术，它结合软件工程、人工智能和自然语言处理等技术，可以为计算机系统设计出智能化的软件应用。智能软件开发的主要目的是使软件能够从数据中自动学习和推断，从而实现自动的决策和行为。',2,1,1,1,NULL,NULL,NULL,NULL),(174,' 请描述你对机器人操···','<QuestionContent>\n  <title> 请描述你对机器人操作系统（ROS）的理解？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：机器人操作系统（ROS）是一种软件平台，它可以帮助机器人开发者更好地管理机器人软件，并实现自动化的操作和任务完成。ROS结合了计算机科学、软件工程、机器学习以及机器人学等技术，可以为机器人开发者提供灵活、可扩展的软件平台，从而实现自动化的控制和任务完成。',2,1,1,1,NULL,NULL,NULL,NULL),(175,' 如何优化数据库的查···','<QuestionContent>\n  <title> 如何优化数据库的查询性能？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：通过建立索引来提高查询性能，选择正确的数据类型，正确设计表结构，避免拼接大量的字符串，缓存查询结果，优化查询语句，使用内存表等方式来优化数据库查询性能。',2,1,1,1,NULL,NULL,NULL,NULL),(176,' 如何处理多线程任务···','<QuestionContent>\n  <title> 如何处理多线程任务？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：多线程任务可以通过多线程编程技术来实现，可以使用多线程库、定时器、可重入锁等方式来实现多线程任务的处理。',2,1,1,1,NULL,NULL,NULL,NULL),(177,' 如何保证系统的可用···','<QuestionContent>\n  <title> 如何保证系统的可用性？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：保证系统的可用性可以通过建立容错机制，提高系统的可靠性，降低资源消耗，实现负载均衡，监控系统性能，积极预防系统故障等方式来保证系统的可用性。',2,1,1,1,NULL,NULL,NULL,NULL),(178,' 请描述一下你所知道···','<QuestionContent>\n  <title> 请描述一下你所知道的负载均衡？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：负载均衡是一种通过对系统资源进行有效分配和管理，使系统的性能和可用性都尽可能达到最佳状态的机制，它可以通过增加服务器的数量，实现多服务器的负载，从而提高系统的可用性和稳定性。',2,1,1,1,NULL,NULL,NULL,NULL),(179,' 如何实现网站的高可···','<QuestionContent>\n  <title> 如何实现网站的高可用性？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:57','答：实现网站的高可用性可以通过建立高可用的系统架构，建立容错机制，提高系统的可靠性，实现负载均衡，监控系统性能，降低资源消耗，积极预防系统故障，优化服务器配置等方式来实现网站的高可用性。',2,1,1,1,NULL,NULL,NULL,NULL),(180,' 如何实现系统的自动···','<QuestionContent>\n  <title> 如何实现系统的自动化部署？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以通过建立自动化部署系统，将代码和资源放置到版本控制工具中，建立配置文件，使用脚本编写部署脚本，实现自动化部署系统的自动化部署。',2,1,1,1,NULL,NULL,NULL,NULL),(181,' 你使用过哪些网络安···','<QuestionContent>\n  <title> 你使用过哪些网络安全工具？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：我使用过TCPdump、Wireshark、Nmap、Netcat、Metasploit、Burp Suite、Aircrack-ng等网络安全工具。',2,1,1,1,NULL,NULL,NULL,NULL),(182,' 请简述一下DDOS···','<QuestionContent>\n  <title> 请简述一下DDOS攻击？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：DDOS攻击是一种威胁网络服务的攻击行为，攻击者通过大量请求消耗服务器资源，从而使服务器无法提供正常的服务。',2,1,1,1,NULL,NULL,NULL,NULL),(183,' 如何保证系统的安全···','<QuestionContent>\n  <title> 如何保证系统的安全性？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：保证系统的安全性可以通过建立安全控制机制，实施系统安全检查，安装防火墙，实施安全监控，使用加密技术，进行安全审计，实施权限控制等方式来实现。',2,1,1,1,NULL,NULL,NULL,NULL),(184,' 如何提高数据库的性···','<QuestionContent>\n  <title> 如何提高数据库的性能？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以通过建立索引，正确设计表结构，正确选择数据类型，避免拼接大量字符串，简化查询语句，合理使用内存表，使用并行查询等方式来提高数据库的性能。',2,1,1,1,NULL,NULL,NULL,NULL),(185,' 请简述一下安全监控···','<QuestionContent>\n  <title> 请简述一下安全监控的作用？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：安全监控的作用是通过定时监控系统，及时发现系统中存在的安全隐患，从而及时采取措施保护系统安全，防止攻击者利用漏洞侵入系统。',2,1,1,1,NULL,NULL,NULL,NULL),(186,' 如何实现多机热备？···','<QuestionContent>\n  <title> 如何实现多机热备？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以通过建立多机热备系统，实现主机和备份机之间的数据同步，当主机出现故障时，通过快速切换实现备份机的上线，从而实现多机热备的功能。',2,1,1,1,NULL,NULL,NULL,NULL),(187,' 如何实现数据库的高···','<QuestionContent>\n  <title> 如何实现数据库的高可用？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以通过建立双主或多主的数据库架构，实现数据库的主备复制，实施数据库容错机制，监控数据库性能，定时备份数据库，优化数据库结构等方式来实现高可用的数据库系统。',2,1,1,1,NULL,NULL,NULL,NULL),(188,' 什么是最长公共子序···','<QuestionContent>\n  <title> 什么是最长公共子序列？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：最长公共子序列（Longest Common Subsequence，LCS）是指在两个序列中找到最长的序列，该序列是两个序列中的每个序列的子序列。',2,1,1,1,NULL,NULL,NULL,NULL),(189,' 如何将一个只有一个···','<QuestionContent>\n  <title> 如何将一个只有一个元素的数组分割成两个数组？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用分治算法，将数组分割成两个数组，其中一个包含只有一个元素，另外一个为空。',2,1,1,1,NULL,NULL,NULL,NULL),(190,' 如何使用递归算法解···','<QuestionContent>\n  <title> 如何使用递归算法解决斐波那契数列问题？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用递归算法来解决斐波那契数列问题，即在数列中任意一个数字的值等于它前两个数字之和，如：F(n)=F(n-1)+F(n-2)。',2,1,1,1,NULL,NULL,NULL,NULL),(191,' 如何使用动态规划算···','<QuestionContent>\n  <title> 如何使用动态规划算法求解最短路径问题？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用动态规划算法来求解最短路径问题，即为了从起点到终点的最短路径，从起点开始，将每个结点当做一个步骤，每一步都可能有若干个可以到达的结点，依次比较各个结点之间的距离，选择最短路径。',2,1,1,1,NULL,NULL,NULL,NULL),(192,' 如何使用贪心算法求···','<QuestionContent>\n  <title> 如何使用贪心算法求解集合覆盖问题？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用贪心算法求解集合覆盖问题，即给定一个集合S，由若干子集组成，要求用最少的子集将S覆盖，可以从S中取出一个未被覆盖的元素，将其加入到覆盖集合中，然后从S中去掉已被覆盖的元素，重复此步骤，直到S中的所有元素都被覆盖。',2,1,1,1,NULL,NULL,NULL,NULL),(193,' 如何使用折半查找算···','<QuestionContent>\n  <title> 如何使用折半查找算法求解排序数组中的元素？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用折半查找算法求解排序数组中的元素，即取出数组中间元素，然后将其与要查找的元素进行比较，若相等，则查找成功；若大于要查找的元素，则在元素左边的子数组中继续查找；若小于要查找的元素，则在元素右边的子数组中继续查找，依次类推，直到找到要查找的元素。',2,1,1,1,NULL,NULL,NULL,NULL),(194,' 如何使用KMP算法···','<QuestionContent>\n  <title> 如何使用KMP算法求解字符串搜索问题？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用KMP算法来求解字符串搜索问题，即给定一个文本串s和一个模式串p，要求在s中查找p出现的位置，可以将模式串p构造出一个部分匹配表，并以该表作为参照，为了避免模式串中出现重复的子串，每次仅移动模式串的相应位置，从而加快搜索的速度。',2,1,1,1,NULL,NULL,NULL,NULL),(195,' 如何使用回溯算法求···','<QuestionContent>\n  <title> 如何使用回溯算法求解八皇后问题？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用回溯算法求解八皇后问题，即在一个8×8的棋盘上放置8个皇后，使其不能互相攻击，可以从第一行开始，每次在一行中，从左至右，依次尝试每一列，若此位置不满足条件，则继续尝试下一列，若已经尝试完所有列，则回溯到上一行，重新尝试，依次类推，直到找到合适的位置。',2,1,1,1,NULL,NULL,NULL,NULL),(196,' 如何使用分支限界算···','<QuestionContent>\n  <title> 如何使用分支限界算法解决0-1背包问题？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用分支限界算法来解决0-1背包问题，即给定一组物品，每种物品有一定的重量和价值，在限定的总重量内，如何让物品总价值最大，可以从根结点开始，将每一种物品放入背包或者不放入背包，并依次计算放入的物品的价值，并选择最大价值的状态，依次类推，直到找到最优解。',2,1,1,1,NULL,NULL,NULL,NULL),(197,' 如何使用分治算法计···','<QuestionContent>\n  <title> 如何使用分治算法计算最大子数组的和？</title>\n  <titleImg></titleImg>\n</QuestionContent>',5,NULL,5,NULL,0,NULL,'admin','2023-05-05 09:08:58','答：可以使用分治算法来计算最大子数组的和，即给定一个数组，要求找出其中任意一个子数组，使其和最大，可以将数组分割成两半，每一半分别求解最大子数组的和，然后再求出跨越中点的最大子数组的和，将三者比较，选择最大的和即为最大子数组的和。',2,1,1,1,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `et_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_question_2_point`
--

DROP TABLE IF EXISTS `et_question_2_point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_question_2_point` (
  `question_2_point_id` int NOT NULL AUTO_INCREMENT,
  `question_id` int DEFAULT NULL,
  `point_id` int DEFAULT NULL,
  PRIMARY KEY (`question_2_point_id`) USING BTREE,
  KEY `fk_question_111` (`question_id`) USING BTREE,
  KEY `fk_point_111` (`point_id`) USING BTREE,
  CONSTRAINT `et_question_2_point_ibfk_1` FOREIGN KEY (`point_id`) REFERENCES `et_knowledge_point` (`point_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `et_question_2_point_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `et_question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=220 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_question_2_point`
--

LOCK TABLES `et_question_2_point` WRITE;
/*!40000 ALTER TABLE `et_question_2_point` DISABLE KEYS */;
INSERT INTO `et_question_2_point` VALUES (21,21,1),(31,31,1),(32,32,1),(33,33,1),(34,34,1),(35,35,1),(36,36,1),(37,37,1),(38,38,1),(39,39,1),(40,40,1),(41,41,1),(42,42,1),(44,44,1),(45,45,1),(66,66,3),(67,67,3),(68,68,3),(69,69,3),(70,70,3),(71,71,3),(72,72,3),(73,73,3),(74,74,3),(75,75,3),(76,76,3),(77,77,3),(78,78,3),(97,97,3),(100,100,3),(101,101,3),(102,102,3),(103,103,3),(105,105,3),(106,106,3),(108,108,3),(121,121,3),(122,122,3),(123,123,3),(124,124,3),(125,125,3),(126,126,3),(127,127,3),(128,128,3),(129,29,3),(130,4,4),(131,5,4),(132,1,4),(133,3,4),(134,6,4),(135,2,4),(136,7,4),(137,8,4),(138,9,4),(139,10,4),(140,11,3),(141,20,3),(142,19,3),(143,18,3),(144,17,3),(145,16,3),(146,15,3),(147,14,3),(148,13,3),(149,12,3),(150,30,3),(151,28,3),(152,27,3),(153,26,3),(154,25,3),(155,24,3),(156,23,3),(157,22,3),(158,52,4),(159,51,4),(160,50,3),(161,49,2),(162,46,1),(163,47,3),(164,48,2),(165,59,4),(166,60,4),(167,58,4),(168,53,4),(169,54,4),(170,55,4),(171,56,4),(172,57,4),(173,61,4),(174,62,4),(175,63,3),(176,64,3),(177,65,3),(179,79,1),(180,80,1),(182,81,1),(183,82,1),(184,83,1),(185,84,1),(186,85,1),(187,86,1),(188,87,1),(189,88,1),(190,89,1),(191,90,1),(192,91,1),(193,92,1),(194,93,1),(195,94,2),(196,95,2),(197,96,3),(200,99,3),(201,98,3),(202,107,1),(203,115,1),(204,109,1),(206,111,1),(207,112,1),(208,113,1),(209,114,1),(210,116,1),(211,117,1),(212,118,1),(214,120,1),(216,43,3),(217,104,2),(218,119,3),(219,110,2);
/*!40000 ALTER TABLE `et_question_2_point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_question_2_tag`
--

DROP TABLE IF EXISTS `et_question_2_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_question_2_tag` (
  `question_tag_id` int NOT NULL AUTO_INCREMENT,
  `question_id` int NOT NULL,
  `tag_id` int NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creator` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`question_tag_id`) USING BTREE,
  KEY `fk_question_tag_tid` (`tag_id`) USING BTREE,
  KEY `fk_question_tag_qid` (`question_id`) USING BTREE,
  CONSTRAINT `fk_question_tag_qid` FOREIGN KEY (`question_id`) REFERENCES `et_question` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_question_tag_tid` FOREIGN KEY (`tag_id`) REFERENCES `et_tag` (`tag_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_question_2_tag`
--

LOCK TABLES `et_question_2_tag` WRITE;
/*!40000 ALTER TABLE `et_question_2_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_question_2_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_question_type`
--

DROP TABLE IF EXISTS `et_question_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_question_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `subjective` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='试题类型';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_question_type`
--

LOCK TABLES `et_question_type` WRITE;
/*!40000 ALTER TABLE `et_question_type` DISABLE KEYS */;
INSERT INTO `et_question_type` VALUES (1,'单选题',0),(2,'多选题',0),(3,'判断题',0),(5,'简答题',1);
/*!40000 ALTER TABLE `et_question_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_r_user_role`
--

DROP TABLE IF EXISTS `et_r_user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_r_user_role` (
  `user_id` int NOT NULL COMMENT '用户ID',
  `role_id` int NOT NULL COMMENT '角色ID',
  KEY `user_id` (`user_id`) USING BTREE,
  KEY `role_id` (`role_id`) USING BTREE,
  CONSTRAINT `et_r_user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `et_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='用户_角色 关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_r_user_role`
--

LOCK TABLES `et_r_user_role` WRITE;
/*!40000 ALTER TABLE `et_r_user_role` DISABLE KEYS */;
INSERT INTO `et_r_user_role` VALUES (4,1),(5,3);
/*!40000 ALTER TABLE `et_r_user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_reference`
--

DROP TABLE IF EXISTS `et_reference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_reference` (
  `reference_id` int NOT NULL AUTO_INCREMENT,
  `reference_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `state` decimal(10,0) NOT NULL DEFAULT '1' COMMENT '1 正常 0 废弃',
  PRIMARY KEY (`reference_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_reference`
--

LOCK TABLES `et_reference` WRITE;
/*!40000 ALTER TABLE `et_reference` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_reference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_role`
--

DROP TABLE IF EXISTS `et_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `authority` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='角色表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_role`
--

LOCK TABLES `et_role` WRITE;
/*!40000 ALTER TABLE `et_role` DISABLE KEYS */;
INSERT INTO `et_role` VALUES (1,'ROLE_ADMIN','超级管理员','admin'),(2,'ROLE_TEACHER','教师','teacher'),(3,'ROLE_STUDENT','学员','student');
/*!40000 ALTER TABLE `et_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_tag`
--

DROP TABLE IF EXISTS `et_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_tag` (
  `tag_id` int NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creator` int NOT NULL,
  `is_private` tinyint(1) NOT NULL DEFAULT '0',
  `memo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`tag_id`) USING BTREE,
  KEY `fk_tag_creator` (`creator`) USING BTREE,
  CONSTRAINT `fk_tag_creator` FOREIGN KEY (`creator`) REFERENCES `et_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_tag`
--

LOCK TABLES `et_tag` WRITE;
/*!40000 ALTER TABLE `et_tag` DISABLE KEYS */;
INSERT INTO `et_tag` VALUES (4,'较难题','2023-05-04 11:15:13',4,0,'错误率较高'),(5,'简单题','2023-05-04 11:15:18',4,0,'基本能对的');
/*!40000 ALTER TABLE `et_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_user`
--

DROP TABLE IF EXISTS `et_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK',
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '账号',
  `truename` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '真实姓名',
  `password` char(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `add_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `expire_date` timestamp NULL DEFAULT NULL,
  `add_by` int DEFAULT NULL COMMENT '创建人',
  `enabled` tinyint(1) DEFAULT '0' COMMENT '激活状态：0-未激活 1-激活',
  `field_id` int NOT NULL,
  `last_login_time` timestamp NULL DEFAULT NULL,
  `login_time` timestamp NULL DEFAULT NULL,
  `province` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `company` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `department` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_user`
--

LOCK TABLES `et_user` WRITE;
/*!40000 ALTER TABLE `et_user` DISABLE KEYS */;
INSERT INTO `et_user` VALUES (4,'admin',NULL,'260acbffd3c30786febc29d7dd71a9880a811e77','1@1.1',NULL,'2023-05-05 00:36:48',NULL,NULL,1,1,'2023-05-05 00:03:42','2023-05-05 00:36:49',NULL,'2','3'),(5,'user01',NULL,'b313c806131f17b53d83d8bfecb5f0f7b68486fb','no@no.no',NULL,'2023-05-05 00:26:06',NULL,NULL,1,1,NULL,'2023-05-05 00:26:07',NULL,NULL,NULL);
/*!40000 ALTER TABLE `et_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_user_exam_history`
--

DROP TABLE IF EXISTS `et_user_exam_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_user_exam_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `exam_paper_id` int NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `answer_sheet` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `duration` int NOT NULL,
  `point_get` float(10,1) NOT NULL DEFAULT '0.0',
  `submit_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_user_exam_history`
--

LOCK TABLES `et_user_exam_history` WRITE;
/*!40000 ALTER TABLE `et_user_exam_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_user_exam_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `et_user_question_history_t`
--

DROP TABLE IF EXISTS `et_user_question_history_t`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `et_user_question_history_t` (
  `user_question_hist_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `user_question_hist` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `modify_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_question_hist_id`) USING BTREE,
  UNIQUE KEY `idx_u_q_hist_userid` (`user_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `et_user_question_history_t`
--

LOCK TABLES `et_user_question_history_t` WRITE;
/*!40000 ALTER TABLE `et_user_question_history_t` DISABLE KEYS */;
/*!40000 ALTER TABLE `et_user_question_history_t` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_c3p0`
--

DROP TABLE IF EXISTS `t_c3p0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_c3p0` (
  `a` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_c3p0`
--

LOCK TABLES `t_c3p0` WRITE;
/*!40000 ALTER TABLE `t_c3p0` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_c3p0` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05 17:09:23
