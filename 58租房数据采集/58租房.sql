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