-- 创建数据库
CREATE DATABASE IF NOT EXISTS agriculture_data;

-- 切换到新创建的数据库
USE agriculture_data;

-- 创建农产品批发价格数据表（修改字段名避免冲突）
CREATE TABLE IF NOT EXISTS crop_prices (
    year_month_value INT,
    product VARCHAR(50),
    price DECIMAL(10,2),
    category VARCHAR(50)
);


-- 导入农产品批发价格数据集，（！如果无法导入，有安全验证，请用navicat手动导入csv文件）
LOAD DATA INFILE 'wholesale_price_of_agricultural_products.csv'
INTO TABLE crop_prices
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year_month, product, price, category);

