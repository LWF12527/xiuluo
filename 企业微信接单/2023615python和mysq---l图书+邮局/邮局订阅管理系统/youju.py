
# coding=utf-8
import mysql.connector

# 连接到MySQL数据库
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="youju"
)

# 创建游标对象
cursor = db.cursor()

# 报刊数据管理
def manage_newspapers():
    print("报刊数据管理")

    while True:
        print("1. 添加报刊")
        print("2. 修改报刊")
        print("3. 删除报刊")
        print("4. 显示报刊列表")
        print("5. 返回主菜单")

        choice = input("请选择操作：")

        if choice == "1":
            newspaper_name = input("请输入报刊名称：")
            newspaper_price = float(input("请输入报刊价格："))

            # 执行SQL插入语句
            sql = "INSERT INTO newspapers (name, price) VALUES (%s, %s)"
            values = (newspaper_name, newspaper_price)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("报刊添加成功！")

        elif choice == "2":
            newspaper_id = int(input("请输入要修改的报刊ID："))
            new_price = float(input("请输入新的报刊价格："))

            # 执行SQL更新语句
            sql = "UPDATE newspapers SET price = %s WHERE id = %s"
            values = (new_price, newspaper_id)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("报刊修改成功！")

        elif choice == "3":
            newspaper_id = int(input("请输入要删除的报刊ID："))

            # 执行SQL删除语句
            sql = "DELETE FROM newspapers WHERE id = %s"
            values = (newspaper_id,)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("报刊删除成功！")

        elif choice == "4":
            # 执行SQL查询语句
            sql = "SELECT * FROM newspapers"
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()

            # 显示报刊列表
            for row in result:
                print("ID: {}，名称: {}，价格: {}".format(row[0], row[1], row[2]))

        elif choice == "5":
            break

# 用户数据管理
def manage_users():
    print("用户数据管理")

    while True:
        print("1. 添加用户")
        print("2. 修改用户信息")
        print("3. 删除用户")
        print("4. 显示用户列表")
        print("5. 返回主菜单")

        choice = input("请选择操作：")

        if choice == "1":
            user_name = input("请输入用户名：")
            user_address = input("请输入用户地址：")

            # 执行SQL插入语句
            sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
            values = (user_name, user_address)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("用户添加成功！")

        elif choice == "2":
            user_id = int(input("请输入要修改的用户ID："))
            new_address = input("请输入新的用户地址：")

            # 执行SQL更新语句
            sql = "UPDATE users SET address = %s WHERE id = %s"
            values = (new_address, user_id)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("用户信息修改成功！")

        elif choice == "3":
            user_id = int(input("请输入要删除的用户ID："))

            # 执行SQL删除语句
            sql = "DELETE FROM users WHERE id = %s"
            values = (user_id,)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("用户删除成功！")

        elif choice == "4":
            # 执行SQL查询语句
            sql = "SELECT * FROM users"
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()

            # 显示用户列表
            for row in result:
                print("ID: {}，用户名: {}，地址: {}".format(row[0], row[1], row[2]))

        elif choice == "5":
            break

# 订阅管理
def manage_subscriptions():
    print("订阅管理")

    while True:
        print("1. 添加订阅")
        print("2. 修改订阅信息")
        print("3. 取消订阅")
        print("4. 显示订阅列表")
        print("5. 返回主菜单")

        choice = input("请选择操作：")

        if choice == "1":
            user_id = int(input("请输入用户ID："))
            newspaper_id = int(input("请输入报刊ID："))
            subscription_date = input("请输入订阅日期（YYYY-MM-DD）：")

            # 执行SQL插入语句
            sql = "INSERT INTO subscriptions (user_id, newspaper_id, date) VALUES (%s, %s, %s)"
            values = (user_id, newspaper_id, subscription_date)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("订阅添加成功！")

        elif choice == "2":
            subscription_id = int(input("请输入要修改的订阅ID："))
            new_date = input("请输入新的订阅日期（YYYY-MM-DD）：")

            # 执行SQL更新语句
            sql = "UPDATE subscriptions SET date = %s WHERE id = %s"
            values = (new_date, subscription_id)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("订阅信息修改成功！")

        elif choice == "3":
            subscription_id = int(input("请输入要取消的订阅ID："))

            # 执行SQL删除语句
            sql = "DELETE FROM subscriptions WHERE id = %s"
            values = (subscription_id,)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("订阅取消成功！")

        elif choice == "4":
            # 执行SQL查询语句
            sql = "SELECT * FROM subscriptions"
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()

            # 显示订阅列表
            for row in result:
                print("ID: {}，用户ID: {}，报刊ID: {}，日期: {}".format(row[0], row[1], row[2], row[3]))

        elif choice == "5":
            break

# 报刊入库管理
def manage_stock():
    print("报刊入库管理")

    while True:
        print("1. 添加入库记录")
        print("2. 修改入库记录")
        print("3. 删除入库记录")
        print("4. 显示入库记录列表")
        print("5. 返回主菜单")

        choice = input("请选择操作：")

        if choice == "1":
            newspaper_id = int(input("请输入报刊ID："))
            quantity = int(input("请输入入库数量："))

            # 执行SQL插入语句
            sql = "INSERT INTO stock (newspaper_id, quantity) VALUES (%s, %s)"
            values = (newspaper_id, quantity)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("入库记录添加成功！")

        elif choice == "2":
            stock_id = int(input("请输入要修改的入库记录ID："))
            new_quantity = int(input("请输入新的入库数量："))

            # 执行SQL更新语句
            sql = "UPDATE stock SET quantity = %s WHERE id = %s"
            values = (new_quantity, stock_id)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("入库记录修改成功！")

        elif choice == "3":
            stock_id = int(input("请输入要删除的入库记录ID："))

            # 执行SQL删除语句
            sql = "DELETE FROM stock WHERE id = %s"
            values = (stock_id,)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("入库记录删除成功！")

        elif choice == "4":
            # 执行SQL查询语句
            sql = "SELECT * FROM stock"
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()

            # 显示入库记录列表
            for row in result:
                print("ID: {}，报刊ID: {}，数量: {}".format(row[0], row[1], row[2]))

        elif choice == "5":
            break

# 报刊发放管理
def manage_distribution():
    print("报刊发放管理")

    while True:
        print("1. 添加发放记录")
        print("2. 修改发放记录")
        print("3. 删除发放记录")
        print("4. 显示发放记录列表")
        print("5. 返回主菜单")

        choice = input("请选择操作：")

        if choice == "1":
            user_id = int(input("请输入用户ID："))
            newspaper_id = int(input("请输入报刊ID："))
            quantity = int(input("请输入发放数量："))

            # 执行SQL插入语句
            sql = "INSERT INTO distribution (user_id, newspaper_id, quantity) VALUES (%s, %s, %s)"
            values = (user_id, newspaper_id, quantity)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("发放记录添加成功！")

        elif choice == "2":
            distribution_id = int(input("请输入要修改的发放记录ID："))
            new_quantity = int(input("请输入新的发放数量："))

            # 执行SQL更新语句
            sql = "UPDATE distribution SET quantity = %s WHERE id = %s"
            values = (new_quantity, distribution_id)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("发放记录修改成功！")

        elif choice == "3":
            distribution_id = int(input("请输入要删除的发放记录ID："))

            # 执行SQL删除语句
            sql = "DELETE FROM distribution WHERE id = %s"
            values = (distribution_id,)
            cursor.execute(sql, values)

            # 提交事务
            db.commit()

            print("发放记录删除成功！")

        elif choice == "4":
            # 执行SQL查询语句
            sql = "SELECT * FROM distribution"
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()

            # 显示发放记录列表
            for row in result:
                print("ID: {}，用户ID: {}，报刊ID: {}，数量: {}".format(row[0], row[1], row[2], row[3]))

        elif choice == "5":
            break

# 主菜单
def main_menu():
    while True:
        print("欢迎使用邮局订阅管理系统")
        print("1. 报刊数据管理")
        print("2. 用户数据管理")
        print("3. 订阅管理")
        print("4. 报刊入库管理")
        print("5. 报刊发放管理")
        print("6. 退出程序")

        choice = input("请选择操作：")

        if choice == "1":
            manage_newspapers()
        elif choice == "2":
            manage_users()
        elif choice == "3":
            manage_subscriptions()
        elif choice == "4":
            manage_stock()
        elif choice == "5":
            manage_distribution()
        elif choice == "6":
            break
        else:
            print("无效的选择，请重新输入！")

# 创建数据库表
def create_tables():
    # 创建报刊表
    cursor.execute("CREATE TABLE IF NOT EXISTS newspapers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price FLOAT)")

    # 创建用户表
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    # 创建订阅表
    cursor.execute("CREATE TABLE IF NOT EXISTS subscriptions (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, newspaper_id INT, date DATE, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (newspaper_id) REFERENCES newspapers(id))")

    # 创建入库记录表
    cursor.execute("CREATE TABLE IF NOT EXISTS stock (id INT AUTO_INCREMENT PRIMARY KEY, newspaper_id INT, quantity INT, FOREIGN KEY (newspaper_id) REFERENCES newspapers(id))")

    # 创建发放记录表
    cursor.execute("CREATE TABLE IF NOT EXISTS distribution (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, newspaper_id INT, quantity INT, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (newspaper_id) REFERENCES newspapers(id))")

# 初始化数据库
def initialize_database():
    # 删除已存在的表
    cursor.execute("DROP TABLE IF EXISTS subscriptions")
    cursor.execute("DROP TABLE IF EXISTS distribution")
    cursor.execute("DROP TABLE IF EXISTS stock")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS newspapers")

    # 创建新表
    create_tables()

# 初始化数据库
# initialize_database()

# 运行主菜单
main_menu()

