/*
 Navicat Premium Data Transfer

 Source Server         : abc
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : shoping

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 20/06/2023 12:03:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `order_id` int(0) NOT NULL,
  `user_id` int(0) NULL DEFAULT NULL,
  `product_id` int(0) NULL DEFAULT NULL,
  `quantity` int(0) NOT NULL,
  `order_date` date NOT NULL,
  PRIMARY KEY (`order_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `product_id`(`product_id`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (1, 1, 1, 2, '2023-06-01');
INSERT INTO `orders` VALUES (2, 2, 2, 1, '2023-06-02');
INSERT INTO `orders` VALUES (3, 3, 3, 3, '2023-06-03');
INSERT INTO `orders` VALUES (4, 4, 4, 2, '2023-06-04');
INSERT INTO `orders` VALUES (5, 5, 5, 1, '2023-06-05');
INSERT INTO `orders` VALUES (6, 6, 6, 3, '2023-06-06');
INSERT INTO `orders` VALUES (7, 7, 7, 2, '2023-06-07');
INSERT INTO `orders` VALUES (8, 8, 8, 1, '2023-06-08');
INSERT INTO `orders` VALUES (9, 9, 9, 3, '2023-06-09');
INSERT INTO `orders` VALUES (10, 10, 10, 2, '2023-06-10');

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products`  (
  `product_id` int(0) NOT NULL,
  `product_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `shop_id` int(0) NULL DEFAULT NULL,
  `stock` int(0) UNSIGNED NOT NULL DEFAULT 0,
  `price` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`product_id`) USING BTREE,
  INDEX `shop_id`(`shop_id`) USING BTREE,
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`shop_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of products
-- ----------------------------
INSERT INTO `products` VALUES (1, 'Product 1', 1, 0, 10.00);
INSERT INTO `products` VALUES (2, 'Product 2', 2, 0, 20.00);
INSERT INTO `products` VALUES (3, 'Product 3', 3, 0, 30.00);
INSERT INTO `products` VALUES (4, 'Product 4', 4, 0, 40.00);
INSERT INTO `products` VALUES (5, 'Product 5', 5, 0, 50.00);
INSERT INTO `products` VALUES (6, 'Product 6', 6, 0, 60.00);
INSERT INTO `products` VALUES (7, 'Product 7', 7, 0, 70.00);
INSERT INTO `products` VALUES (8, 'Product 8', 8, 0, 80.00);
INSERT INTO `products` VALUES (9, 'Product 9', 9, 0, 90.00);
INSERT INTO `products` VALUES (10, 'Product 10', 10, 0, 100.00);

-- ----------------------------
-- Table structure for shops
-- ----------------------------
DROP TABLE IF EXISTS `shops`;
CREATE TABLE `shops`  (
  `shop_id` int(0) NOT NULL,
  `shop_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`shop_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shops
-- ----------------------------
INSERT INTO `shops` VALUES (1, 'Shop 1', 'Shop Address 1', 'Shop Phone 1');
INSERT INTO `shops` VALUES (2, 'Shop 2', 'Shop Address 2', 'Shop Phone 2');
INSERT INTO `shops` VALUES (3, 'Shop 3', 'Shop Address 3', 'Shop Phone 3');
INSERT INTO `shops` VALUES (4, 'Shop 4', 'Shop Address 4', 'Shop Phone 4');
INSERT INTO `shops` VALUES (5, 'Shop 5', 'Shop Address 5', 'Shop Phone 5');
INSERT INTO `shops` VALUES (6, 'Shop 6', 'Shop Address 6', 'Shop Phone 6');
INSERT INTO `shops` VALUES (7, 'Shop 7', 'Shop Address 7', 'Shop Phone 7');
INSERT INTO `shops` VALUES (8, 'Shop 8', 'Shop Address 8', 'Shop Phone 8');
INSERT INTO `shops` VALUES (9, 'Shop 9', 'Shop Address 9', 'Shop Phone 9');
INSERT INTO `shops` VALUES (10, 'Shop 10', 'Shop Address 10', 'Shop Phone 10');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_id` int(0) NOT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `gender` enum('Male','Female') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'user1', 'password1', 'Male', '1234567890', 'Address 1');
INSERT INTO `users` VALUES (2, 'user2', 'password2', 'Female', '0987654321', 'Address 2');
INSERT INTO `users` VALUES (3, 'user3', 'password3', 'Male', '1111111111', 'Address 3');
INSERT INTO `users` VALUES (4, 'user4', 'password4', 'Female', '2222222222', 'Address 4');
INSERT INTO `users` VALUES (5, 'user5', 'password5', 'Male', '3333333333', 'Address 5');
INSERT INTO `users` VALUES (6, 'user6', 'password6', 'Female', '4444444444', 'Address 6');
INSERT INTO `users` VALUES (7, 'user7', 'password7', 'Male', '5555555555', 'Address 7');
INSERT INTO `users` VALUES (8, 'user8', 'password8', 'Female', '6666666666', 'Address 8');
INSERT INTO `users` VALUES (9, 'user9', 'password9', 'Male', '7777777777', 'Address 9');
INSERT INTO `users` VALUES (10, 'user10', 'password10', 'Female', '8888888888', 'Address 10');

-- ----------------------------
-- View structure for v_commodity
-- ----------------------------
DROP VIEW IF EXISTS `v_commodity`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_commodity` AS select `products`.`product_id` AS `product_id`,`products`.`product_name` AS `product_name`,`products`.`shop_id` AS `shop_id`,`products`.`stock` AS `stock`,`products`.`price` AS `price` from `products`;

-- ----------------------------
-- Procedure structure for pc_wg
-- ----------------------------
DROP PROCEDURE IF EXISTS `pc_wg`;
delimiter ;;
CREATE PROCEDURE `pc_wg`(IN p_order_id INT, IN p_user_id INT, IN p_product_id INT, IN p_quantity INT)
BEGIN
  DECLARE user_exists INT;
  DECLARE product_stock INT;
  
  -- a) 按用户ID查询用户信息，判断是否存在
  SELECT COUNT(*) INTO user_exists FROM users WHERE user_id = p_user_id;
  
  IF user_exists = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User does not exist';
  END IF;
  
  -- b) 按商品ID查询商品信息，若库存不为零，则进行网购处理，否则，结束
  SELECT stock INTO product_stock FROM products WHERE product_id = p_product_id;
  
  IF product_stock = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product is out of stock';
  END IF;
  
  -- c) 网购处理：为表orders添加一条网购记录
  INSERT INTO orders (order_id, user_id, product_id, quantity, order_date)
  VALUES (p_order_id, p_user_id, p_product_id, p_quantity, CURDATE());
  
  -- d) products（商品）表中被网购商品ID的当前库存（减网购的数量）
  UPDATE products SET stock = stock - p_quantity WHERE product_id = p_product_id;
  
  SELECT 'Purchase successful' AS message;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
