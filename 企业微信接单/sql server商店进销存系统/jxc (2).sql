/*
 Navicat Premium Data Transfer

 Source Server         : sql server
 Source Server Type    : SQL Server
 Source Server Version : 16004105
 Source Host           : localhost:1433
 Source Catalog        : jxc
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 16004105
 File Encoding         : 65001

 Date: 18/12/2024 11:13:41
*/


-- ----------------------------
-- Table structure for Product
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Product]') AND type IN ('U'))
	DROP TABLE [dbo].[Product]
GO

CREATE TABLE [dbo].[Product] (
  [ProductID] int  IDENTITY(1,1) NOT NULL,
  [ProductName] nvarchar(100) COLLATE Chinese_PRC_CS_AI_WS  NOT NULL,
  [CategoryID] int  NULL,
  [Unit] nvarchar(10) COLLATE Chinese_PRC_CS_AI_WS  NOT NULL,
  [TotalStock] int DEFAULT 0 NULL
)
GO

ALTER TABLE [dbo].[Product] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Product
-- ----------------------------
SET IDENTITY_INSERT [dbo].[Product] ON
GO

INSERT INTO [dbo].[Product] ([ProductID], [ProductName], [CategoryID], [Unit], [TotalStock]) VALUES (N'1', N'智能手机', N'1', N'只', N'120')
GO

INSERT INTO [dbo].[Product] ([ProductID], [ProductName], [CategoryID], [Unit], [TotalStock]) VALUES (N'2', N'沙发', N'2', N'件', N'60')
GO

INSERT INTO [dbo].[Product] ([ProductID], [ProductName], [CategoryID], [Unit], [TotalStock]) VALUES (N'3', N'方便面', N'3', N'箱', N'280')
GO

INSERT INTO [dbo].[Product] ([ProductID], [ProductName], [CategoryID], [Unit], [TotalStock]) VALUES (N'4', N'T恤', N'4', N'件', N'400')
GO

INSERT INTO [dbo].[Product] ([ProductID], [ProductName], [CategoryID], [Unit], [TotalStock]) VALUES (N'5', N'钢笔', N'5', N'只', N'600')
GO

SET IDENTITY_INSERT [dbo].[Product] OFF
GO


-- ----------------------------
-- Table structure for ProductCategory
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[ProductCategory]') AND type IN ('U'))
	DROP TABLE [dbo].[ProductCategory]
GO

CREATE TABLE [dbo].[ProductCategory] (
  [CategoryID] int  IDENTITY(1,1) NOT NULL,
  [CategoryName] nvarchar(100) COLLATE Chinese_PRC_CS_AI_WS  NOT NULL
)
GO

ALTER TABLE [dbo].[ProductCategory] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of ProductCategory
-- ----------------------------
SET IDENTITY_INSERT [dbo].[ProductCategory] ON
GO

INSERT INTO [dbo].[ProductCategory] ([CategoryID], [CategoryName]) VALUES (N'1', N'电子产品')
GO

INSERT INTO [dbo].[ProductCategory] ([CategoryID], [CategoryName]) VALUES (N'2', N'家具')
GO

INSERT INTO [dbo].[ProductCategory] ([CategoryID], [CategoryName]) VALUES (N'3', N'食品')
GO

INSERT INTO [dbo].[ProductCategory] ([CategoryID], [CategoryName]) VALUES (N'4', N'服装')
GO

INSERT INTO [dbo].[ProductCategory] ([CategoryID], [CategoryName]) VALUES (N'5', N'文具')
GO

SET IDENTITY_INSERT [dbo].[ProductCategory] OFF
GO


-- ----------------------------
-- Table structure for ProductInbound
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[ProductInbound]') AND type IN ('U'))
	DROP TABLE [dbo].[ProductInbound]
GO

CREATE TABLE [dbo].[ProductInbound] (
  [InboundID] int  IDENTITY(1,1) NOT NULL,
  [ProductID] int  NULL,
  [SupplierID] int  NULL,
  [Quantity] int  NOT NULL,
  [WarehouseID] int  NULL,
  [InboundDate] date  NOT NULL
)
GO

ALTER TABLE [dbo].[ProductInbound] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of ProductInbound
-- ----------------------------
SET IDENTITY_INSERT [dbo].[ProductInbound] ON
GO

INSERT INTO [dbo].[ProductInbound] ([InboundID], [ProductID], [SupplierID], [Quantity], [WarehouseID], [InboundDate]) VALUES (N'1', N'1', N'1', N'50', N'1', N'2024-12-01')
GO

INSERT INTO [dbo].[ProductInbound] ([InboundID], [ProductID], [SupplierID], [Quantity], [WarehouseID], [InboundDate]) VALUES (N'2', N'2', N'2', N'20', N'1', N'2024-12-05')
GO

INSERT INTO [dbo].[ProductInbound] ([InboundID], [ProductID], [SupplierID], [Quantity], [WarehouseID], [InboundDate]) VALUES (N'3', N'3', N'3', N'100', N'2', N'2024-12-10')
GO

INSERT INTO [dbo].[ProductInbound] ([InboundID], [ProductID], [SupplierID], [Quantity], [WarehouseID], [InboundDate]) VALUES (N'4', N'4', N'4', N'150', N'2', N'2024-12-12')
GO

INSERT INTO [dbo].[ProductInbound] ([InboundID], [ProductID], [SupplierID], [Quantity], [WarehouseID], [InboundDate]) VALUES (N'5', N'5', N'5', N'200', N'3', N'2024-12-15')
GO

SET IDENTITY_INSERT [dbo].[ProductInbound] OFF
GO


-- ----------------------------
-- Table structure for ProductOutbound
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[ProductOutbound]') AND type IN ('U'))
	DROP TABLE [dbo].[ProductOutbound]
GO

CREATE TABLE [dbo].[ProductOutbound] (
  [OutboundID] int  IDENTITY(1,1) NOT NULL,
  [ProductID] int  NULL,
  [SalespersonID] int  NULL,
  [Quantity] int  NOT NULL,
  [WarehouseID] int  NULL,
  [OutboundDate] date  NOT NULL
)
GO

ALTER TABLE [dbo].[ProductOutbound] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of ProductOutbound
-- ----------------------------
SET IDENTITY_INSERT [dbo].[ProductOutbound] ON
GO

INSERT INTO [dbo].[ProductOutbound] ([OutboundID], [ProductID], [SalespersonID], [Quantity], [WarehouseID], [OutboundDate]) VALUES (N'1', N'1', N'1', N'30', N'1', N'2024-12-02')
GO

INSERT INTO [dbo].[ProductOutbound] ([OutboundID], [ProductID], [SalespersonID], [Quantity], [WarehouseID], [OutboundDate]) VALUES (N'2', N'2', N'2', N'10', N'1', N'2024-12-06')
GO

INSERT INTO [dbo].[ProductOutbound] ([OutboundID], [ProductID], [SalespersonID], [Quantity], [WarehouseID], [OutboundDate]) VALUES (N'3', N'3', N'3', N'20', N'2', N'2024-12-11')
GO

INSERT INTO [dbo].[ProductOutbound] ([OutboundID], [ProductID], [SalespersonID], [Quantity], [WarehouseID], [OutboundDate]) VALUES (N'4', N'4', N'4', N'50', N'2', N'2024-12-13')
GO

INSERT INTO [dbo].[ProductOutbound] ([OutboundID], [ProductID], [SalespersonID], [Quantity], [WarehouseID], [OutboundDate]) VALUES (N'5', N'5', N'5', N'100', N'3', N'2024-12-16')
GO

SET IDENTITY_INSERT [dbo].[ProductOutbound] OFF
GO


-- ----------------------------
-- Table structure for Salesperson
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Salesperson]') AND type IN ('U'))
	DROP TABLE [dbo].[Salesperson]
GO

CREATE TABLE [dbo].[Salesperson] (
  [SalespersonID] int  IDENTITY(1,1) NOT NULL,
  [Name] nvarchar(100) COLLATE Chinese_PRC_CS_AI_WS  NOT NULL,
  [Phone] nvarchar(15) COLLATE Chinese_PRC_CS_AI_WS  NULL
)
GO

ALTER TABLE [dbo].[Salesperson] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Salesperson
-- ----------------------------
SET IDENTITY_INSERT [dbo].[Salesperson] ON
GO

INSERT INTO [dbo].[Salesperson] ([SalespersonID], [Name], [Phone]) VALUES (N'1', N'业务员1', N'10000000001')
GO

INSERT INTO [dbo].[Salesperson] ([SalespersonID], [Name], [Phone]) VALUES (N'2', N'业务员2', N'10000000002')
GO

INSERT INTO [dbo].[Salesperson] ([SalespersonID], [Name], [Phone]) VALUES (N'3', N'业务员3', N'10000000003')
GO

INSERT INTO [dbo].[Salesperson] ([SalespersonID], [Name], [Phone]) VALUES (N'4', N'业务员4', N'10000000004')
GO

INSERT INTO [dbo].[Salesperson] ([SalespersonID], [Name], [Phone]) VALUES (N'5', N'业务员5', N'10000000005')
GO

SET IDENTITY_INSERT [dbo].[Salesperson] OFF
GO


-- ----------------------------
-- Table structure for Supplier
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Supplier]') AND type IN ('U'))
	DROP TABLE [dbo].[Supplier]
GO

CREATE TABLE [dbo].[Supplier] (
  [SupplierID] int  IDENTITY(1,1) NOT NULL,
  [SupplierName] nvarchar(100) COLLATE Chinese_PRC_CS_AI_WS  NOT NULL,
  [Contact] nvarchar(50) COLLATE Chinese_PRC_CS_AI_WS  NULL
)
GO

ALTER TABLE [dbo].[Supplier] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Supplier
-- ----------------------------
SET IDENTITY_INSERT [dbo].[Supplier] ON
GO

INSERT INTO [dbo].[Supplier] ([SupplierID], [SupplierName], [Contact]) VALUES (N'1', N'供货商A', N'123456789')
GO

INSERT INTO [dbo].[Supplier] ([SupplierID], [SupplierName], [Contact]) VALUES (N'2', N'供货商B', N'234567890')
GO

INSERT INTO [dbo].[Supplier] ([SupplierID], [SupplierName], [Contact]) VALUES (N'3', N'供货商C', N'345678901')
GO

INSERT INTO [dbo].[Supplier] ([SupplierID], [SupplierName], [Contact]) VALUES (N'4', N'供货商D', N'456789012')
GO

INSERT INTO [dbo].[Supplier] ([SupplierID], [SupplierName], [Contact]) VALUES (N'5', N'供货商E', N'567890123')
GO

SET IDENTITY_INSERT [dbo].[Supplier] OFF
GO


-- ----------------------------
-- Table structure for TransferLog
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[TransferLog]') AND type IN ('U'))
	DROP TABLE [dbo].[TransferLog]
GO

CREATE TABLE [dbo].[TransferLog] (
  [TransferID] int  IDENTITY(1,1) NOT NULL,
  [ProductID] int  NULL,
  [FromWarehouseID] int  NULL,
  [ToWarehouseID] int  NULL,
  [Quantity] int  NOT NULL,
  [TransferDate] date  NOT NULL
)
GO

ALTER TABLE [dbo].[TransferLog] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of TransferLog
-- ----------------------------
SET IDENTITY_INSERT [dbo].[TransferLog] ON
GO

INSERT INTO [dbo].[TransferLog] ([TransferID], [ProductID], [FromWarehouseID], [ToWarehouseID], [Quantity], [TransferDate]) VALUES (N'1', N'1', N'1', N'2', N'10', N'2024-12-07')
GO

INSERT INTO [dbo].[TransferLog] ([TransferID], [ProductID], [FromWarehouseID], [ToWarehouseID], [Quantity], [TransferDate]) VALUES (N'2', N'2', N'1', N'3', N'5', N'2024-12-08')
GO

INSERT INTO [dbo].[TransferLog] ([TransferID], [ProductID], [FromWarehouseID], [ToWarehouseID], [Quantity], [TransferDate]) VALUES (N'3', N'3', N'2', N'4', N'20', N'2024-12-09')
GO

INSERT INTO [dbo].[TransferLog] ([TransferID], [ProductID], [FromWarehouseID], [ToWarehouseID], [Quantity], [TransferDate]) VALUES (N'4', N'4', N'2', N'5', N'30', N'2024-12-14')
GO

INSERT INTO [dbo].[TransferLog] ([TransferID], [ProductID], [FromWarehouseID], [ToWarehouseID], [Quantity], [TransferDate]) VALUES (N'5', N'5', N'3', N'4', N'50', N'2024-12-17')
GO

SET IDENTITY_INSERT [dbo].[TransferLog] OFF
GO


-- ----------------------------
-- Table structure for Warehouse
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Warehouse]') AND type IN ('U'))
	DROP TABLE [dbo].[Warehouse]
GO

CREATE TABLE [dbo].[Warehouse] (
  [WarehouseID] int  IDENTITY(1,1) NOT NULL,
  [WarehouseName] nvarchar(100) COLLATE Chinese_PRC_CS_AI_WS  NOT NULL,
  [Location] nvarchar(100) COLLATE Chinese_PRC_CS_AI_WS  NULL
)
GO

ALTER TABLE [dbo].[Warehouse] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Warehouse
-- ----------------------------
SET IDENTITY_INSERT [dbo].[Warehouse] ON
GO

INSERT INTO [dbo].[Warehouse] ([WarehouseID], [WarehouseName], [Location]) VALUES (N'1', N'仓库A', N'北京')
GO

INSERT INTO [dbo].[Warehouse] ([WarehouseID], [WarehouseName], [Location]) VALUES (N'2', N'仓库B', N'上海')
GO

INSERT INTO [dbo].[Warehouse] ([WarehouseID], [WarehouseName], [Location]) VALUES (N'3', N'仓库C', N'广州')
GO

INSERT INTO [dbo].[Warehouse] ([WarehouseID], [WarehouseName], [Location]) VALUES (N'4', N'仓库D', N'深圳')
GO

INSERT INTO [dbo].[Warehouse] ([WarehouseID], [WarehouseName], [Location]) VALUES (N'5', N'仓库E', N'成都')
GO

SET IDENTITY_INSERT [dbo].[Warehouse] OFF
GO


-- ----------------------------
-- Table structure for WarehouseProduct
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[WarehouseProduct]') AND type IN ('U'))
	DROP TABLE [dbo].[WarehouseProduct]
GO

CREATE TABLE [dbo].[WarehouseProduct] (
  [WarehouseID] int  NOT NULL,
  [ProductID] int  NOT NULL,
  [Quantity] int DEFAULT 0 NOT NULL
)
GO

ALTER TABLE [dbo].[WarehouseProduct] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of WarehouseProduct
-- ----------------------------
INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'1', N'1', N'30')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'1', N'2', N'35')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'1', N'3', N'40')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'2', N'1', N'10')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'2', N'3', N'60')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'2', N'4', N'120')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'2', N'5', N'60')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'3', N'2', N'5')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'3', N'5', N'50')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'4', N'3', N'20')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'4', N'5', N'50')
GO

INSERT INTO [dbo].[WarehouseProduct] ([WarehouseID], [ProductID], [Quantity]) VALUES (N'5', N'4', N'30')
GO


-- ----------------------------
-- procedure structure for sp_Statistics
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[sp_Statistics]') AND type IN ('P', 'PC', 'RF', 'X'))
	DROP PROCEDURE[dbo].[sp_Statistics]
GO

CREATE PROCEDURE [dbo].[sp_Statistics]
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


-- ----------------------------
-- Auto increment value for Product
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[Product]', RESEED, 5)
GO


-- ----------------------------
-- Checks structure for table Product
-- ----------------------------
ALTER TABLE [dbo].[Product] ADD CONSTRAINT [CK__Product__TotalSt__3F466844] CHECK ([TotalStock]>=(0))
GO


-- ----------------------------
-- Primary Key structure for table Product
-- ----------------------------
ALTER TABLE [dbo].[Product] ADD CONSTRAINT [PK__Product__B40CC6EDFD77CBEC] PRIMARY KEY CLUSTERED ([ProductID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for ProductCategory
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[ProductCategory]', RESEED, 5)
GO


-- ----------------------------
-- Primary Key structure for table ProductCategory
-- ----------------------------
ALTER TABLE [dbo].[ProductCategory] ADD CONSTRAINT [PK__ProductC__19093A2BF3FAE7C6] PRIMARY KEY CLUSTERED ([CategoryID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for ProductInbound
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[ProductInbound]', RESEED, 5)
GO


-- ----------------------------
-- Triggers structure for table ProductInbound
-- ----------------------------
CREATE TRIGGER [dbo].[trg_ProductInbound]
ON [dbo].[ProductInbound]
WITH EXECUTE AS CALLER
FOR INSERT
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


-- ----------------------------
-- Primary Key structure for table ProductInbound
-- ----------------------------
ALTER TABLE [dbo].[ProductInbound] ADD CONSTRAINT [PK__ProductI__B4DB7A9573105ECB] PRIMARY KEY CLUSTERED ([InboundID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for ProductOutbound
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[ProductOutbound]', RESEED, 5)
GO


-- ----------------------------
-- Triggers structure for table ProductOutbound
-- ----------------------------
CREATE TRIGGER [dbo].[trg_ProductOutbound]
ON [dbo].[ProductOutbound]
WITH EXECUTE AS CALLER
FOR INSERT
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


-- ----------------------------
-- Primary Key structure for table ProductOutbound
-- ----------------------------
ALTER TABLE [dbo].[ProductOutbound] ADD CONSTRAINT [PK__ProductO__3518456118A39186] PRIMARY KEY CLUSTERED ([OutboundID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for Salesperson
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[Salesperson]', RESEED, 5)
GO


-- ----------------------------
-- Primary Key structure for table Salesperson
-- ----------------------------
ALTER TABLE [dbo].[Salesperson] ADD CONSTRAINT [PK__Salesper__C2010568341C6500] PRIMARY KEY CLUSTERED ([SalespersonID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for Supplier
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[Supplier]', RESEED, 5)
GO


-- ----------------------------
-- Primary Key structure for table Supplier
-- ----------------------------
ALTER TABLE [dbo].[Supplier] ADD CONSTRAINT [PK__Supplier__4BE66694648E265D] PRIMARY KEY CLUSTERED ([SupplierID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for TransferLog
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[TransferLog]', RESEED, 5)
GO


-- ----------------------------
-- Triggers structure for table TransferLog
-- ----------------------------
CREATE TRIGGER [dbo].[trg_TransferWarehouse]
ON [dbo].[TransferLog]
WITH EXECUTE AS CALLER
FOR INSERT
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


-- ----------------------------
-- Checks structure for table TransferLog
-- ----------------------------
ALTER TABLE [dbo].[TransferLog] ADD CONSTRAINT [CK__TransferL__Quant__5812160E] CHECK ([Quantity]>(0))
GO


-- ----------------------------
-- Primary Key structure for table TransferLog
-- ----------------------------
ALTER TABLE [dbo].[TransferLog] ADD CONSTRAINT [PK__Transfer__954901718F255666] PRIMARY KEY CLUSTERED ([TransferID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for Warehouse
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[Warehouse]', RESEED, 5)
GO


-- ----------------------------
-- Primary Key structure for table Warehouse
-- ----------------------------
ALTER TABLE [dbo].[Warehouse] ADD CONSTRAINT [PK__Warehous__2608AFD9F551E8B8] PRIMARY KEY CLUSTERED ([WarehouseID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table WarehouseProduct
-- ----------------------------
ALTER TABLE [dbo].[WarehouseProduct] ADD CONSTRAINT [PK__Warehous__ED4863B7FDA3642F] PRIMARY KEY CLUSTERED ([WarehouseID], [ProductID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Foreign Keys structure for table Product
-- ----------------------------
ALTER TABLE [dbo].[Product] ADD CONSTRAINT [FK__Product__Categor__3D5E1FD2] FOREIGN KEY ([CategoryID]) REFERENCES [dbo].[ProductCategory] ([CategoryID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO


-- ----------------------------
-- Foreign Keys structure for table ProductInbound
-- ----------------------------
ALTER TABLE [dbo].[ProductInbound] ADD CONSTRAINT [FK__ProductIn__Produ__49C3F6B7] FOREIGN KEY ([ProductID]) REFERENCES [dbo].[Product] ([ProductID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[ProductInbound] ADD CONSTRAINT [FK__ProductIn__Suppl__4AB81AF0] FOREIGN KEY ([SupplierID]) REFERENCES [dbo].[Supplier] ([SupplierID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[ProductInbound] ADD CONSTRAINT [FK__ProductIn__Wareh__4BAC3F29] FOREIGN KEY ([WarehouseID]) REFERENCES [dbo].[Warehouse] ([WarehouseID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO


-- ----------------------------
-- Foreign Keys structure for table ProductOutbound
-- ----------------------------
ALTER TABLE [dbo].[ProductOutbound] ADD CONSTRAINT [FK__ProductOu__Produ__4E88ABD4] FOREIGN KEY ([ProductID]) REFERENCES [dbo].[Product] ([ProductID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[ProductOutbound] ADD CONSTRAINT [FK__ProductOu__Sales__4F7CD00D] FOREIGN KEY ([SalespersonID]) REFERENCES [dbo].[Salesperson] ([SalespersonID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[ProductOutbound] ADD CONSTRAINT [FK__ProductOu__Wareh__5070F446] FOREIGN KEY ([WarehouseID]) REFERENCES [dbo].[Warehouse] ([WarehouseID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO


-- ----------------------------
-- Foreign Keys structure for table TransferLog
-- ----------------------------
ALTER TABLE [dbo].[TransferLog] ADD CONSTRAINT [FK__TransferL__Produ__5535A963] FOREIGN KEY ([ProductID]) REFERENCES [dbo].[Product] ([ProductID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[TransferLog] ADD CONSTRAINT [FK__TransferL__FromW__5629CD9C] FOREIGN KEY ([FromWarehouseID]) REFERENCES [dbo].[Warehouse] ([WarehouseID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[TransferLog] ADD CONSTRAINT [FK__TransferL__ToWar__571DF1D5] FOREIGN KEY ([ToWarehouseID]) REFERENCES [dbo].[Warehouse] ([WarehouseID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO


-- ----------------------------
-- Foreign Keys structure for table WarehouseProduct
-- ----------------------------
ALTER TABLE [dbo].[WarehouseProduct] ADD CONSTRAINT [FK__Warehouse__Wareh__44FF419A] FOREIGN KEY ([WarehouseID]) REFERENCES [dbo].[Warehouse] ([WarehouseID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

ALTER TABLE [dbo].[WarehouseProduct] ADD CONSTRAINT [FK__Warehouse__Produ__45F365D3] FOREIGN KEY ([ProductID]) REFERENCES [dbo].[Product] ([ProductID]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

