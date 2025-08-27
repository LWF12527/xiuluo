CREATE TABLE `58_queue` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `city` varchar(100) NOT NULL DEFAULT '' COMMENT '城市',
  `area` varchar(100) NOT NULL DEFAULT '' COMMENT '区域',
  `area_pingyin` varchar(100) NOT NULL DEFAULT '' COMMENT '区域拼音--参考网站拼音-有的需要加上城市缩写',
  `min_price` varchar(100) NOT NULL DEFAULT '' COMMENT '最低价格',
  `max_price` varchar(100) NOT NULL DEFAULT '' COMMENT '最高价格',
  `house_type` enum('不限','一室','两室','三室','四室','四室以上') NOT NULL DEFAULT '不限' COMMENT '房源类型: 不限、一室、两室、三室、四室、四室以上',
  `rental_mode` enum('不限','租房','合租/单间') NOT NULL DEFAULT '不限' COMMENT '租赁类型: ''不限'',''租房'',''合租/单间''',
  `current_page` int(11) NOT NULL DEFAULT '0' COMMENT '已完成执行页数',
  `max_pages` int(11) NOT NULL DEFAULT '5' COMMENT '采集最大页数',
  `sync_status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态：0未执行 1已完成',
  `retry_count` tinyint(1) NOT NULL DEFAULT '0' COMMENT '重试次数',
  `error_log` text COMMENT '错误信息',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_task` (`area`,`min_price`,`house_type`,`rental_mode`) USING BTREE COMMENT '任务唯一索引'
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COMMENT='58采集任务队列表';

CREATE TABLE `58_detail` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL DEFAULT '' COMMENT '标题',
  `price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '价格',
  `area_size` varchar(50) NOT NULL DEFAULT '' COMMENT '面积(平方米)',
  `location` varchar(200) NOT NULL DEFAULT '' COMMENT '位置',
  `pic_urls` text COMMENT '图片链接',
  `detail_url` varchar(500) NOT NULL DEFAULT '' COMMENT '详情链接',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_detail` (`detail_url`(200)) COMMENT '详情链接唯一索引',
  KEY `idx_price` (`price`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='58房源详情表';

INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (1, '北京', '朝阳', 'chaoyang', '1000', '3000', '两室', '合租/单间', 0, 10, 0, 0, '', '2025-08-27 09:52:32', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (2, '合肥', '包河', 'baohe', '500', '1000', '三室', '不限', 0, 10, 0, 0, '', '2025-08-27 09:53:16', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (6, '合肥', '蜀山', 'shushanqu', '1000', '3000', '不限', '租房', 0, 10, 0, 0, '', '2025-08-27 14:24:30', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (7, '合肥', '瑶海', 'yaohai', '1000', '1500', '不限', '不限', 0, 10, 0, 0, '', '2025-08-27 14:26:09', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (8, '合肥', '长丰', 'changfenghf', '500', '3000', '不限', '不限', 0, 10, 0, 0, '', '2025-08-27 14:27:18', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (9, '武汉', '武昌', 'wuchang', '1500', '3000', '四室', '租房', 0, 10, 0, 0, '', '2025-08-27 14:27:48', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (10, '武汉', '江下', 'jiangxia', '500', '3000', '一室', '不限', 0, 10, 0, 0, '', '2025-08-27 14:28:33', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (11, '广州', '天河', 'tianhe', '1500', '3000', '两室', '合租/单间', 0, 10, 0, 0, '', '2025-08-27 14:29:24', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (12, '广州', '番禺', 'panyu', '500', '3000', '不限', '租房', 0, 10, 0, 0, '', '2025-08-27 14:29:39', '2025-08-27 16:35:17');
INSERT INTO `bstcollect_dev`.`58_queue` (`id`, `city`, `area`, `area_pingyin`, `min_price`, `max_price`, `house_type`, `rental_mode`, `current_page`, `max_pages`, `sync_status`, `retry_count`, `error_log`, `create_time`, `update_time`) VALUES (13, '深圳', '龙岗', 'longgang', '1000', '5000', '不限', '不限', 0, 10, 0, 0, '', '2025-08-27 14:30:40', '2025-08-27 16:35:17');
