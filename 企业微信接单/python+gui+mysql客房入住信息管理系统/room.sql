create database room;
use room;
DROP TABLE IF EXISTS `customer_info`;
CREATE TABLE `customer_info` (
  `customer_id` int(0) NOT NULL,
  `room_id` int(0) NOT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NULL DEFAULT NULL,
  `total_cost` decimal(10, 2) NULL DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`customer_id`),
  INDEX `room_id`(`room_id`),
  CONSTRAINT `customer_info_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room_info` (`room_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
);

INSERT INTO `customer_info` VALUES (1, 1, '2023-06-21', '2023-06-23', 200.00, '张三');
INSERT INTO `customer_info` VALUES (2, 2, '2023-06-21', '2023-06-25', 300.00, '王五');
INSERT INTO `customer_info` VALUES (3, 3, '2023-06-22', '2023-06-26', 400.00, '刘麻子');
INSERT INTO `customer_info` VALUES (4, 4, '2023-06-23', '2023-06-30', 900.00, '小猫');
INSERT INTO `customer_info` VALUES (5, 5, '2023-06-24', '2023-06-29', 750.00, '小月月');
INSERT INTO `customer_info` VALUES (6, 6, '2023-06-25', '2023-06-28', 540.00, '洋洋');
INSERT INTO `customer_info` VALUES (7, 7, '2023-06-26', '2023-06-27', 90.00, '沸羊羊');
INSERT INTO `customer_info` VALUES (8, 8, '2023-06-27', '2023-06-29', 240.00, '舔狗');

DROP TABLE IF EXISTS `room_info`;
CREATE TABLE `room_info` (
  `room_id` int(0) NOT NULL,
  `type_id` int(0) NOT NULL,
  `room_number` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT 'Vacant',
  PRIMARY KEY (`room_id`),
  UNIQUE INDEX `room_number`(`room_number`),
  CONSTRAINT `room_info_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `room_type` (`type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
);

INSERT INTO `room_info` VALUES (1, 1, '101', 'Vacant');
INSERT INTO `room_info` VALUES (2, 2, '102', 'Vacant');
INSERT INTO `room_info` VALUES (3, 3, '103', 'Vacant');
INSERT INTO `room_info` VALUES (4, 4, '104', 'Vacant');
INSERT INTO `room_info` VALUES (5, 5, '105', 'Vacant');
INSERT INTO `room_info` VALUES (6, 6, '201', 'Vacant');
INSERT INTO `room_info` VALUES (7, 7, '202', 'Vacant');
INSERT INTO `room_info` VALUES (8, 8, '203', 'Vacant');

DROP TABLE IF EXISTS `room_price`;
CREATE TABLE `room_price` (
  `price_id` int(0) NOT NULL,
  `type_id` int(0) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`price_id`),
  CONSTRAINT `room_price_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `room_type` (`type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
);

INSERT INTO `room_price` VALUES (1, 1, '2023-06-21', '2023-06-30', 100.00);
INSERT INTO `room_price` VALUES (2, 2, '2023-06-21', '2023-06-30', 150.00);
INSERT INTO `room_price` VALUES (3, 3, '2023-06-21', '2023-06-30', 200.00);
INSERT INTO `room_price` VALUES (4, 4, '2023-06-21', '2023-06-30', 300.00);
INSERT INTO `room_price` VALUES (5, 5, '2023-06-21', '2023-06-30', 250.00);
INSERT INTO `room_price` VALUES (6, 6, '2023-06-21', '2023-06-30', 180.00);
INSERT INTO `room_price` VALUES (7, 7, '2023-06-21', '2023-06-30', 90.00);
INSERT INTO `room_price` VALUES (8, 8, '2023-06-21', '2023-06-30', 120.00);

DROP TABLE IF EXISTS `room_type`;
CREATE TABLE `room_type` (
  `type_id` int(0) NOT NULL,
  `type_name` varchar(50) NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`type_id`)
);

INSERT INTO `room_type` VALUES (1, 'Standard', 100.00);
INSERT INTO `room_type` VALUES (2, 'Deluxe', 150.00);
INSERT INTO `room_type` VALUES (3, 'Suite', 200.00);
INSERT INTO `room_type` VALUES (4, 'VIP', 300.00);
INSERT INTO `room_type` VALUES (5, 'Family', 250.00);
INSERT INTO `room_type` VALUES (6, 'Executive', 180.00);
INSERT INTO `room_type` VALUES (7, 'Single', 90.00);
INSERT INTO `room_type` VALUES (8, 'Double', 120.00);

DROP VIEW IF EXISTS `vacant_rooms_view`;
CREATE VIEW `vacant_rooms_view` AS SELECT `ri`.`room_id`, `ri`.`room_number`, `rt`.`type_name` FROM `room_info` `ri` JOIN `room_type` `rt` ON `ri`.`type_id` = `rt`.`type_id` WHERE `ri`.`status` = 'Vacant';

DROP PROCEDURE IF EXISTS `calculate_cost`;
DELIMITER ;;
CREATE PROCEDURE `calculate_cost`(IN start_date DATE, IN end_date DATE)
BEGIN
    SELECT rt.type_name, SUM(DATEDIFF(ci.check_out_date, ci.check_in_date)) AS total_days, SUM(rp.price * DATEDIFF(ci.check_out_date, ci.check_in_date)) AS total_cost
    FROM customer_info ci
    JOIN room_info ri ON ci.room_id = ri.room_id
    JOIN room_type rt ON ri.type_id = rt.type_id
    JOIN room_price rp ON rt.type_id = rp.type_id AND ci.check_in_date >= rp.start_date AND ci.check_out_date <= rp.end_date
    WHERE (ci.check_in_date BETWEEN start_date AND end_date) OR (ci.check_out_date BETWEEN start_date AND end_date)
    GROUP BY rt.type_name;
END
;;
DELIMITER ;

DROP TRIGGER IF EXISTS `check_in_trigger`;
DELIMITER ;;
CREATE TRIGGER `check_in_trigger` AFTER INSERT ON `customer_info` FOR EACH ROW BEGIN
    UPDATE room_info SET status = 'Occupied' WHERE room_id = NEW.room_id;
END
;;
DELIMITER ;

DROP TRIGGER IF EXISTS `check_out_trigger`;
DELIMITER ;;
CREATE TRIGGER `check_out_trigger` AFTER UPDATE ON `customer_info` FOR EACH ROW BEGIN
    IF NEW.check_out_date IS NOT NULL THEN
        UPDATE room_info SET status = 'Vacant' WHERE room_id = NEW.room_id;
    END IF;
END
;;
DELIMITER ;
