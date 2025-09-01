#coding=utf-8
import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="food_court"
)

# 食堂基本信息
food_court_info = {
    "name": "西一食堂",
    "location": "西区",
    "description": "西一食堂是一家提供美食的食堂，拥有丰富的菜品种类和优质的服务，欢迎光临！"
}

# 定义用户类
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

# 定义管理员类
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    # 设定当日菜品的种类和数量
    def set_menu(self, menu):
        cursor = mydb.cursor()
        sql = "INSERT INTO menu (name, quantity) VALUES (%s, %s)"
        val = (menu["name"], menu["quantity"])
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

    # 制定菜品的成本和销售价格
    def set_price(self, menu):
        cursor = mydb.cursor()
        sql = "UPDATE menu SET cost = %s, price = %s WHERE name = %s"
        val = (menu["cost"], menu["price"], menu["name"])
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record updated.")

    # 计算当日食堂的盈利
    def calculate_profit(self):
        cursor = mydb.cursor()
        sql = "SELECT SUM(price - cost) AS profit FROM menu"
        cursor.execute(sql)
        result = cursor.fetchone()
        print("Today's profit is", result[0])

# 定义阿姨类
class Aunt(User):
    def __init__(self, username, password):
        super().__init__(username, password, "aunt")

    # 确定所选择的饭菜，计算总价格并扣除饭费
    def order_food(self, menu, user):
        cursor = mydb.cursor()
        sql = "SELECT price FROM menu WHERE name = %s"
        val = (menu,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            price = result[0]
            sql = "SELECT balance FROM user WHERE username = %s"
            val = (user.username,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                balance = result[0]
                if balance >= price:
                    balance -= price
                    sql = "UPDATE user SET balance = %s WHERE username = %s"
                    val = (balance, user.username)
                    cursor.execute(sql, val)
                    mydb.commit()
                    print("Order placed successfully. Your balance is", balance)
                else:
                    print("Insufficient balance. Please recharge your card.")
            else:
                print("User does not exist.")
        else:
            print("Menu item not found.")

# 定义小白类
class White(User):
    def __init__(self, username, password):
        super().__init__(username, password, "white")

    # 选择今天想要吃的饭菜
    def select_food(self):
        cursor = mydb.cursor()
        sql = "SELECT name FROM menu"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Today's menu:")
        for menu in result:
            print(menu[0])
        food = input("Please select a menu item: ")
        return food

    # 确定饭卡内的资金是否足够
    def check_balance(self):
        cursor = mydb.cursor()
        sql = "SELECT balance FROM user WHERE username = %s"
        val = (self.username,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            balance = result[0]
            print("Your current balance is", balance)
        else:
            print("User does not exist.")

    # 对菜品的评价
    def rate_food(self, menu):
        cursor = mydb.cursor()
        sql = "SELECT rating FROM menu WHERE name = %s"
        val = (menu,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            rating = result[0]
            print("The current rating for", menu, "is", rating)
            new_rating = int(input("Please rate this menu item (1-5): "))
            if new_rating >= 1 and new_rating <= 5:
                sql = "UPDATE menu SET rating = %s WHERE name = %s"
                val = (new_rating, menu)
                cursor.execute(sql, val)
                mydb.commit()
                print("Thank you for your rating.")
            else:
                print("Invalid rating.")
        else:
            print("Menu item not found.")

# 用户登录函数
def login():
    cursor = mydb.cursor()
    username = input("Username: ")
    password = input("Password: ")
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        role = result[3]
        if role == "admin":
            return Admin(username, password)
        elif role == "aunt":
            return Aunt(username, password)
        elif role == "white":
            return White(username, password)
    else:
        print("Invalid username or password.")
        return None

# 用户注册函数
def register():
    cursor = mydb.cursor()
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (admin/aunt/white): ")
    sql = "INSERT INTO user (username, password, role) VALUES (%s, %s, %s)"
    val = (username, password, role)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
    if role == "admin":
        return Admin(username, password)
    elif role == "aunt":
        return Aunt(username, password)
    elif role == "white":
        return White(username, password)

# 主函数
if __name__ == '__main__':
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Please select an option: ")
        if choice == "1":
            user = login()
            if user:
                # 显示食堂基本信息
                print("Food court name:", food_court_info["name"])
                print("Location:", food_court_info["location"])
                print("Description:", food_court_info["description"])
                if user.role == "admin":
                    while True:
                        print("1. Set menu")
                        print("2. Set price")
                        print("3. Calculate profit")
                        print("4. Logout")
                        choice = input("Please select an option: ")
                        if choice == "1":
                            name = input("Menu item name: ")
                            quantity = int(input("Quantity: "))
                            menu = {"name": name, "quantity": quantity}
                            user.set_menu(menu)
                        elif choice == "2":
                            name = input("Menu item name: ")
                            cost = float(input("Cost: "))
                            price = float(input("Price: "))
                            menu = {"name": name, "cost": cost, "price": price}
                            user.set_price(menu)
                        elif choice == "3":
                            user.calculate_profit()
                        elif choice == "4":
                            break
                        else:
                            print("Invalid choice.")
                elif user.role == "aunt":
                    while True:
                        print("1. Order food")
                        print("2. Logout")
                        choice = input("Please select an option: ")
                        if choice == "1":
                            menu = input("Menu item name: ")
                            user.order_food(menu, user)
                        elif choice == "2":
                            break
                        else:
                            print("Invalid choice.")
                elif user.role == "white":
                    while True:
                        print("1. Select food")
                        print("2. Check balance")
                        print("3. Rate food")
                        print("4. Logout")
                        choice = input("Please select an option: ")
                        if choice == "1":
                            food = user.select_food()
                            print("You have selected", food)
                        elif choice == "2":
                            user.check_balance()
                        elif choice == "3":
                            menu = input("Menu item name: ")
                            user.rate_food(menu)
                        elif choice == "4":
                            break
                        else:
                            print("Invalid choice.")
        elif choice == "2":
            user = register()
            if user:
                if user.role == "admin":
                    print("Welcome, admin.")
                elif user.role == "aunt":
                    print("Welcome, aunt.")
                elif user.role == "white":
                    print("Welcome, white.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


