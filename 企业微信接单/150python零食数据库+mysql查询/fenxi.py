# coding=utf-8
import mysql.connector

# 连接MySQL数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="sancks"
)

# 创建游标对象
cursor = mydb.cursor()

# 总体报表
def overall_report():
    # 查询仓库总体统计信息
    cursor.execute("SELECT COUNT(*) FROM `商品资料`")
    total_products = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT `分类`) FROM `商品资料`")
    total_categories = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(`库存量`) FROM `商品资料`")
    total_stock = cursor.fetchone()[0]

    # 查询采购总体统计信息
    cursor.execute("SELECT COUNT(*) FROM `采购记录`")
    total_purchases = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(`采购量` * `采购单价`) FROM `采购记录`")
    total_purchase_amount = cursor.fetchone()[0]

    # 查询销售总体统计信息
    cursor.execute("SELECT COUNT(*) FROM `商品销售流水`")
    total_sales = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) FROM `商品销售流水` JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称`")
    total_sales_amount = cursor.fetchone()[0]

    # 查询财务总体统计信息
    cursor.execute("SELECT SUM(`采购量` * `采购单价`) FROM `采购记录`")
    total_purchase_expenses = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) FROM `商品销售流水` JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称`")
    total_revenue = cursor.fetchone()[0]

    print("总体报表:")
    print("仓库统计信息:")
    print("总商品数:", total_products)
    print("总分类数:", total_categories)
    print("总库存量:", total_stock)
    print()
    print("采购统计信息:")
    print("总采购次数:", total_purchases)
    print("总采购金额:", total_purchase_amount)
    print()
    print("销售统计信息:")
    print("总销售次数:", total_sales)
    print("总销售金额:", total_sales_amount)
    print()
    print("财务统计信息:")
    print("总采购支出金额:", total_purchase_expenses)
    print("总销售收入金额:", total_revenue)

# 仓库查询
def warehouse_query():
    # 查询商品分类及对应的商品数量
    cursor.execute("SELECT `分类`, COUNT(*) FROM `商品资料` GROUP BY `分类`")
    categories = cursor.fetchall()
    print("商品分类及对应的商品数量:")
    for category in categories:
        print(category[0], ":", category[1])
    print()

    # 查询进货价小于等于5元的商品列表
    cursor.execute("SELECT * FROM `商品资料` WHERE `成本` <= 5")
    cheap_products = cursor.fetchall()
    print("进货价小于等于5元的商品列表:")
    for product in cheap_products:
        print(product)
    print()

    # 计算每个商品的利润，并根据利润从高到低排序
    cursor.execute("SELECT `id`, (`售价` - `成本`) AS `利润` FROM `商品资料` ORDER BY `利润` DESC")
    products_profit = cursor.fetchall()
    print("每个商品的利润:")
    for product in products_profit:
        print("商品ID:", product[0], "利润:", product[1])
    print()

    # 库存最多的10个商品
    cursor.execute("SELECT * FROM `商品资料` ORDER BY `库存量` DESC LIMIT 10")
    top_10_stock = cursor.fetchall()
    print("库存最多的10个商品:")
    for product in top_10_stock:
        print(product)
    print()

    # 存货货值最高的10个商品
    cursor.execute("SELECT * FROM `商品资料` ORDER BY (`库存量` * `成本`) DESC LIMIT 10")
    top_10_inventory_value = cursor.fetchall()
    print("存货货值最高的10个商品:")
    for product in top_10_inventory_value:
        print(product)
    print()

# 采购查询
def purchase_query():
    # 查询所有供货商及其供货次数
    cursor.execute("SELECT `供应商`, COUNT(*) FROM `采购记录` GROUP BY `供应商`")
    suppliers = cursor.fetchall()
    print("供货商及其供货次数:")
    for supplier in suppliers:
        print(supplier[0], ":", supplier[1])
    print()

    # 查询2023年3月份的采购记录
    cursor.execute("SELECT * FROM `采购记录` WHERE YEAR(`采购时间`) = 2023 AND MONTH(`采购时间`) = 3")
    march_purchases = cursor.fetchall()
    print("2023年3月份的采购记录:")
    for purchase in march_purchases:
        print(purchase)
    print()

    # 查询采购量大于100的采购记录
    cursor.execute("SELECT * FROM `采购记录` WHERE `采购量` > 100")
    large_quantity_purchases = cursor.fetchall()
    print("采购量大于100的采购记录:")
    for purchase in large_quantity_purchases:
        print(purchase)
    print()

    # 查询采购金额最高的前10项采购记录
    cursor.execute("SELECT * FROM `采购记录` ORDER BY (`采购量` * `采购单价`) DESC LIMIT 10")
    top_10_purchase_amount = cursor.fetchall()
    print("采购金额最高的前10项采购记录:")
    for purchase in top_10_purchase_amount:
        print(purchase)
    print()

    # 查询“超友味”品牌的采购记录，并计算该品牌的总采购金额
    cursor.execute("SELECT * FROM `采购记录` WHERE `商品名称` LIKE '%超友味%'")
    chao_you_wei_purchases = cursor.fetchall()
    total_chao_you_wei_purchase_amount = sum([purchase[8] * purchase[9] for purchase in chao_you_wei_purchases])
    print("“超友味”品牌的采购记录:")
    for purchase in chao_you_wei_purchases:
        print(purchase)
    print("该品牌的总采购金额:", total_chao_you_wei_purchase_amount)
    print()

# 销售查询
def sales_query():
    # 查询每个商品分类的销售汇总金额
    cursor.execute("SELECT SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) FROM `商品销售流水` JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称` GROUP BY `商品分类`")
    sales_by_category = cursor.fetchall()
    print("每个商品分类的销售汇总金额:")
    # for category in sales_by_category:
    #     print(category[0], ":", category[1])
    # print()

    # 查询3月26日的销售记录
    cursor.execute("SELECT * FROM `商品销售流水` WHERE DATE(`销售时间`) = '2023-03-26'")
    march_26_sales = cursor.fetchall()
    print("3月26日的销售记录:")
    for sale in march_26_sales:
        print(sale)
    print()

    # 查询销售数量最高的前10项销售记录
    cursor.execute("SELECT * FROM `商品销售流水` ORDER BY `销售数量` DESC LIMIT 10")
    top_10_sales_quantity = cursor.fetchall()
    print("销售数量最高的前10项销售记录:")
    for sale in top_10_sales_quantity:
        print(sale)
    print()

    # 结合[商品资料]表，查询3月26日的销售明细，要求包含销售单价、销售总价等信息
    cursor.execute("SELECT `商品销售流水`.`id`, `商品销售流水`.`流水号`, `商品销售流水`.`销售时间`, `商品销售流水`.`会员卡号脱敏`, `商品资料`.`名称`, `商品资料`.`售价`, `商品销售流水`.`销售数量`, (`商品销售流水`.`销售数量` * `商品资料`.`售价`) AS `销售总价` FROM `商品销售流水` INNER JOIN `商品资料` ON `商品销售流水`.`商品条码` = `商品资料`.`条码` WHERE DATE(`商品销售流水`.`销售时间`) = '2023-03-26'")
    march_26_sales_detail = cursor.fetchall()
    print("3月26日的销售明细:")
    for sale in march_26_sales_detail:
        print(sale)
    print()

    # 查询所给销售区间里，每类商品的销售数量和销售金额
    cursor.execute("SELECT `商品分类`, SUM(`销售数量`), SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) FROM `商品销售流水` JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称` WHERE DATE(`销售时间`) BETWEEN '2023-03-01' AND '2023-03-31' GROUP BY `商品分类`")
    sales_by_category_interval = cursor.fetchall()
    print("所给销售区间里，每类商品的销售数量和销售金额:")
    for category in sales_by_category_interval:
        print(category[0], "销售数量:", category[1], "销售金额:", category[2])
    print()

# 财务查询
def finance_query():

    # 根据采购记录表，查询每个月的采购支出金额
    cursor.execute("SELECT YEAR(`采购时间`), MONTH(`采购时间`), SUM(`采购量` * `采购单价`) FROM `采购记录` GROUP BY YEAR(`采购时间`), MONTH(`采购时间`)")
    purchase_expenses_by_month = cursor.fetchall()
    print("每个月的采购支出金额:")
    for month in purchase_expenses_by_month:
        print(month[0], "年", month[1], "月:", month[2])
    print()

    # 根据商品销售流水表和商品资料，查询每个月的销售总收入
    cursor.execute("SELECT YEAR(`销售时间`), MONTH(`销售时间`), SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) FROM `商品销售流水` JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称` GROUP BY YEAR(`销售时间`), MONTH(`销售时间`)")
    sales_revenue_by_month = cursor.fetchall()
    print("每个月的销售总收入:")
    for month in sales_revenue_by_month:
        print(month[0], "年", month[1], "月:", month[2])
    print()

    # 根据商品资料表，分别按照进货价、销售价计算库存商品货值
    cursor.execute("SELECT '进货价', SUM(`库存量` * `成本`) FROM `商品资料` UNION SELECT '销售价', SUM(`库存量` * `售价`) FROM `商品资料`")
    inventory_value = cursor.fetchall()
    print("库存商品货值:")
    for value in inventory_value:
        print(value[0], ":", value[1])
    print()

    # 根据上述结果，计算每个月的营收情况
    cursor.execute('''SELECT `采购支出`.`年`, `采购支出`.`月`, `采购支出`, `销售收入`
FROM (
    SELECT YEAR(`采购记录`.`采购时间`) AS `年`, MONTH(`采购记录`.`采购时间`) AS `月`, SUM(`采购记录`.`采购量` * `采购记录`.`采购单价`) AS `采购支出`
    FROM `采购记录`
    GROUP BY YEAR(`采购记录`.`采购时间`), MONTH(`采购记录`.`采购时间`)
) AS `采购支出`
INNER JOIN (
    SELECT YEAR(`商品销售流水`.`销售时间`) AS `年`, MONTH(`商品销售流水`.`销售时间`) AS `月`, SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) AS `销售收入`
    FROM `商品销售流水`
    JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称`
    GROUP BY YEAR(`商品销售流水`.`销售时间`), MONTH(`商品销售流水`.`销售时间`)
) AS `销售收入`
ON `采购支出`.`年` = `销售收入`.`年` AND `采购支出`.`月` = `销售收入`.`月`
''')
    monthly_revenue = cursor.fetchall()
    print("每个月的营收情况:")
    for month in monthly_revenue:
        print(month[0], "年", month[1], "月: 采购支出:", month[2], "销售收入:", month[3])
    print()
    # cursor.execute("SELECT SUM(`商品销售流水`.`销售数量` * `商品资料`.`售价`) FROM `商品销售流水` JOIN `商品资料` ON `商品销售流水`.`商品名称` = `商品资料`.`名称`")

    # 计算每类商品的利润率情况
    cursor.execute('''SELECT `商品分类`, SUM((`售价` - `成本`) * `库存量`) / SUM(`成本` * `库存量`) * 100 
        FROM `商品资料` 
        JOIN `商品销售流水` ON `商品资料`.`条码` = `商品销售流水`.`商品条码`
        GROUP BY `商品分类`
        ''')
    profit_margin_by_category = cursor.fetchall()
    print("每类商品的利润率情况:")
    for category in profit_margin_by_category:
        print(category[0], "利润率:", category[1], "%")
    print()

# 调用函数进行查询
overall_report()
warehouse_query()
purchase_query()
sales_query()
finance_query()

# 关闭数据库连接
mydb.close()