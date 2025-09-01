-- 数据库创建
CREATE DATABASE jxc;

use jxc;

-- 2. 创建基本信息表
-- 商品类别表
CREATE TABLE ProductCategory (
    CategoryID INT PRIMARY KEY IDENTITY(1,1),
    CategoryName NVARCHAR(100) NOT NULL
);

-- 供货商表
CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY IDENTITY(1,1),
    SupplierName NVARCHAR(100) NOT NULL,
    Contact NVARCHAR(50)
);

-- 业务员信息表
CREATE TABLE Salesperson (
    SalespersonID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL,
    Phone NVARCHAR(15)
);

-- 3. 商品信息与仓库管理
-- 商品信息表
CREATE TABLE Product (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(100) NOT NULL,
    CategoryID INT FOREIGN KEY REFERENCES ProductCategory(CategoryID),
    Unit NVARCHAR(10) NOT NULL,
    TotalStock INT DEFAULT 0,
    CHECK (TotalStock >= 0) -- 库存不能为负
);
-- 添加规则限制商品单位
CREATE RULE ProductUnitRule AS 
@Unit IN ('只', '件', '箱');
GO
sp_bindrule 'ProductUnitRule', 'Product.Unit';

-- 创建仓库表
CREATE TABLE Warehouse (
    WarehouseID INT PRIMARY KEY IDENTITY(1,1),
    WarehouseName NVARCHAR(100) NOT NULL,
    Location NVARCHAR(100)
);

-- 仓库商品表
CREATE TABLE WarehouseProduct (
    WarehouseID INT FOREIGN KEY REFERENCES Warehouse(WarehouseID),
    ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
    Quantity INT NOT NULL DEFAULT 0, -- 初始化数量为0
    PRIMARY KEY (WarehouseID, ProductID)
);


-- 4. 商品入库与出库管理
-- 商品入库表
CREATE TABLE ProductInbound (
    InboundID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
    SupplierID INT FOREIGN KEY REFERENCES Supplier(SupplierID),
    Quantity INT NOT NULL,
    WarehouseID INT FOREIGN KEY REFERENCES Warehouse(WarehouseID),
    InboundDate DATE NOT NULL
);

-- 商品销售出库表
CREATE TABLE ProductOutbound (
    OutboundID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
    SalespersonID INT FOREIGN KEY REFERENCES Salesperson(SalespersonID),
    Quantity INT NOT NULL,
    WarehouseID INT FOREIGN KEY REFERENCES Warehouse(WarehouseID),
    OutboundDate DATE NOT NULL
);

-- 5. 入库和出库触发器

-- 1. 入库触发器：增加库存
-- 当商品入库时，触发器会自动增加 Product 表的总库存和 WarehouseProduct 表的库存数量。
-- 
CREATE TRIGGER trg_ProductInbound
ON ProductInbound
AFTER INSERT
AS
BEGIN
    -- 更新 Product 表的总库存
    UPDATE p
    SET p.TotalStock = p.TotalStock + i.Quantity
    FROM Product p
    INNER JOIN INSERTED i ON p.ProductID = i.ProductID;

    -- 更新 WarehouseProduct 表的库存数量
    UPDATE wp
    SET wp.Quantity = wp.Quantity + i.Quantity
    FROM WarehouseProduct wp
    INNER JOIN INSERTED i 
        ON wp.WarehouseID = i.WarehouseID 
       AND wp.ProductID = i.ProductID;

    -- 如果 WarehouseProduct 中不存在对应记录，则插入新记录
    INSERT INTO WarehouseProduct (WarehouseID, ProductID, Quantity)
    SELECT i.WarehouseID, i.ProductID, i.Quantity
    FROM INSERTED i
    WHERE NOT EXISTS (
        SELECT 1 
        FROM WarehouseProduct wp 
        WHERE wp.WarehouseID = i.WarehouseID AND wp.ProductID = i.ProductID
    );
END;
GO

-- 出库触发器：减少库存
-- 当商品出库时，触发器会自动减少 Product 表的总库存和 WarehouseProduct 表的库存数量。

CREATE TRIGGER trg_ProductOutbound
ON ProductOutbound
AFTER INSERT
AS
BEGIN
    -- 更新 Product 表的总库存
    UPDATE p
    SET p.TotalStock = p.TotalStock - i.Quantity
    FROM Product p
    INNER JOIN INSERTED i ON p.ProductID = i.ProductID;

    -- 更新 WarehouseProduct 表的库存数量
    UPDATE wp
    SET wp.Quantity = wp.Quantity - i.Quantity
    FROM WarehouseProduct wp
    INNER JOIN INSERTED i 
        ON wp.WarehouseID = i.WarehouseID 
       AND wp.ProductID = i.ProductID;
END;
GO
-- 3. 转仓管理触发器
-- 当商品进行转仓时，触发器会自动修改转出仓库和转入仓库的商品数量。
-- 
-- 转仓记录表

CREATE TABLE TransferLog (
    TransferID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
    FromWarehouseID INT FOREIGN KEY REFERENCES Warehouse(WarehouseID),
    ToWarehouseID INT FOREIGN KEY REFERENCES Warehouse(WarehouseID),
    Quantity INT NOT NULL CHECK (Quantity > 0),
    TransferDate DATE NOT NULL
);

-- 转仓触发器

CREATE TRIGGER trg_TransferWarehouse
ON TransferLog
AFTER INSERT
AS
BEGIN
    -- 更新转出仓库：减少商品数量
    UPDATE wp
    SET wp.Quantity = wp.Quantity - i.Quantity
    FROM WarehouseProduct wp
    INNER JOIN INSERTED i 
        ON wp.WarehouseID = i.FromWarehouseID 
       AND wp.ProductID = i.ProductID;

    -- 更新转入仓库：增加商品数量
    UPDATE wp
    SET wp.Quantity = wp.Quantity + i.Quantity
    FROM WarehouseProduct wp
    INNER JOIN INSERTED i 
        ON wp.WarehouseID = i.ToWarehouseID 
       AND wp.ProductID = i.ProductID;

    -- 如果转入仓库中不存在对应记录，则插入新记录
    INSERT INTO WarehouseProduct (WarehouseID, ProductID, Quantity)
    SELECT i.ToWarehouseID, i.ProductID, i.Quantity
    FROM INSERTED i
    WHERE NOT EXISTS (
        SELECT 1 
        FROM WarehouseProduct wp 
        WHERE wp.WarehouseID = i.ToWarehouseID AND wp.ProductID = i.ProductID
    );
END;
GO

-- 统计指定时间段内各种商品的进货数量和销售数量：
CREATE PROCEDURE sp_Statistics
    @StartDate DATE, -- 开始日期
    @EndDate DATE    -- 结束日期
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        p.ProductID AS 商品ID,
        p.ProductName AS 商品名称,
        ISNULL(SUM(CASE WHEN pi.InboundDate BETWEEN @StartDate AND @EndDate THEN pi.Quantity ELSE 0 END), 0) AS 进货数量,
        ISNULL(SUM(CASE WHEN po.OutboundDate BETWEEN @StartDate AND @EndDate THEN po.Quantity ELSE 0 END), 0) AS 销售数量
    FROM Product p
    LEFT JOIN ProductInbound pi ON p.ProductID = pi.ProductID
    LEFT JOIN ProductOutbound po ON p.ProductID = po.ProductID
    GROUP BY p.ProductID, p.ProductName
    ORDER BY p.ProductID;
END;
GO

-- 1. 插入商品类别表数据
INSERT INTO ProductCategory (CategoryName) VALUES 
('电子产品'),
('家具'),
('食品'),
('服装'),
('文具');

-- 2. 插入供货商表数据
INSERT INTO Supplier (SupplierName, Contact) VALUES 
('供货商A', '123456789'),
('供货商B', '234567890'),
('供货商C', '345678901'),
('供货商D', '456789012'),
('供货商E', '567890123');

-- 3. 插入业务员信息表数据
INSERT INTO Salesperson (Name, Phone) VALUES 
('业务员1', '10000000001'),
('业务员2', '10000000002'),
('业务员3', '10000000003'),
('业务员4', '10000000004'),
('业务员5', '10000000005');

-- 4. 插入仓库表数据
INSERT INTO Warehouse (WarehouseName, Location) VALUES 
('仓库A', '北京'),
('仓库B', '上海'),
('仓库C', '广州'),
('仓库D', '深圳'),
('仓库E', '成都');

-- 5. 插入商品信息表数据
INSERT INTO Product (ProductName, CategoryID, Unit, TotalStock) VALUES 
('智能手机', 1, '只', 100),
('沙发', 2, '件', 50),
('方便面', 3, '箱', 200),
('T恤', 4, '件', 300),
('钢笔', 5, '只', 500);

-- 6. 插入仓库商品表数据
-- 假设商品ID从1到5，仓库ID从1到5
INSERT INTO WarehouseProduct (WarehouseID, ProductID, Quantity) VALUES 
(1, 1, 20),
(1, 2, 30),
(1, 3, 40),
(2, 4, 50),
(2, 5, 60);

-- 7. 插入商品入库表数据
INSERT INTO ProductInbound (ProductID, SupplierID, Quantity, WarehouseID, InboundDate) VALUES 
(1, 1, 50, 1, '2024-12-01'),
(2, 2, 20, 1, '2024-12-05'),
(3, 3, 100, 2, '2024-12-10'),
(4, 4, 150, 2, '2024-12-12'),
(5, 5, 200, 3, '2024-12-15');

-- 8. 插入商品销售出库表数据
INSERT INTO ProductOutbound (ProductID, SalespersonID, Quantity, WarehouseID, OutboundDate) VALUES 
(1, 1, 30, 1, '2024-12-02'),
(2, 2, 10, 1, '2024-12-06'),
(3, 3, 20, 2, '2024-12-11'),
(4, 4, 50, 2, '2024-12-13'),
(5, 5, 100, 3, '2024-12-16');

-- 9. 插入转仓记录表数据
INSERT INTO TransferLog (ProductID, FromWarehouseID, ToWarehouseID, Quantity, TransferDate) VALUES 
(1, 1, 2, 10, '2024-12-07'),
(2, 1, 3, 5, '2024-12-08'),
(3, 2, 4, 20, '2024-12-09'),
(4, 2, 5, 30, '2024-12-14'),
(5, 3, 4, 50, '2024-12-17');
