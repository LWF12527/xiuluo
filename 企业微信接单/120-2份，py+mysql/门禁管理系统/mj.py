# -*- coding: utf-8 -*-

import pymysql

# 数据库配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "access_control_system",
    "charset": "utf8mb4"
}


# 连接数据库
def connect_db():
    try:
        connection = pymysql.connect(**db_config)
        return connection
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return None


# 插入用户数据
def insert_user():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            name = input("请输入用户名：")
            phone = input("请输入用户电话号码：")

            # 检查手机号是否唯一
            sql_check = "SELECT COUNT(*) FROM users WHERE phone = %s"
            cursor.execute(sql_check, (phone,))
            result = cursor.fetchone()
            if result[0] > 0:
                print("该电话号码已存在，请输入一个唯一的电话号码！")
                return

            # 插入用户数据
            sql_user = "INSERT INTO users (name, phone) VALUES (%s, %s)"
            cursor.execute(sql_user, (name, phone))

            connection.commit()
            print("用户数据插入成功！")
    except Exception as e:
        print(f"插入用户数据失败: {e}")
    finally:
        connection.close()


# 插入门禁设备数据
def insert_device():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            location = input("请输入门禁设备位置：")

            # 插入设备数据
            sql_device = "INSERT INTO access_devices (location) VALUES (%s)"
            cursor.execute(sql_device, (location,))

            connection.commit()
            print("门禁设备数据插入成功！")
    except Exception as e:
        print(f"插入门禁设备数据失败: {e}")
    finally:
        connection.close()


# 插入访问记录
def insert_access_log():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            user_id = int(input("请输入用户ID："))
            device_id = int(input("请输入设备ID："))
            access_result = input("请输入访问结果（SUCCESS/FAILURE）：").upper()

            # 插入访问记录数据
            sql_log = "INSERT INTO access_logs (user_id, device_id, access_result) VALUES (%s, %s, %s)"
            cursor.execute(sql_log, (user_id, device_id, access_result))

            connection.commit()
            print("访问记录插入成功！")
    except Exception as e:
        print(f"插入访问记录失败: {e}")
    finally:
        connection.close()


# 查询数据
def query_data():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            # 查询视图数据
            sql_query = "SELECT * FROM access_logs_view"
            cursor.execute(sql_query)
            results = cursor.fetchall()
            print("查询结果：")
            for row in results:
                print(row)
    except Exception as e:
        print(f"查询数据失败: {e}")
    finally:
        connection.close()


# 更新数据
def update_data():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            # 更新用户电话号码
            sql_update = "UPDATE users SET phone = %s WHERE name = %s"
            name = input("请输入要更新的用户名：")
            new_phone = input("请输入新的电话号码：")
            cursor.execute(sql_update, (new_phone, name))

            connection.commit()
            print("数据更新成功！")
    except Exception as e:
        print(f"更新数据失败: {e}")
    finally:
        connection.close()


# 删除数据
def delete_data():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            # 删除访问记录
            log_id = int(input("请输入要删除的访问记录ID："))
            sql_delete = "DELETE FROM access_logs WHERE log_id = %s"
            cursor.execute(sql_delete, (log_id,))

            connection.commit()
            print("数据删除成功！")
    except Exception as e:
        print(f"删除数据失败: {e}")
    finally:
        connection.close()


# 主函数
def main():
    while True:
        print("\n=== 门禁系统数据库操作 ===")
        print("1. 插入用户数据")
        print("2. 插入门禁设备数据")
        print("3. 插入访问记录数据")
        print("4. 查询数据")
        print("5. 更新数据")
        print("6. 删除数据")
        print("7. 退出")
        choice = input("请选择操作: ")

        if choice == "1":
            insert_user()
        elif choice == "2":
            insert_device()
        elif choice == "3":
            insert_access_log()
        elif choice == "4":
            query_data()
        elif choice == "5":
            update_data()
        elif choice == "6":
            delete_data()
        elif choice == "7":
            print("退出程序。")
            break
        else:
            print("无效选择，请重新输入！")


if __name__ == "__main__":
    main()
