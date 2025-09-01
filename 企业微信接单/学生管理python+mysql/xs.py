import pymysql

def connect_to_db():
    # 连接到数据库
    connection = pymysql.connect(
        host='localhost',
        user='root',  # 替换为你的 MySQL 用户名
        password='123456',  # 替换为你的 MySQL 密码
        database='StudentManagementSystem'
    )
    return connection

def login(username, password):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM UserInfo WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        print(f"错误: {e}")
        return None

def register_user(username, password, role):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO UserInfo (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, role))
        conn.commit()
        conn.close()
        print("用户注册成功！")
    except Exception as e:
        print(f"错误: {e}")

def fetch_students():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM StudentInfo"
        cursor.execute(query)
        students = cursor.fetchall()
        conn.close()
        return students
    except Exception as e:
        print(f"错误: {e}")
        return []

def add_student(name, gender, age, contact_info):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO StudentInfo (name, gender, age, contact_info) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, gender, age, contact_info))
        conn.commit()
        conn.close()
        print("学生添加成功！")
    except Exception as e:
        print(f"错误: {e}")

def update_student(student_id, name, gender, age, contact_info):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE StudentInfo SET name = %s, gender = %s, age = %s, contact_info = %s WHERE student_id = %s"
        cursor.execute(query, (name, gender, age, contact_info, student_id))
        conn.commit()
        conn.close()
        print("学生信息更新成功！")
    except Exception as e:
        print(f"错误: {e}")

def delete_student(student_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "DELETE FROM StudentInfo WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        conn.close()
        print("学生删除成功！")
    except Exception as e:
        print(f"错误: {e}")

def main():
    while True:
        print("\n学生管理系统")
        print("1. 登录")
        print("2. 注册")
        print("3. 退出")
        choice = input("请输入你的选择: ")

        if choice == "1":
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            user = login(username, password)
            if user:
                print(f"欢迎 {user[1]}！")
                if user[3] == 'admin':
                    admin_menu()
                elif user[3] == 'teacher' or user[3] == 'student':
                    student_teacher_menu()
            else:
                print("用户名或密码错误")

        elif choice == "2":
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            role = input("请输入角色 (admin/teacher/student): ")
            register_user(username, password, role)

        elif choice == "3":
            print("退出系统，再见！")
            break

        else:
            print("无效的选择，请重试。")

def admin_menu():
    while True:
        print("\n管理员菜单")
        print("1. 查看学生信息")
        print("2. 添加学生")
        print("3. 更新学生信息")
        print("4. 删除学生")
        print("5. 退出登录")
        choice = input("请输入你的选择: ")

        if choice == "1":
            students = fetch_students()
            print("\n学生列表:")
            for student in students:
                print(student)

        elif choice == "2":
            name = input("请输入姓名: ")
            gender = input("请输入性别 (male/female): ")
            age = int(input("请输入年龄: "))
            contact_info = input("请输入联系方式: ")
            add_student(name, gender, age, contact_info)

        elif choice == "3":
            student_id = int(input("请输入要更新的学生ID: "))
            name = input("请输入新姓名: ")
            gender = input("请输入新性别 (male/female): ")
            age = int(input("请输入新年龄: "))
            contact_info = input("请输入新联系方式: ")
            update_student(student_id, name, gender, age, contact_info)

        elif choice == "4":
            student_id = int(input("请输入要删除的学生ID: "))
            delete_student(student_id)

        elif choice == "5":
            print("退出登录...")
            break

        else:
            print("无效的选择，请重试。")

def student_teacher_menu():
    while True:
        print("\n菜单")
        print("1. 查看学生信息")
        print("2. 退出登录")
        choice = input("请输入你的选择: ")

        if choice == "1":
            students = fetch_students()
            print("\n学生列表:")
            for student in students:
                print(student)

        elif choice == "2":
            print("退出登录...")
            break

        else:
            print("无效的选择，请重试。")

if __name__ == "__main__":
    main()
