import mysql.connector

# 连接数据库
cnx = mysql.connector.connect(user='root', password='123456',
                              host='localhost', database='stoke')
cursor = cnx.cursor()

# 入库操作
def inbound():
    product_id = int(input("请输入产品号："))
    warehouse_id = int(input("请输入仓库号："))
    delivery_person = input("请输入送货人：")
    quantity = int(input("请输入入库数量："))
    date = input("请输入入库日期（格式：YYYY-MM-DD）：")

    # 更新库存表
    query = ("INSERT INTO inventory (product_id, warehouse_id, quantity) "
             "VALUES (%s, %s, %s) "
             "ON DUPLICATE KEY UPDATE quantity = quantity + %s")
    data = (product_id, warehouse_id, quantity, quantity)
    cursor.execute(query, data)
    cnx.commit()

    # 插入入库记录
    query = ("INSERT INTO inbound (product_id, warehouse_id, delivery_person, quantity, date) "
             "VALUES (%s, %s, %s, %s, %s)")
    data = (product_id, warehouse_id, delivery_person, quantity, date)
    cursor.execute(query, data)
    cnx.commit()

    print("入库成功！")

# 出库操作
def outbound():
    product_id = int(input("请输入产品号："))
    warehouse_id = int(input("请输入仓库号："))
    delivery_person = input("请输入送货人：")
    quantity = int(input("请输入出库数量："))
    date = input("请输入出库日期（格式：YYYY-MM-DD）：")

    # 检查库存是否足够
    query = ("SELECT quantity FROM inventory "
             "WHERE product_id = %s AND warehouse_id = %s")
    data = (product_id, warehouse_id)
    cursor.execute(query, data)
    result = cursor.fetchone()
    if not result or result[0] < quantity:
        print("库存不足，出库失败！")
        return

    # 更新库存表
    query = ("UPDATE inventory SET quantity = quantity - %s "
             "WHERE product_id = %s AND warehouse_id = %s")
    data = (quantity, product_id, warehouse_id)
    cursor.execute(query, data)
    cnx.commit()

    # 插入出库记录
    query = ("INSERT INTO outbound (product_id, warehouse_id, delivery_person, quantity, date) "
             "VALUES (%s, %s, %s, %s, %s)")
    data = (product_id, warehouse_id, delivery_person, quantity, date)
    cursor.execute(query, data)
    cnx.commit()

    print("出库成功！")

# 查询库存数量
def get_inventory():
    product_id = int(input("请输入产品号："))
    warehouse_id = int(input("请输入仓库号："))

    query = ("SELECT quantity FROM inventory "
             "WHERE product_id = %s AND warehouse_id = %s")
    data = (product_id, warehouse_id)
    cursor.execute(query, data)
    result = cursor.fetchone()
    if result:
        print("库存数量：", result[0])
    else:
        print("该产品在该仓库中不存在！")

# 查询出入库记录
def get_records():
    query = ("SELECT 'inbound' AS type, product_id, warehouse_id, delivery_person, quantity, date "
             "FROM inbound "
             "UNION "
             "SELECT 'outbound' AS type, product_id, warehouse_id, delivery_person, quantity, date "
             "FROM outbound "
             "ORDER BY date DESC")
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("出入库记录：")
        for row in result:
            print(row)
    else:
        print("暂无出入库记录！")

# 主函数
def main():
    while True:
        print("请选择操作：")
        print("1. 入库")
        print("2. 出库")
        print("3. 查询库存数量")
        print("4. 查询出入库记录")
        print("5. 退出")
        choice = input()

        if choice == "1":
            inbound()
        elif choice == "2":
            outbound()
        elif choice == "3":
            get_inventory()
        elif choice == "4":
            get_records()
        elif choice == "5":
            break
        else:
            print("无效的选择，请重新输入！")

    # 关闭数据库连接
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    main()
