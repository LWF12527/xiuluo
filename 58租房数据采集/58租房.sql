CREATE TABLE `cdiscount_collect_queue`
(
    `id`          bigint(20)   NOT NULL AUTO_INCREMENT,
    `sku_id`      varchar(40)  NOT NULL DEFAULT '' COMMENT '产品/变体idOffre',
    `product_url` varchar(500) NOT NULL COMMENT '采集链接',
    `ass_q_id`    int(11)      NOT NULL DEFAULT '0' COMMENT '关联cdiscount_category主键',
    `page1`       int(11)      NOT NULL DEFAULT '0' COMMENT '热销前5页page，便于调试',
    `page2`       int(11)      NOT NULL DEFAULT '0' COMMENT '评论全部页面page，便于调试',
    `sync_status` tinyint(1)   NOT NULL DEFAULT '0' COMMENT '执行状态：0未执行，1完成，2下架',
    `sync_count`  tinyint(1)   NOT NULL DEFAULT '0' COMMENT '执行次数',
    `sync_result` tinytext COMMENT '错误记录',
    `create_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
    PRIMARY KEY (`id`) USING BTREE,
    UNIQUE KEY `uniq_sku_id` (`sku_id`) USING BTREE,
    KEY `idx_ass_q_id` (`sku_id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 3932473
  DEFAULT CHARSET = utf8mb4 COMMENT ='cdiscount产品队列表';

