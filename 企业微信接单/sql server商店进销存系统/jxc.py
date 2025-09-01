import pyodbc

# 连接 SQL Server 数据库
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=localhost;'  # 请替换为您的 SQL Server 服务器地址
    'DATABASE=jxc;'      # 数据库名
    'UID=sa;'            # 用户名
    'PWD=L.sa123456;'  # 密码
)

# 建立数据库连接
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
except Exception as e:
    print("数据库连接失败：", e)
    exit()

# 增加商品入库
def add_inbound():
    product_id = input("输入商品ID: ")
    supplier_id = input("输入供应商ID: ")
    quantity = input("输入入库数量: ")
    warehouse_id = input("输入仓库ID: ")
    inbound_date = input("输入入库日期 (YYYY-MM-DD): ")

    try:
        query = "INSERT INTO ProductInbound (ProductID, SupplierID, Quantity, WarehouseID, InboundDate) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, product_id, supplier_id, quantity, warehouse_id, inbound_date)
        conn.commit()
        print("入库成功！")
    except Exception as e:
        print("入库失败：", e)

# 增加商品出库
def add_outbound():
    product_id = input("输入商品ID: ")
    salesperson_id = input("输入业务员ID: ")
    quantity = input("输入出库数量: ")
    warehouse_id = input("输入仓库ID: ")
    outbound_date = input("输入出库日期 (YYYY-MM-DD): ")

    try:
        query = "INSERT INTO ProductOutbound (ProductID, SalespersonID, Quantity, WarehouseID, OutboundDate) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, product_id, salesperson_id, quantity, warehouse_id, outbound_date)
        conn.commit()
        print("出库成功！")
    except Exception as e:
        print("出库失败：", e)

# 查询入库表
def view_inbound():
    try:
        query = "SELECT * FROM ProductInbound"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n入库表信息：")
        for row in results:
            print(row)
    except Exception as e:
        print("查询失败：", e)

# 查询出库表
def view_outbound():
    try:
        query = "SELECT * FROM ProductOutbound"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n出库表信息：")
        for row in results:
            print(row)
    except Exception as e:
        print("查询失败：", e)

# 商品信息管理（增删改查）
def manage_product():
    while True:
        print("\n--- 商品信息管理 ---")
        print("1. 添加商品")
        print("2. 删除商品")
        print("3. 更新商品")
        print("4. 查看商品")
        print("5. 返回主菜单")
        choice = input("请选择功能: ")

        if choice == '1':
            name = input("输入商品名称: ")
            category_id = input("输入商品类别ID: ")
            unit = input("输入商品单位: ")
            try:
                query = "INSERT INTO Product (ProductName, CategoryID, Unit) VALUES (?, ?, ?)"
                cursor.execute(query, name, category_id, unit)
                conn.commit()
                print("商品添加成功！")
            except Exception as e:
                print("添加失败：", e)

        elif choice == '2':
            product_id = input("输入要删除的商品ID: ")
            try:
                query = "DELETE FROM Product WHERE ProductID = ?"
                cursor.execute(query, product_id)
                conn.commit()
                print("商品删除成功！")
            except Exception as e:
                print("删除失败：", e)

        elif choice == '3':
            product_id = input("输入商品ID: ")
            name = input("输入新商品名称: ")
            category_id = input("输入新类别ID: ")
            unit = input("输入新单位: ")
            try:
                query = "UPDATE Product SET ProductName = ?, CategoryID = ?, Unit = ? WHERE ProductID = ?"
                cursor.execute(query, name, category_id, unit, product_id)
                conn.commit()
                print("商品更新成功！")
            except Exception as e:
                print("更新失败：", e)

        elif choice == '4':
            try:
                query = "SELECT * FROM Product"
                cursor.execute(query)
                results = cursor.fetchall()
                print("\n商品信息：")
                for row in results:
                    print(row)
            except Exception as e:
                print("查询失败：", e)

        elif choice == '5':
            break
        else:
            print("无效选择，请重试！")

# 主菜单
def main_menu():
    while True:
        print("\n--- 仓库管理系统 ---")
        print("1. 商品入库")
        print("2. 商品出库")
        print("3. 查询入库表")
        print("4. 查询出库表")
        print("5. 商品信息管理")
        print("6. 退出系统")
        choice = input("请选择功能: ")

        if choice == '1':
            add_inbound()
        elif choice == '2':
            add_outbound()
        elif choice == '3':
            view_inbound()
        elif choice == '4':
            view_outbound()
        elif choice == '5':
            manage_product()
        elif choice == '6':
            print("退出系统！")
            break
        else:
            print("无效选择，请重试！")

if __name__ == "__main__":
    main_menu()
    cursor.close()
    conn.close()
