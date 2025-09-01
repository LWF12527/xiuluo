

DROP DATABASE if exists `jf`;

CREATE DATABASE if not exists `jf` DEFAULT CHARACTER SET gb2312;

USE `jf`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `id` int(4) NOT NULL auto_increment,
  `username` varchar(50) default NULL,
  `password` varchar(50) default NULL,
  `creattime` datetime default NULL,
  `flag` int(4) default NULL,
  `isuse` int(4) default NULL,
  `logintimes` int(4) default NULL,
  `quanxian` varchar(1000) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=gb2312;

/*Data for the table `admin` */

insert  into `admin`(`id`,`username`,`password`,`creattime`,`flag`,`isuse`,`logintimes`,`quanxian`) values (1,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','0000-00-00 00:00:00',1,1,90,'1');

/*Table structure for table `adminlog` */

DROP TABLE IF EXISTS `adminlog`;

CREATE TABLE `adminlog` (
  `id` int(4) NOT NULL auto_increment,
  `username` varchar(50) default NULL,
  `password` varchar(50) default NULL,
  `logintime` datetime default NULL,
  `loginip` varchar(50) default NULL,
  `useros` varchar(50) default NULL,
  `ok` varchar(50) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=gb2312;

/*Data for the table `adminlog` */

insert  into `adminlog`(`id`,`username`,`password`,`logintime`,`loginip`,`useros`,`ok`) values (29,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-02-29 11:13:05','Mozilla/4.0 (compatible','127.0.0.1','true'),(30,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 14:58:30','Mozilla/4.0 (compatible','127.0.0.1','true'),(31,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:13:32','Mozilla/4.0 (compatible','127.0.0.1','true'),(32,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:22:56','Mozilla/4.0 (compatible','127.0.0.1','true'),(33,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:33:37','Mozilla/4.0 (compatible','127.0.0.1','true'),(34,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:34:00','Mozilla/4.0 (compatible','127.0.0.1','true'),(35,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:36:26','Mozilla/4.0 (compatible','127.0.0.1','true'),(36,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:37:09','Mozilla/4.0 (compatible','127.0.0.1','true'),(37,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:37:15','Mozilla/4.0 (compatible','127.0.0.1','true'),(38,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-12 15:37:30','Mozilla/4.0 (compatible','127.0.0.1','true'),(39,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 12:58:28','Mozilla/4.0 (compatible','127.0.0.1','true'),(40,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 12:59:28','Mozilla/4.0 (compatible','127.0.0.1','true'),(41,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 12:59:44','Mozilla/4.0 (compatible','127.0.0.1','true'),(42,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 13:04:56','Mozilla/4.0 (compatible','127.0.0.1','true'),(43,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 13:10:36','Mozilla/4.0 (compatible','127.0.0.1','true'),(44,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 13:28:40','Mozilla/4.0 (compatible','127.0.0.1','true'),(45,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 15:21:04','Mozilla/4.0 (compatible','127.0.0.1','true'),(46,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 15:27:47','Mozilla/4.0 (compatible','127.0.0.1','true'),(47,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 15:51:13','Mozilla/4.0 (compatible','127.0.0.1','true'),(48,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:09:10','Mozilla/4.0 (compatible','127.0.0.1','true'),(49,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:15:01','Mozilla/4.0 (compatible','127.0.0.1','true'),(50,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:17:11','Mozilla/4.0 (compatible','127.0.0.1','true'),(51,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:17:38','Mozilla/4.0 (compatible','127.0.0.1','true'),(52,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:28:44','Mozilla/4.0 (compatible','127.0.0.1','true'),(53,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:30:54','Mozilla/4.0 (compatible','127.0.0.1','true'),(54,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-28 16:32:23','Mozilla/4.0 (compatible','127.0.0.1','true'),(55,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-29 01:23:04','Mozilla/4.0 (compatible','127.0.0.1','true'),(56,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-29 01:25:03','Mozilla/4.0 (compatible','127.0.0.1','true'),(57,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-03-29 01:25:49','Mozilla/4.0 (compatible','127.0.0.1','true'),(58,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 17:36:23','Mozilla/4.0 (compatible','127.0.0.1','true'),(59,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 17:40:36','Mozilla/4.0 (compatible','127.0.0.1','true'),(60,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 17:44:41','Mozilla/4.0 (compatible','127.0.0.1','true'),(61,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 17:57:03','Mozilla/4.0 (compatible','127.0.0.1','true'),(62,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 18:38:59','Mozilla/4.0 (compatible','127.0.0.1','true'),(63,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 18:43:14','Mozilla/4.0 (compatible','127.0.0.1','true'),(64,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-03 19:04:01','Mozilla/4.0 (compatible','127.0.0.1','true'),(65,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 11:44:38','Mozilla/4.0 (compatible','127.0.0.1','true'),(66,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 11:50:07','Mozilla/4.0 (compatible','127.0.0.1','true'),(67,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 11:50:51','Mozilla/4.0 (compatible','127.0.0.1','true'),(68,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 12:46:03','Mozilla/4.0 (compatible','127.0.0.1','true'),(69,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 12:53:08','Mozilla/4.0 (compatible','127.0.0.1','true'),(70,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 13:26:45','Mozilla/4.0 (compatible','127.0.0.1','true'),(71,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 13:55:59','Mozilla/4.0 (compatible','127.0.0.1','true'),(72,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 13:57:21','Mozilla/4.0 (compatible','127.0.0.1','true'),(73,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 13:58:12','Mozilla/4.0 (compatible','127.0.0.1','true'),(74,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 14:41:57','Mozilla/4.0 (compatible','127.0.0.1','true'),(75,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 14:42:25','Mozilla/4.0 (compatible','127.0.0.1','true'),(76,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 14:48:23','Mozilla/4.0 (compatible','127.0.0.1','true'),(77,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 14:49:25','Mozilla/4.0 (compatible','127.0.0.1','true'),(78,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 14:49:52','Mozilla/4.0 (compatible','127.0.0.1','true'),(79,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 14:50:17','Mozilla/4.0 (compatible','127.0.0.1','true'),(80,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 15:07:33','Mozilla/4.0 (compatible','127.0.0.1','true'),(81,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 15:07:44','Mozilla/4.0 (compatible','127.0.0.1','true'),(82,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 15:08:04','Mozilla/4.0 (compatible','127.0.0.1','true'),(83,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 15:36:53','Mozilla/4.0 (compatible','127.0.0.1','true'),(84,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 15:39:38','Mozilla/4.0 (compatible','127.0.0.1','true'),(85,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 16:27:43','Mozilla/4.0 (compatible','127.0.0.1','true'),(86,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 16:51:30','Mozilla/4.0 (compatible','127.0.0.1','true'),(87,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 16:51:42','Mozilla/4.0 (compatible','127.0.0.1','true'),(88,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 17:25:18','Mozilla/4.0 (compatible','127.0.0.1','true'),(89,'admin','ae7783f0ae4cb82dfe39bb4ec4a53047','2012-04-12 17:36:58','Mozilla/4.0 (compatible','127.0.0.1','true');

/*Table structure for table `cz` */

DROP TABLE IF EXISTS `cz`;

CREATE TABLE `cz` (
  `id` int(4) NOT NULL auto_increment,
  `hykid` varchar(50) default NULL,
  `je` float default NULL,
  `sj` varchar(50) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=gb2312;

/*Data for the table `cz` */

insert  into `cz`(`id`,`hykid`,`je`,`sj`) values (3,'3',300,'2012-04-12'),(4,'2',180,'2012-04-12'),(5,'3',10000,'2012-04-12');

/*Table structure for table `dh` */

DROP TABLE IF EXISTS `dh`;

CREATE TABLE `dh` (
  `id` int(4) NOT NULL auto_increment,
  `dhspid` varchar(50) default NULL,
  `hykid` varchar(50) default NULL,
  `syjf` float default NULL,
  `sj` varchar(50) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312;

/*Data for the table `dh` */

insert  into `dh`(`id`,`dhspid`,`hykid`,`syjf`,`sj`) values (2,'2','3',2000,'2012-04-12'),(3,'2','3',2000,'2012-04-12');

/*Table structure for table `dhsp` */

DROP TABLE IF EXISTS `dhsp`;

CREATE TABLE `dhsp` (
  `id` int(4) NOT NULL auto_increment,
  `mc` varchar(50) default NULL,
  `jf` float default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312;

/*Data for the table `dhsp` */

insert  into `dhsp`(`id`,`mc`,`jf`) values (2,'半导体收音机',2000),(3,'沐浴露',1000);

/*Table structure for table `guestbook` */

DROP TABLE IF EXISTS `guestbook`;

CREATE TABLE `guestbook` (
  `id` int(4) NOT NULL auto_increment,
  `nickname` varchar(100) default NULL,
  `pic` varchar(100) default NULL,
  `email` varchar(50) default NULL,
  `qq` varchar(50) default NULL,
  `weburl` varchar(50) default NULL,
  `blogurl` varchar(50) default NULL,
  `expressions` varchar(50) default NULL,
  `content` varchar(200) default NULL,
  `addtime` datetime default NULL,
  `ip` varchar(50) default NULL,
  `replay` int(4) default NULL,
  `ifhide` int(4) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=gb2312;

/*Data for the table `guestbook` */

insert  into `guestbook`(`id`,`nickname`,`pic`,`email`,`qq`,`weburl`,`blogurl`,`expressions`,`content`,`addtime`,`ip`,`replay`,`ifhide`) values (5,'游客','images/nobody.gif','','','','','images/face/1.gif','我要找工作','2012-04-28 15:50:33','127.0.0.1',1,1);

/*Table structure for table `hy` */

DROP TABLE IF EXISTS `hy`;

CREATE TABLE `hy` (
  `id` int(4) NOT NULL auto_increment,
  `xm` varchar(50) default NULL,
  `xb` varchar(50) default NULL,
  `cs` varchar(50) default NULL,
  `fm` varchar(50) default NULL,
  `zz` varchar(50) default NULL,
  `dh` varchar(50) default NULL,
  `yx` varchar(50) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312;

/*Data for the table `hy` */

insert  into `hy`(`id`,`xm`,`xb`,`cs`,`fm`,`zz`,`dh`,`yx`) values (2,'张三','男','21122019900909123','04-12','青年大街108号','13800000000','130@163.com'),(3,'莉莉','女','21122019900909123','09-09','前门大街','13200000000','111@163.com');

/*Table structure for table `hyk` */

DROP TABLE IF EXISTS `hyk`;

CREATE TABLE `hyk` (
  `id` int(4) NOT NULL auto_increment,
  `kh` varchar(50) default NULL,
  `xm` varchar(50) default NULL,
  `rq` varchar(50) default NULL,
  `je` float default NULL,
  `sd` varchar(50) default '未',
  `gs` varchar(50) default '未',
  `jf` float default '0',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312;

/*Data for the table `hyk` */

insert  into `hyk`(`id`,`kh`,`xm`,`rq`,`je`,`sd`,`gs`,`jf`) values (2,'K201200001','2','2012-04-12',1180,'未','未',0),(3,'K1234567890','3','2012-04-12',10800,'未','未',0);

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `id` int(4) NOT NULL auto_increment,
  `username` varchar(50) default NULL,
  `password` varchar(50) default NULL,
  `type` varchar(50) default NULL,
  `regtime` varchar(50) default NULL,
  `ifuse` int(4) default NULL,
  `logintimes` int(4) default NULL,
  `lasttime` datetime default NULL,
  `lastip` varchar(50) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=gb2312;

/*Data for the table `member` */

insert  into `member`(`id`,`username`,`password`,`type`,`regtime`,`ifuse`,`logintimes`,`lasttime`,`lastip`) values (1,'xiaoqiang','96e79218965eb72c92a549dd5a330112','person','2012-03-01 12:00:00',1,23,'2012-04-12 17:46:01','127.0.0.1'),(2,'xiaoniu','96e79218965eb72c92a549dd5a330112','person','2012-03-29 00:30:40',1,7,'2012-04-03 19:00:34','127.0.0.1');

/*Table structure for table `pmember` */

DROP TABLE IF EXISTS `pmember`;

CREATE TABLE `pmember` (
  `id` int(4) NOT NULL auto_increment,
  `mid` int(4) default NULL,
  `realname` varchar(100) default NULL,
  `sex` varchar(50) default NULL,
  `bir` varchar(50) default NULL,
  `sheng` varchar(50) default NULL,
  `city` varchar(50) default NULL,
  `telphone` varchar(50) default NULL,
  `email` varchar(50) default NULL,
  `question` varchar(100) default NULL,
  `answer` varchar(100) default NULL,
  `address` varchar(100) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=gb2312;

/*Data for the table `pmember` */

insert  into `pmember`(`id`,`mid`,`realname`,`sex`,`bir`,`sheng`,`city`,`telphone`,`email`,`question`,`answer`,`address`) values (1,1,'xiaoqiang','男','21122019900909121','甘肃','天水','02488888888','xiaoqiang@163.com','我是谁','小强','测试'),(2,2,'莉莉','女','212124244','江苏','南京','02088888888','11@163.com','11','22','雨花台路100号');

/*Table structure for table `replay` */

DROP TABLE IF EXISTS `replay`;

CREATE TABLE `replay` (
  `id` int(4) NOT NULL auto_increment,
  `mid` int(4) default NULL,
  `replay` varchar(200) default NULL,
  `replayer` varchar(50) default NULL,
  `replaytime` datetime default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=gb2312;

/*Data for the table `replay` */

insert  into `replay`(`id`,`mid`,`replay`,`replayer`,`replaytime`) values (4,5,'no','admin','2012-04-29 01:27:06');

/*Table structure for table `sp` */

DROP TABLE IF EXISTS `sp`;

CREATE TABLE `sp` (
  `id` int(4) NOT NULL auto_increment,
  `mc` varchar(50) default NULL,
  `js` varchar(50) default NULL,
  `jg` float default NULL,
  `jf` float default NULL,
  `bj` int(4) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312;

/*Data for the table `sp` */

insert  into `sp`(`id`,`mc`,`js`,`jg`,`jf`,`bj`) values (2,'IPhone4S','20',4800,2000,5),(3,'松下吹风机','100',180,100,10);

/*Table structure for table `system` */

DROP TABLE IF EXISTS `system`;

CREATE TABLE `system` (
  `id` int(4) NOT NULL auto_increment,
  `sitename` varchar(100) default NULL,
  `url` varchar(100) default NULL,
  `keyword` varchar(100) default NULL,
  `description` varchar(100) default NULL,
  `email` varchar(100) default NULL,
  `state` varchar(100) default NULL,
  `reasons` varchar(100) default NULL,
  `dir` varchar(100) default NULL,
  `record` varchar(100) default NULL,
  `copyright` text,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=gb2312;

/*Data for the table `system` */

insert  into `system`(`id`,`sitename`,`url`,`keyword`,`description`,`email`,`state`,`reasons`,`dir`,`record`,`copyright`) values (1,'超市会员积分管理系统','超市会员积分管理系统','超市会员积分管理系统','超市会员积分管理系统','超市会员积分管理系统','open','超市会员积分管理系统','admin','超市会员积分管理系统','超市会员积分管理系统');

/*Table structure for table `xs` */

DROP TABLE IF EXISTS `xs`;

CREATE TABLE `xs` (
  `id` int(4) NOT NULL auto_increment,
  `spid` varchar(50) default NULL,
  `hykid` varchar(50) default NULL,
  `sl` int(4) default NULL,
  `je` float default NULL,
  `jf` float default NULL,
  `sj` varchar(50) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=gb2312;

/*Data for the table `xs` */

insert  into `xs`(`id`,`spid`,`hykid`,`sl`,`je`,`jf`,`sj`) values (2,'3','3',1,180,100,'2012-04-12'),(3,'2','3',1,4800,2000,'2012-04-12'),(4,'2','3',1,4800,2000,'2012-04-12');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
