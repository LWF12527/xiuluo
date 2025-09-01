/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : store_management

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 01/01/2025 22:29:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `ProductID` int NOT NULL AUTO_INCREMENT,
  `ProductName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `CategoryID` int NOT NULL,
  `Unit` enum('只','件','箱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `TotalStock` int NULL DEFAULT 0,
  PRIMARY KEY (`ProductID`) USING BTREE,
  INDEX `CategoryID`(`CategoryID` ASC) USING BTREE,
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`CategoryID`) REFERENCES `productcategory` (`CategoryID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_chk_1` CHECK (`TotalStock` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, '手机', 1, '件', 50);
INSERT INTO `product` VALUES (2, '电视', 2, '件', 30);
INSERT INTO `product` VALUES (3, '衣服', 3, '件', 100);
INSERT INTO `product` VALUES (4, '零食', 4, '箱', 200);
INSERT INTO `product` VALUES (5, '玩具车', 5, '只', 150);
INSERT INTO `product` VALUES (6, '钢笔', 6, '只', 500);
INSERT INTO `product` VALUES (7, '口红', 7, '件', 80);
INSERT INTO `product` VALUES (8, '沙发', 8, '件', 20);
INSERT INTO `product` VALUES (9, '篮球', 9, '只', 60);
INSERT INTO `product` VALUES (10, '刹车片', 10, '件', 40);
INSERT INTO `product` VALUES (31, '小说', 11, '件', 300);
INSERT INTO `product` VALUES (32, '维生素', 12, '件', 120);
INSERT INTO `product` VALUES (33, '水泥', 13, '件', 50);
INSERT INTO `product` VALUES (34, '螺丝刀', 14, '件', 100);
INSERT INTO `product` VALUES (35, '耳环', 15, '件', 70);
INSERT INTO `product` VALUES (36, '小麦', 16, '箱', 1000);
INSERT INTO `product` VALUES (37, '键盘', 17, '件', 120);
INSERT INTO `product` VALUES (38, '洗衣液', 18, '箱', 80);
INSERT INTO `product` VALUES (39, '充电器', 19, '件', 200);
INSERT INTO `product` VALUES (40, '清洁剂', 20, '箱', 60);

-- ----------------------------
-- Table structure for productcategory
-- ----------------------------
DROP TABLE IF EXISTS `productcategory`;
CREATE TABLE `productcategory`  (
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`CategoryID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of productcategory
-- ----------------------------
INSERT INTO `productcategory` VALUES (1, '电子产品');
INSERT INTO `productcategory` VALUES (2, '家用电器');
INSERT INTO `productcategory` VALUES (3, '服装');
INSERT INTO `productcategory` VALUES (4, '食品');
INSERT INTO `productcategory` VALUES (5, '玩具');
INSERT INTO `productcategory` VALUES (6, '文具');
INSERT INTO `productcategory` VALUES (7, '化妆品');
INSERT INTO `productcategory` VALUES (8, '家具');
INSERT INTO `productcategory` VALUES (9, '运动用品');
INSERT INTO `productcategory` VALUES (10, '汽车配件');
INSERT INTO `productcategory` VALUES (11, '书籍');
INSERT INTO `productcategory` VALUES (12, '医药用品');
INSERT INTO `productcategory` VALUES (13, '建筑材料');
INSERT INTO `productcategory` VALUES (14, '五金工具');
INSERT INTO `productcategory` VALUES (15, '饰品');
INSERT INTO `productcategory` VALUES (16, '农产品');
INSERT INTO `productcategory` VALUES (17, '电脑配件');
INSERT INTO `productcategory` VALUES (18, '日用品');
INSERT INTO `productcategory` VALUES (19, '手机配件');
INSERT INTO `productcategory` VALUES (20, '清洁用品');

-- ----------------------------
-- Table structure for productinbound
-- ----------------------------
DROP TABLE IF EXISTS `productinbound`;
CREATE TABLE `productinbound`  (
  `InboundID` int NOT NULL AUTO_INCREMENT,
  `ProductID` int NOT NULL,
  `SupplierID` int NOT NULL,
  `Quantity` int NOT NULL,
  `WarehouseID` int NOT NULL,
  `InboundDate` date NOT NULL,
  PRIMARY KEY (`InboundID`) USING BTREE,
  INDEX `ProductID`(`ProductID` ASC) USING BTREE,
  INDEX `SupplierID`(`SupplierID` ASC) USING BTREE,
  INDEX `WarehouseID`(`WarehouseID` ASC) USING BTREE,
  CONSTRAINT `productinbound_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `productinbound_ibfk_2` FOREIGN KEY (`SupplierID`) REFERENCES `supplier` (`SupplierID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `productinbound_ibfk_3` FOREIGN KEY (`WarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of productinbound
-- ----------------------------
INSERT INTO `productinbound` VALUES (1, 1, 1, 10, 1, '2025-01-01');
INSERT INTO `productinbound` VALUES (2, 2, 2, 15, 1, '2025-01-02');
INSERT INTO `productinbound` VALUES (3, 3, 3, 20, 1, '2025-01-03');
INSERT INTO `productinbound` VALUES (4, 4, 4, 30, 2, '2025-01-04');
INSERT INTO `productinbound` VALUES (5, 5, 5, 25, 2, '2025-01-05');
INSERT INTO `productinbound` VALUES (6, 6, 6, 40, 3, '2025-01-06');
INSERT INTO `productinbound` VALUES (7, 7, 7, 15, 3, '2025-01-07');
INSERT INTO `productinbound` VALUES (8, 8, 8, 10, 4, '2025-01-08');
INSERT INTO `productinbound` VALUES (9, 9, 9, 20, 4, '2025-01-09');
INSERT INTO `productinbound` VALUES (10, 10, 10, 5, 5, '2025-01-10');
INSERT INTO `productinbound` VALUES (11, 11, 11, 35, 5, '2025-01-11');
INSERT INTO `productinbound` VALUES (12, 12, 12, 25, 6, '2025-01-12');
INSERT INTO `productinbound` VALUES (13, 13, 13, 50, 6, '2025-01-13');
INSERT INTO `productinbound` VALUES (14, 14, 14, 20, 7, '2025-01-14');
INSERT INTO `productinbound` VALUES (15, 15, 15, 30, 7, '2025-01-15');
INSERT INTO `productinbound` VALUES (16, 16, 16, 200, 8, '2025-01-16');
INSERT INTO `productinbound` VALUES (17, 17, 17, 60, 8, '2025-01-17');
INSERT INTO `productinbound` VALUES (18, 18, 18, 40, 9, '2025-01-18');
INSERT INTO `productinbound` VALUES (19, 19, 19, 50, 9, '2025-01-19');
INSERT INTO `productinbound` VALUES (20, 20, 20, 30, 10, '2025-01-20');

-- ----------------------------
-- Table structure for productoutbound
-- ----------------------------
DROP TABLE IF EXISTS `productoutbound`;
CREATE TABLE `productoutbound`  (
  `OutboundID` int NOT NULL AUTO_INCREMENT,
  `ProductID` int NOT NULL,
  `SalespersonID` int NOT NULL,
  `Quantity` int NOT NULL,
  `WarehouseID` int NOT NULL,
  `OutboundDate` date NOT NULL,
  PRIMARY KEY (`OutboundID`) USING BTREE,
  INDEX `ProductID`(`ProductID` ASC) USING BTREE,
  INDEX `SalespersonID`(`SalespersonID` ASC) USING BTREE,
  INDEX `WarehouseID`(`WarehouseID` ASC) USING BTREE,
  CONSTRAINT `productoutbound_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `productoutbound_ibfk_2` FOREIGN KEY (`SalespersonID`) REFERENCES `salesperson` (`SalespersonID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `productoutbound_ibfk_3` FOREIGN KEY (`WarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of productoutbound
-- ----------------------------
INSERT INTO `productoutbound` VALUES (1, 1, 1, 5, 1, '2025-01-21');
INSERT INTO `productoutbound` VALUES (2, 2, 2, 10, 1, '2025-01-22');
INSERT INTO `productoutbound` VALUES (3, 3, 3, 15, 1, '2025-01-23');
INSERT INTO `productoutbound` VALUES (4, 4, 4, 20, 2, '2025-01-24');
INSERT INTO `productoutbound` VALUES (5, 5, 5, 10, 2, '2025-01-25');
INSERT INTO `productoutbound` VALUES (6, 6, 6, 15, 3, '2025-01-26');
INSERT INTO `productoutbound` VALUES (7, 7, 7, 5, 3, '2025-01-27');
INSERT INTO `productoutbound` VALUES (8, 8, 8, 8, 4, '2025-01-28');
INSERT INTO `productoutbound` VALUES (9, 9, 9, 12, 4, '2025-01-29');
INSERT INTO `productoutbound` VALUES (10, 10, 10, 3, 5, '2025-01-30');
INSERT INTO `productoutbound` VALUES (11, 11, 11, 18, 5, '2025-01-31');
INSERT INTO `productoutbound` VALUES (12, 12, 12, 10, 6, '2025-02-01');
INSERT INTO `productoutbound` VALUES (13, 13, 13, 25, 6, '2025-02-02');
INSERT INTO `productoutbound` VALUES (14, 14, 14, 10, 7, '2025-02-03');
INSERT INTO `productoutbound` VALUES (15, 15, 15, 15, 7, '2025-02-04');
INSERT INTO `productoutbound` VALUES (16, 16, 16, 100, 8, '2025-02-05');
INSERT INTO `productoutbound` VALUES (17, 17, 17, 40, 8, '2025-02-06');
INSERT INTO `productoutbound` VALUES (18, 18, 18, 20, 9, '2025-02-07');
INSERT INTO `productoutbound` VALUES (19, 19, 19, 25, 9, '2025-02-08');
INSERT INTO `productoutbound` VALUES (20, 20, 20, 20, 10, '2025-02-09');

-- ----------------------------
-- Table structure for salesperson
-- ----------------------------
DROP TABLE IF EXISTS `salesperson`;
CREATE TABLE `salesperson`  (
  `SalespersonID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Phone` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`SalespersonID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of salesperson
-- ----------------------------
INSERT INTO `salesperson` VALUES (1, '业务员A', '1111111111');
INSERT INTO `salesperson` VALUES (2, '业务员B', '2222222222');
INSERT INTO `salesperson` VALUES (3, '业务员C', '3333333333');
INSERT INTO `salesperson` VALUES (4, '业务员D', '4444444444');
INSERT INTO `salesperson` VALUES (5, '业务员E', '5555555555');
INSERT INTO `salesperson` VALUES (6, '业务员F', '6666666666');
INSERT INTO `salesperson` VALUES (7, '业务员G', '7777777777');
INSERT INTO `salesperson` VALUES (8, '业务员H', '8888888888');
INSERT INTO `salesperson` VALUES (9, '业务员I', '9999999999');
INSERT INTO `salesperson` VALUES (10, '业务员J', '1010101010');
INSERT INTO `salesperson` VALUES (11, '业务员K', '1212121212');
INSERT INTO `salesperson` VALUES (12, '业务员L', '1313131313');
INSERT INTO `salesperson` VALUES (13, '业务员M', '1414141414');
INSERT INTO `salesperson` VALUES (14, '业务员N', '1515151515');
INSERT INTO `salesperson` VALUES (15, '业务员O', '1616161616');
INSERT INTO `salesperson` VALUES (16, '业务员P', '1717171717');
INSERT INTO `salesperson` VALUES (17, '业务员Q', '1818181818');
INSERT INTO `salesperson` VALUES (18, '业务员R', '1919191919');
INSERT INTO `salesperson` VALUES (19, '业务员S', '2020202020');
INSERT INTO `salesperson` VALUES (20, '业务员T', '2121212121');

-- ----------------------------
-- Table structure for supplier
-- ----------------------------
DROP TABLE IF EXISTS `supplier`;
CREATE TABLE `supplier`  (
  `SupplierID` int NOT NULL AUTO_INCREMENT,
  `SupplierName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Contact` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`SupplierID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of supplier
-- ----------------------------
INSERT INTO `supplier` VALUES (1, '供应商A', '1234567890');
INSERT INTO `supplier` VALUES (2, '供应商B', '0987654321');
INSERT INTO `supplier` VALUES (3, '供应商C', '1231231234');
INSERT INTO `supplier` VALUES (4, '供应商D', '3213213214');
INSERT INTO `supplier` VALUES (5, '供应商E', '1112223334');
INSERT INTO `supplier` VALUES (6, '供应商F', '4445556667');
INSERT INTO `supplier` VALUES (7, '供应商G', '7778889990');
INSERT INTO `supplier` VALUES (8, '供应商H', '6665554443');
INSERT INTO `supplier` VALUES (9, '供应商I', '3332221111');
INSERT INTO `supplier` VALUES (10, '供应商J', '9998887770');
INSERT INTO `supplier` VALUES (11, '供应商K', '1011121314');
INSERT INTO `supplier` VALUES (12, '供应商L', '1516171819');
INSERT INTO `supplier` VALUES (13, '供应商M', '2021222324');
INSERT INTO `supplier` VALUES (14, '供应商N', '2526272829');
INSERT INTO `supplier` VALUES (15, '供应商O', '3031323334');
INSERT INTO `supplier` VALUES (16, '供应商P', '3536373839');
INSERT INTO `supplier` VALUES (17, '供应商Q', '4041424344');
INSERT INTO `supplier` VALUES (18, '供应商R', '4546474849');
INSERT INTO `supplier` VALUES (19, '供应商S', '5051525354');
INSERT INTO `supplier` VALUES (20, '供应商T', '5556575859');

-- ----------------------------
-- Table structure for transferlog
-- ----------------------------
DROP TABLE IF EXISTS `transferlog`;
CREATE TABLE `transferlog`  (
  `TransferID` int NOT NULL AUTO_INCREMENT,
  `ProductID` int NOT NULL,
  `FromWarehouseID` int NOT NULL,
  `ToWarehouseID` int NOT NULL,
  `Quantity` int NOT NULL,
  `TransferDate` date NOT NULL,
  PRIMARY KEY (`TransferID`) USING BTREE,
  INDEX `ProductID`(`ProductID` ASC) USING BTREE,
  INDEX `FromWarehouseID`(`FromWarehouseID` ASC) USING BTREE,
  INDEX `ToWarehouseID`(`ToWarehouseID` ASC) USING BTREE,
  CONSTRAINT `transferlog_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `transferlog_ibfk_2` FOREIGN KEY (`FromWarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `transferlog_ibfk_3` FOREIGN KEY (`ToWarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `transferlog_chk_1` CHECK (`Quantity` > 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of transferlog
-- ----------------------------
INSERT INTO `transferlog` VALUES (1, 1, 1, 2, 5, '2025-02-01');
INSERT INTO `transferlog` VALUES (2, 2, 2, 3, 10, '2025-02-02');
INSERT INTO `transferlog` VALUES (3, 3, 3, 4, 15, '2025-02-03');
INSERT INTO `transferlog` VALUES (4, 4, 4, 5, 20, '2025-02-04');
INSERT INTO `transferlog` VALUES (5, 5, 5, 6, 25, '2025-02-05');
INSERT INTO `transferlog` VALUES (6, 6, 6, 7, 30, '2025-02-06');
INSERT INTO `transferlog` VALUES (7, 7, 7, 8, 10, '2025-02-07');
INSERT INTO `transferlog` VALUES (8, 8, 8, 9, 12, '2025-02-08');
INSERT INTO `transferlog` VALUES (9, 9, 9, 10, 15, '2025-02-09');
INSERT INTO `transferlog` VALUES (10, 10, 10, 1, 20, '2025-02-10');
INSERT INTO `transferlog` VALUES (11, 11, 1, 2, 8, '2025-02-11');
INSERT INTO `transferlog` VALUES (12, 12, 2, 3, 12, '2025-02-12');
INSERT INTO `transferlog` VALUES (13, 13, 3, 4, 18, '2025-02-13');
INSERT INTO `transferlog` VALUES (14, 14, 4, 5, 22, '2025-02-14');
INSERT INTO `transferlog` VALUES (15, 15, 5, 6, 25, '2025-02-15');
INSERT INTO `transferlog` VALUES (16, 16, 6, 7, 30, '2025-02-16');
INSERT INTO `transferlog` VALUES (17, 17, 7, 8, 35, '2025-02-17');
INSERT INTO `transferlog` VALUES (18, 18, 8, 9, 40, '2025-02-18');
INSERT INTO `transferlog` VALUES (19, 19, 9, 10, 45, '2025-02-19');
INSERT INTO `transferlog` VALUES (20, 20, 10, 1, 50, '2025-02-20');

-- ----------------------------
-- Table structure for warehouse
-- ----------------------------
DROP TABLE IF EXISTS `warehouse`;
CREATE TABLE `warehouse`  (
  `WarehouseID` int NOT NULL AUTO_INCREMENT,
  `WarehouseName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Location` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`WarehouseID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of warehouse
-- ----------------------------
INSERT INTO `warehouse` VALUES (1, '仓库A', '北京');
INSERT INTO `warehouse` VALUES (2, '仓库B', '上海');
INSERT INTO `warehouse` VALUES (3, '仓库C', '广州');
INSERT INTO `warehouse` VALUES (4, '仓库D', '深圳');
INSERT INTO `warehouse` VALUES (5, '仓库E', '杭州');
INSERT INTO `warehouse` VALUES (6, '仓库F', '南京');
INSERT INTO `warehouse` VALUES (7, '仓库G', '成都');
INSERT INTO `warehouse` VALUES (8, '仓库H', '武汉');
INSERT INTO `warehouse` VALUES (9, '仓库I', '重庆');
INSERT INTO `warehouse` VALUES (10, '仓库J', '西安');
INSERT INTO `warehouse` VALUES (11, '仓库K', '天津');
INSERT INTO `warehouse` VALUES (12, '仓库L', '郑州');
INSERT INTO `warehouse` VALUES (13, '仓库M', '长沙');
INSERT INTO `warehouse` VALUES (14, '仓库N', '苏州');
INSERT INTO `warehouse` VALUES (15, '仓库O', '青岛');
INSERT INTO `warehouse` VALUES (16, '仓库P', '济南');
INSERT INTO `warehouse` VALUES (17, '仓库Q', '福州');
INSERT INTO `warehouse` VALUES (18, '仓库R', '厦门');
INSERT INTO `warehouse` VALUES (19, '仓库S', '南昌');
INSERT INTO `warehouse` VALUES (20, '仓库T', '合肥');

-- ----------------------------
-- Table structure for warehouseproduct
-- ----------------------------
DROP TABLE IF EXISTS `warehouseproduct`;
CREATE TABLE `warehouseproduct`  (
  `WarehouseID` int NOT NULL,
  `ProductID` int NOT NULL,
  `Quantity` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`WarehouseID`, `ProductID`) USING BTREE,
  INDEX `ProductID`(`ProductID` ASC) USING BTREE,
  CONSTRAINT `warehouseproduct_ibfk_1` FOREIGN KEY (`WarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `warehouseproduct_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of warehouseproduct
-- ----------------------------
INSERT INTO `warehouseproduct` VALUES (1, 1, 10);
INSERT INTO `warehouseproduct` VALUES (1, 2, 20);
INSERT INTO `warehouseproduct` VALUES (1, 3, 25);
INSERT INTO `warehouseproduct` VALUES (1, 10, 20);
INSERT INTO `warehouseproduct` VALUES (1, 20, 50);
INSERT INTO `warehouseproduct` VALUES (2, 1, 5);
INSERT INTO `warehouseproduct` VALUES (2, 4, 40);
INSERT INTO `warehouseproduct` VALUES (2, 5, 40);
INSERT INTO `warehouseproduct` VALUES (2, 11, 8);
INSERT INTO `warehouseproduct` VALUES (3, 2, 10);
INSERT INTO `warehouseproduct` VALUES (3, 6, 65);
INSERT INTO `warehouseproduct` VALUES (3, 7, 25);
INSERT INTO `warehouseproduct` VALUES (3, 12, 12);
INSERT INTO `warehouseproduct` VALUES (4, 3, 15);
INSERT INTO `warehouseproduct` VALUES (4, 8, 12);
INSERT INTO `warehouseproduct` VALUES (4, 9, 28);
INSERT INTO `warehouseproduct` VALUES (4, 13, 18);
INSERT INTO `warehouseproduct` VALUES (5, 4, 20);
INSERT INTO `warehouseproduct` VALUES (5, 10, 7);
INSERT INTO `warehouseproduct` VALUES (5, 11, 52);
INSERT INTO `warehouseproduct` VALUES (5, 14, 22);
INSERT INTO `warehouseproduct` VALUES (6, 5, 25);
INSERT INTO `warehouseproduct` VALUES (6, 12, 40);
INSERT INTO `warehouseproduct` VALUES (6, 13, 75);
INSERT INTO `warehouseproduct` VALUES (6, 15, 25);
INSERT INTO `warehouseproduct` VALUES (7, 6, 30);
INSERT INTO `warehouseproduct` VALUES (7, 14, 30);
INSERT INTO `warehouseproduct` VALUES (7, 15, 45);
INSERT INTO `warehouseproduct` VALUES (7, 16, 30);
INSERT INTO `warehouseproduct` VALUES (8, 7, 10);
INSERT INTO `warehouseproduct` VALUES (8, 16, 300);
INSERT INTO `warehouseproduct` VALUES (8, 17, 115);
INSERT INTO `warehouseproduct` VALUES (9, 8, 12);
INSERT INTO `warehouseproduct` VALUES (9, 18, 100);
INSERT INTO `warehouseproduct` VALUES (9, 19, 30);
INSERT INTO `warehouseproduct` VALUES (10, 9, 15);
INSERT INTO `warehouseproduct` VALUES (10, 19, 45);
INSERT INTO `warehouseproduct` VALUES (10, 20, -10);

-- ----------------------------
-- Procedure structure for GetProductStatistics
-- ----------------------------
DROP PROCEDURE IF EXISTS `GetProductStatistics`;
delimiter ;;
CREATE PROCEDURE `GetProductStatistics`(IN ProductID INT)
BEGIN
    SELECT 
        p.ProductName AS 商品名称,
        IFNULL(SUM(pi.Quantity), 0) AS 总进货量,
        IFNULL(SUM(po.Quantity), 0) AS 总销售量
    FROM Product p
    LEFT JOIN ProductInbound pi ON p.ProductID = pi.ProductID
    LEFT JOIN ProductOutbound po ON p.ProductID = po.ProductID
    WHERE p.ProductID = ProductID
    GROUP BY p.ProductName;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for sp_Statistics
-- ----------------------------
DROP PROCEDURE IF EXISTS `sp_Statistics`;
delimiter ;;
CREATE PROCEDURE `sp_Statistics`(IN StartDate DATE, IN EndDate DATE)
BEGIN
    SELECT 
        p.ProductID AS 商品ID,
        p.ProductName AS 商品名称,
        IFNULL(SUM(CASE WHEN pi.InboundDate BETWEEN StartDate AND EndDate THEN pi.Quantity ELSE 0 END), 0) AS 进货数量,
        IFNULL(SUM(CASE WHEN po.OutboundDate BETWEEN StartDate AND EndDate THEN po.Quantity ELSE 0 END), 0) AS 销售数量
    FROM Product p
    LEFT JOIN ProductInbound pi ON p.ProductID = pi.ProductID
    LEFT JOIN ProductOutbound po ON p.ProductID = po.ProductID
    GROUP BY p.ProductID, p.ProductName
    ORDER BY p.ProductID;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table productinbound
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_ProductInbound`;
delimiter ;;
CREATE TRIGGER `trg_ProductInbound` AFTER INSERT ON `productinbound` FOR EACH ROW BEGIN
    -- 更新 Product 表的总库存
    UPDATE Product
    SET TotalStock = TotalStock + NEW.Quantity
    WHERE ProductID = NEW.ProductID;

    -- 更新 WarehouseProduct 表的库存数量
    UPDATE WarehouseProduct
    SET Quantity = Quantity + NEW.Quantity
    WHERE WarehouseID = NEW.WarehouseID AND ProductID = NEW.ProductID;

    -- 如果 WarehouseProduct 中不存在对应记录，则插入新记录
    INSERT INTO WarehouseProduct (WarehouseID, ProductID, Quantity)
    SELECT NEW.WarehouseID, NEW.ProductID, NEW.Quantity
    WHERE NOT EXISTS (
        SELECT 1 
        FROM WarehouseProduct 
        WHERE WarehouseID = NEW.WarehouseID AND ProductID = NEW.ProductID
    );
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table productoutbound
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_ProductOutbound`;
delimiter ;;
CREATE TRIGGER `trg_ProductOutbound` AFTER INSERT ON `productoutbound` FOR EACH ROW BEGIN
    -- 更新 Product 表的总库存
    UPDATE Product
    SET TotalStock = TotalStock - NEW.Quantity
    WHERE ProductID = NEW.ProductID;

    -- 更新 WarehouseProduct 表的库存数量
    UPDATE WarehouseProduct
    SET Quantity = Quantity - NEW.Quantity
    WHERE WarehouseID = NEW.WarehouseID AND ProductID = NEW.ProductID;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table transferlog
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_TransferWarehouse`;
delimiter ;;
CREATE TRIGGER `trg_TransferWarehouse` AFTER INSERT ON `transferlog` FOR EACH ROW BEGIN
    -- 更新转出仓库：减少商品数量
    UPDATE WarehouseProduct
    SET Quantity = Quantity - NEW.Quantity
    WHERE WarehouseID = NEW.FromWarehouseID AND ProductID = NEW.ProductID;

    -- 更新转入仓库：增加商品数量
    UPDATE WarehouseProduct
    SET Quantity = Quantity + NEW.Quantity
    WHERE WarehouseID = NEW.ToWarehouseID AND ProductID = NEW.ProductID;

    -- 如果转入仓库中不存在对应记录，则插入新记录
    INSERT INTO WarehouseProduct (WarehouseID, ProductID, Quantity)
    SELECT NEW.ToWarehouseID, NEW.ProductID, NEW.Quantity
    WHERE NOT EXISTS (
        SELECT 1 
        FROM WarehouseProduct 
        WHERE WarehouseID = NEW.ToWarehouseID AND ProductID = NEW.ProductID
    );
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
