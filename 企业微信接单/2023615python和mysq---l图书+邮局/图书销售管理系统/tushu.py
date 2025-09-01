import mysql.connector
from datetime import date

# 连接到MySQL数据库
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="bookstore"
)

# 创建游标对象
cursor = db.cursor()

def add_book(title, author, price, stock):
    # 添加书籍信息到books表格
    sql = "INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)"
    val = (title, author, price, stock)
    cursor.execute(sql, val)
    db.commit()
    print("书籍添加成功！")

def add_supplier(name, contact):
    # 添加供应商信息到suppliers表格
    sql = "INSERT INTO suppliers (name, contact) VALUES (%s, %s)"
    val = (name, contact)
    cursor.execute(sql, val)
    db.commit()
    print("供应商添加成功！")

def add_purchase(book_id, supplier_id, quantity):
    # 添加进货信息到purchases表格
    purchase_date = date.today().strftime("%Y-%m-%d")
    sql = "INSERT INTO purchases (book_id, supplier_id, quantity, purchase_date) VALUES (%s, %s, %s, %s)"
    val = (book_id, supplier_id, quantity, purchase_date)
    cursor.execute(sql, val)
    db.commit()

    # 更新库存量
    sql = "UPDATE books SET stock = stock + %s WHERE id = %s"
    val = (quantity, book_id)
    cursor.execute(sql, val)
    db.commit()

    print("进货成功！")

def add_return(book_id, quantity):
    # 添加退货信息到returns表格
    return_date = date.today().strftime("%Y-%m-%d")
    sql = "INSERT INTO returns (book_id, quantity, return_date) VALUES (%s, %s, %s)"
    val = (book_id, quantity, return_date)
    cursor.execute(sql, val)
    db.commit()

    # 更新库存量
    sql = "UPDATE books SET stock = stock - %s WHERE id = %s"
    val = (quantity, book_id)
    cursor.execute(sql, val)
    db.commit()

    print("退货成功！")

def get_sales_report():
    # 获取销售报表
    sql = """
    SELECT b.title, SUM(s.quantity) as total_quantity, SUM(b.price * s.quantity) as total_amount
    FROM sales s
    INNER JOIN books b ON s.book_id = b.id
    GROUP BY b.title
    ORDER BY total_amount DESC
    """
    cursor.execute(sql)
    result = cursor.fetchall()

    # 打印销售报表
    print("销售报表:")
    print("{:<30} {:<15} {:<15}".format("书籍标题", "销售总量", "销售总额"))
    for row in result:
        title, total_quantity, total_amount = row
        print("{:<30} {:<15} {:<15}".format(title, total_quantity, total_amount))

def sell_book(book_id, quantity):
    # 检查库存量是否足够
    sql = "SELECT stock FROM books WHERE id = %s"
    val = (book_id,)
    cursor.execute(sql, val)
    stock = cursor.fetchone()[0]

    if quantity > stock:
        print("库存不足，销售失败！")
    else:
        # 添加销售信息到sales表格
        sale_date = date.today().strftime("%Y-%m-%d")
        sql = "INSERT INTO sales (book_id, quantity, sale_date) VALUES (%s, %s, %s)"
        val = (book_id, quantity, sale_date)
        cursor.execute(sql, val)
        db.commit()

        # 更新库存量
        sql = "UPDATE books SET stock = stock - %s WHERE id = %s"
        val = (quantity, book_id)
        cursor.execute(sql, val)
        db.commit()

        print("销售成功！")

def main_menu():
    while True:
        print("欢迎使用图书销售管理系统")
        print("1. 添加书籍")
        print("2. 添加供应商")
        print("3. 进货")
        print("4. 退货")
        print("5. 销售")
        print("6. 统计报表")
        print("0. 退出系统")
        choice = input("请输入选项：")

        if choice == "1":
            title = input("请输入书籍标题：")
            author = input("请输入作者：")
            price = float(input("请输入价格："))
            stock = int(input("请输入库存量："))
            add_book(title, author, price, stock)
        elif choice == "2":
            name = input("请输入供应商名称：")
            contact = input("请输入联系方式：")
            add_supplier(name, contact)
        elif choice == "3":
            book_id = int(input("请输入书籍ID："))
            supplier_id = int(input("请输入供应商ID："))
            quantity = int(input("请输入进货数量："))
            add_purchase(book_id, supplier_id, quantity)
        elif choice == "4":
            book_id = int(input("请输入书籍ID："))
            quantity = int(input("请输入退货数量："))
            add_return(book_id, quantity)
        elif choice == "5":
            book_id = int(input("请输入书籍ID："))
            quantity = int(input("请输入销售数量："))
            sell_book(book_id, quantity)
        elif choice == "6":
            get_sales_report()
        elif choice == "0":
            break
        else:
            print("无效选项！")

    # 关闭数据库连接
    db.close()

# 启动系统
main_menu()