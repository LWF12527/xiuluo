import pandas as pd
import pymysql

# 配置数据库连接信息
host = 'localhost'
port = 3306
user = 'root'
password = '123456'
database = 'sancks'

# 读取商品资料表数据
df1 = pd.read_excel('1-商品资料.xlsx')

# 读取商品销售流水表数据
df2 = pd.read_excel('3-商品销售流水.xlsx')

# 读取采购记录表数据
df3 = pd.read_excel('2-采购记录.xlsx')

# 建立数据库连接
conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
cursor = conn.cursor()

# 导入商品资料表数据
for index, row in df1.iterrows():
    sql = f"INSERT INTO `商品资料` (`名称`, `分类`, `条码`, `规格`, `主单位`, `库存量`, `成本`, `售价`) VALUES ('{row['名称']}', '{row['分类']}', '{row['条码']}', '{row['规格']}', '{row['主单位']}', {row['库存量']}, {row['成本']}, {row['售价']})"
    cursor.execute(sql)

# 导入商品销售流水表数据
for index, row in df2.iterrows():
    sql = f"INSERT INTO `商品销售流水` (`流水号`, `销售时间`, `会员卡号脱敏`, `商品名称`, `商品条码`, `规格`, `单位`, `商品分类`, `销售数量`) VALUES ('{row['流水号']}', '{row['销售时间']}', '{row['会员卡号脱敏']}', '{row['商品名称']}', '{row['商品条码']}', '{row['规格']}', '{row['单位']}', '{row['商品分类']}', {row['销售数量']})"
    cursor.execute(sql)

# 导入采购记录表数据
for index, row in df3.iterrows():
    sql = f"INSERT INTO `采购记录` (`采购单号`, `采购时间`, `供应商`, `商品条码`, `商品名称`, `单位`, `规格`, `采购量`, `采购单价`) VALUES ('{row['采购单号']}', '{row['采购时间']}', '{row['供应商']}', '{row['商品条码']}', '{row['商品名称']}', '{row['单位']}', '{row['规格']}', {row['采购量']}, {row['采购单价']})"
    cursor.execute(sql)

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()

