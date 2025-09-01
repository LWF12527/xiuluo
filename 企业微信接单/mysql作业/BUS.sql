-- 创建数据库
CREATE DATABASE IF NOT EXISTS BUS;

-- 使用创建的数据库
USE BUS;

-- 创建供应商表
CREATE TABLE Supplier (
  SupplierID INT PRIMARY KEY,
  CompanyName VARCHAR(255),
  Phone VARCHAR(20),
  Fax VARCHAR(20),
  Address VARCHAR(255),
  Country VARCHAR(255),
  City VARCHAR(255),
  ContactName VARCHAR(255),
  ContactTitle VARCHAR(255),
  Homepage VARCHAR(255)
);

-- 创建产品表
CREATE TABLE Product (
  ProductID INT PRIMARY KEY,
  ProductName VARCHAR(255),
  ProductCategory VARCHAR(255),
  Brand VARCHAR(255),
  Origin VARCHAR(255),
  Weight DECIMAL(10, 2),
  Quality VARCHAR(255),
  Size VARCHAR(255),
  Model VARCHAR(255)
);

-- 创建客户表
CREATE TABLE Customer (
  CustomerID INT PRIMARY KEY,
  CompanyName VARCHAR(255),
  Phone VARCHAR(20),
  Fax VARCHAR(20),
  Address VARCHAR(255),
  Country VARCHAR(255),
  City VARCHAR(255),
  ContactName VARCHAR(255),
  ContactTitle VARCHAR(255),
  Homepage VARCHAR(255)
);

-- 创建进货订单表
CREATE TABLE PurchaseOrder (
  OrderID INT PRIMARY KEY,
  OrderModel VARCHAR(255),
  Status VARCHAR(255),
  CreationDate DATE,
  TransactionDate DATE
);

-- 创建进货订单明细表
CREATE TABLE PurchaseOrderDetail (
  OrderID INT,
  ProductID INT,
  Quantity INT,
  UnitPrice DECIMAL(10, 2),
  Discount DECIMAL(4, 2),
  AmountPayable DECIMAL(10, 2),
  AmountPaid DECIMAL(10, 2),
  FOREIGN KEY (OrderID) REFERENCES PurchaseOrder(OrderID),
  FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- 创建销售订单表
CREATE TABLE SalesOrder (
  OrderID INT PRIMARY KEY,
  OrderModel VARCHAR(255),
  Status VARCHAR(255),
  CreationDate DATE,
  TransactionDate DATE
);

-- 创建销售订单明细表
CREATE TABLE SalesOrderDetail (
  OrderID INT,
  ProductID INT,
  Quantity INT,
  UnitPrice DECIMAL(10, 2),
  Discount DECIMAL(4, 2),
  AmountPayable DECIMAL(10, 2),
  AmountPaid DECIMAL(10, 2),
  FOREIGN KEY (OrderID) REFERENCES SalesOrder(OrderID),
  FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- 创建库存表
CREATE TABLE Inventory (
  ProductID INT,
  WarehouseID INT PRIMARY KEY,
  WarehouseName VARCHAR(255),
  QuantityRemaining INT,
  Threshold INT,
  TotalCapacity INT,
  Manager VARCHAR(255),
  Phone VARCHAR(20),
  FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- 创建统计分析表
CREATE TABLE Statistics (
  StatisticsID INT PRIMARY KEY,
  ProductID INT,
  MonthlyGrossProfit DECIMAL(10, 2),
  MonthlyCost DECIMAL(10, 2),
  MonthlyNetProfit DECIMAL(10, 2),
  AnnualGrossProfit DECIMAL(10, 2),
  AnnualCost DECIMAL(10, 2),
  AnnualNetProfit DECIMAL(10, 2),
  FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);


-- 插入供应商数据
INSERT INTO Supplier (SupplierID, CompanyName, Phone, Fax, Address, Country, City, ContactName, ContactTitle, Homepage)
VALUES
  (1, 'Supplier 1', '1234567890', '9876543210', 'Address 1', 'Country 1', 'City 1', 'Contact 1', 'Title 1', 'www.supplier1.com'),
  (2, 'Supplier 2', '1234567890', '9876543210', 'Address 2', 'Country 2', 'City 2', 'Contact 2', 'Title 2', 'www.supplier2.com'),
  (3, 'Supplier 3', '1234567890', '9876543210', 'Address 3', 'Country 3', 'City 3', 'Contact 3', 'Title 3', 'www.supplier3.com'),
  (4, 'Supplier 4', '1234567890', '9876543210', 'Address 4', 'Country 4', 'City 4', 'Contact 4', 'Title 4', 'www.supplier4.com'),
  (5, 'Supplier 5', '1234567890', '9876543210', 'Address 5', 'Country 5', 'City 5', 'Contact 5', 'Title 5', 'www.supplier5.com');

-- 插入产品数据
INSERT INTO Product (ProductID, ProductName, ProductCategory, Brand, Origin, Weight, Quality, Size, Model)
VALUES
  (1, 'Product 1', 'Category 1', 'Brand 1', 'Origin 1', 1.5, 'High', 'Size 1', 'Model 1'),
  (2, 'Product 2', 'Category 2', 'Brand 2', 'Origin 2', 2.0, 'Medium', 'Size 2', 'Model 2'),
  (3, 'Product 3', 'Category 3', 'Brand 3', 'Origin 3', 1.8, 'Low', 'Size 3', 'Model 3'),
  (4, 'Product 4', 'Category 1', 'Brand 1', 'Origin 4', 2.2, 'High', 'Size 4', 'Model 4'),
  (5, 'Product 5', 'Category 2', 'Brand 2', 'Origin 5', 1.9, 'Medium', 'Size 5', 'Model 5');

-- 插入客户数据
INSERT INTO Customer (CustomerID, CompanyName, Phone, Fax, Address, Country, City, ContactName, ContactTitle, Homepage)
VALUES
  (1, 'Customer 1', '1234567890', '9876543210', 'Address 1', 'Country 1', 'City 1', 'Contact 1', 'Title 1', 'www.customer1.com'),
  (2, 'Customer 2', '1234567890', '9876543210', 'Address 2', 'Country 2', 'City 2', 'Contact 2', 'Title 2', 'www.customer2.com'),
  (3, 'Customer 3', '1234567890', '9876543210', 'Address 3', 'Country 3', 'City 3', 'Contact 3', 'Title 3', 'www.customer3.com'),
  (4, 'Customer 4', '1234567890', '9876543210', 'Address 4', 'Country 4', 'City 4', 'Contact 4', 'Title 4', 'www.customer4.com'),
  (5, 'Customer 5', '1234567890', '9876543210', 'Address 5', 'Country 5', 'City 5', 'Contact 5', 'Title 5', 'www.customer5.com');

-- 插入进货订单数据
INSERT INTO PurchaseOrder (OrderID, OrderModel, Status, CreationDate, TransactionDate)
VALUES
  (1, 'Order 1', 'Pending', '2022-01-01', '2022-01-05'),
  (2, 'Order 2', 'Completed', '2022-02-01', '2022-02-05'),
  (3, 'Order 3', 'Pending', '2022-03-01', '2022-03-05'),
  (4, 'Order 4', 'Completed', '2022-04-01', '2022-04-05'),
  (5, 'Order 5', 'Pending', '2022-05-01', '2022-05-05');

-- 插入进货订单明细数据
INSERT INTO PurchaseOrderDetail (OrderID, ProductID, Quantity, UnitPrice, Discount, AmountPayable, AmountPaid)
VALUES
  (1, 1, 10, 10.99, 0.5, 100.00, 50.00),
  (2, 2, 5, 20.99, 0.25, 100.00, 75.00),
  (3, 3, 8, 15.99, 0.1, 100.00, 90.00),
  (4, 4, 12, 8.99, 0.0, 100.00, 100.00),
  (5, 5, 15, 12.99, 0.15, 100.00, 85.00);

-- 插入销售订单数据
INSERT INTO SalesOrder (OrderID, OrderModel, Status, CreationDate, TransactionDate)
VALUES
  (1, 'Order 1', 'Pending', '2022-01-01', '2022-01-05'),
  (2, 'Order 2', 'Completed', '2022-02-01', '2022-02-05'),
  (3, 'Order 3', 'Pending', '2022-03-01', '2022-03-05'),
  (4, 'Order 4', 'Completed', '2022-04-01', '2022-04-05'),
  (5, 'Order 5', 'Pending', '2022-05-01', '2022-05-05');

-- 插入销售订单明细数据
INSERT INTO SalesOrderDetail (OrderID, ProductID, Quantity, UnitPrice, Discount, AmountPayable, AmountPaid)
VALUES
  (1, 1, 10, 10.99, 0.5, 100.00, 50.00),
  (2, 2, 5, 20.99, 0.25, 100.00, 75.00),
  (3, 3, 8, 15.99, 0.1, 100.00, 90.00),
  (4, 4, 12, 8.99, 0.0, 100.00, 100.00),
  (5, 5, 15, 12.99, 0.15, 100.00, 85.00);

-- 插入库存数据
INSERT INTO Inventory (ProductID, WarehouseID, WarehouseName, QuantityRemaining, Threshold, TotalCapacity, Manager, Phone)
VALUES
  (1, 1, 'Warehouse 1', 100, 10, 200, 'Manager 1', '1234567890'),
  (2, 2, 'Warehouse 2', 200, 20, 300, 'Manager 2', '1234567890'),
  (3, 3, 'Warehouse 3', 150, 15, 250, 'Manager 3', '1234567890'),
  (4, 4, 'Warehouse 4', 120, 12, 220, 'Manager 4', '1234567890'),
  (5, 5, 'Warehouse 5', 180, 18, 280, 'Manager 5', '1234567890');

-- 插入统计分析数据
INSERT INTO Statistics (StatisticsID, ProductID, MonthlyGrossProfit, MonthlyCost, MonthlyNetProfit, AnnualGrossProfit, AnnualCost, AnnualNetProfit)
VALUES
  (1, 1, 1000.00, 800.00, 200.00, 12000.00, 9600.00, 2400.00),
  (2, 2, 1500.00, 1200.00, 300.00, 18000.00, 14400.00, 3600.00),
  (3, 3, 1200.00, 1000.00, 200.00, 14400.00, 12000.00, 2400.00),
  (4, 4, 800.00, 600.00, 200.00, 9600.00, 7200.00, 2400.00),
  (5, 5, 1100.00, 900.00, 200.00, 13200.00, 10800.00, 2400.00);

