/*
 Navicat Premium Data Transfer

 Source Server         : abc
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : dingdan

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 20/06/2023 21:57:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


CREATE DATABASE dingdan;
Use dingdan;

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
INSERT INTO `orders` VALUES (1, 1, 1, 5, '2023-06-01');
INSERT INTO `orders` VALUES (2, 2, 3, 2, '2023-06-02');
INSERT INTO `orders` VALUES (3, 3, 5, 1, '2023-06-03');
INSERT INTO `orders` VALUES (4, 4, 7, 3, '2023-06-04');
INSERT INTO `orders` VALUES (5, 5, 2, 4, '2023-06-05');
INSERT INTO `orders` VALUES (6, 6, 4, 1, '2023-06-06');
INSERT INTO `orders` VALUES (7, 7, 6, 2, '2023-06-07');
INSERT INTO `orders` VALUES (8, 8, 8, 1, '2023-06-08');

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
INSERT INTO `products` VALUES (1, 'Apple', 1, 50, 0.50);
INSERT INTO `products` VALUES (2, 'Orange', 1, 100, 0.30);
INSERT INTO `products` VALUES (3, 'Shirt', 2, 20, 9.99);
INSERT INTO `products` VALUES (4, 'Jeans', 2, 10, 19.99);
INSERT INTO `products` VALUES (5, 'TV', 3, 5, 399.99);
INSERT INTO `products` VALUES (6, 'Phone', 3, 8, 699.99);
INSERT INTO `products` VALUES (7, 'Pillow', 4, 30, 14.99);
INSERT INTO `products` VALUES (8, 'Blanket', 4, 15, 24.99);

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
INSERT INTO `shops` VALUES (1, 'Supermart', '123 Market St', '1234567890');
INSERT INTO `shops` VALUES (2, 'Fashion World', '456 Fashion Ave', '0987654321');
INSERT INTO `shops` VALUES (3, 'Electronics Galore', '789 Tech St', '9876543210');
INSERT INTO `shops` VALUES (4, 'Home Essentials', '321 Home St', '0123456789');
INSERT INTO `shops` VALUES (5, 'Toy Kingdom', '654 Toy St', '5678901234');
INSERT INTO `shops` VALUES (6, 'Sports Zone', '987 Sports Dr', '4321098765');
INSERT INTO `shops` VALUES (7, 'Beauty Emporium', '234 Beauty Blvd', '6789012345');
INSERT INTO `shops` VALUES (8, 'Book Haven', '567 Book Rd', '3456789012');

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
INSERT INTO `users` VALUES (1, 'John', '123456', 'Male', '1234567890', '123 Main St');
INSERT INTO `users` VALUES (2, 'Emily', 'abcdef', 'Female', '0987654321', '456 Elm St');
INSERT INTO `users` VALUES (3, 'Michael', 'qwerty', 'Male', '9876543210', '789 Oak St');
INSERT INTO `users` VALUES (4, 'Jessica', 'password', 'Female', '0123456789', '321 Pine St');
INSERT INTO `users` VALUES (5, 'David', 'pass123', 'Male', '5678901234', '654 Maple St');
INSERT INTO `users` VALUES (6, 'Sarah', '987654321', 'Female', '4321098765', '987 Cedar St');
INSERT INTO `users` VALUES (7, 'Daniel', 'abc123', 'Male', '6789012345', '234 Birch St');
INSERT INTO `users` VALUES (8, 'Sophia', 'password123', 'Female', '3456789012', '567 Willow St');

-- ----------------------------
-- View structure for v_commodity
-- ----------------------------
DROP VIEW IF EXISTS `v_commodity`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_commodity` AS select `products`.`product_id` AS `product_id`,`products`.`product_name` AS `product_name`,`products`.`shop_id` AS `shop_id`,`products`.`stock` AS `stock`,`products`.`price` AS `price` from `products`;

SET FOREIGN_KEY_CHECKS = 1;
