# -*- coding: gbk -*-
import pyodbc

# 设置SQL Server数据库连接信息
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost,1433;'  # 这里填写你的SQL Server实例的名称或IP
    r'DATABASE=gxjs;'  # 数据库名称
    r'UID=sa;'  # SQL Server用户名
    r'PWD=L.sa123456'  # SQL Server密码
)

# 连接到数据库
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
print(cursor)

def add_teacher(teacher_id, name, gender, birth_date, department):
    try:
        cursor.execute('''
        INSERT INTO Teacher (teacher_id, name, gender, birth_date, department)
        VALUES (?, ?, ?, ?, ?)
        ''', (teacher_id, name, gender, birth_date, department))
        conn.commit()
        print("教师信息已添加！")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def delete_teacher(teacher_id):
    try:
        cursor.execute('''
        DELETE FROM Teacher WHERE teacher_id = ?
        ''', (teacher_id,))
        conn.commit()
        print("教师信息已删除！")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def update_teacher(teacher_id, name=None, gender=None, birth_date=None, department=None):
    try:
        update_fields = []
        update_values = []

        if name:
            update_fields.append("name = ?")
            update_values.append(name)
        if gender:
            update_fields.append("gender = ?")
            update_values.append(gender)
        if birth_date:
            update_fields.append("birth_date = ?")
            update_values.append(birth_date)
        if department:
            update_fields.append("department = ?")
            update_values.append(department)

        if not update_fields:
            print("没有数据需要更新。")
            return

        update_fields.append("teacher_id = ?")
        update_values.append(teacher_id)

        update_query = f"UPDATE Teacher SET {', '.join(update_fields)} WHERE teacher_id = ?"
        cursor.execute(update_query, tuple(update_values))
        conn.commit()
        print("教师信息已更新！")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def get_teacher(teacher_id=None):
    try:
        if teacher_id:
            cursor.execute('''
            SELECT * FROM Teacher WHERE teacher_id = ?
            ''', (teacher_id,))
        else:
            cursor.execute('''
            SELECT * FROM Teacher
            ''')

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, 姓名: {row[1]}, 性别: {row[2]}, 出生日期: {row[3]}, 部门: {row[4]}")
        else:
            print("没有找到教师信息。")
    except Exception as e:
        print(f"Error: {e}")
def get_teachers_for_course(course_name):
    try:
        cursor.execute('''
        SELECT T.* 
        FROM Teacher T
        INNER JOIN Course C ON T.teacher_id = C.teacher_id
        WHERE C.course_name = ?
        ''', (course_name,))

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, 姓名: {row[1]}, 性别: {row[2]}, 出生日期: {row[3]}, 部门: {row[4]}")
        else:
            print(f"没有找到教授 {course_name} 的教师信息。")
    except Exception as e:
        print(f"Error: {e}")
def get_grades_by_teacher(teacher_id):
    try:
        cursor.execute('''
        SELECT G.student_id, C.course_name, G.score 
        FROM Grade G
        INNER JOIN Course C ON G.course_id = C.course_id
        WHERE G.teacher_id = ?
        ''', (teacher_id,))

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"学号: {row[0]}, 课程: {row[1]}, 分数: {row[2]}")
        else:
            print(f"没有找到教师ID为{teacher_id}的成绩信息。")
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n高校教师信息管理系统")
        print("1. 添加教师")
        print("2. 删除教师")
        print("3. 更新教师信息")
        print("4. 查询教师信息")
        print("5. 查询特定课程的教师信息")
        print("6. 查询教师的成绩信息")
        print("7. 退出")

        choice = input("请输入选项: ")

        if choice == '1':
            teacher_id = int(input("请输入教师ID: "))
            name = input("请输入教师姓名: ")
            gender = input("请输入性别 (M/F): ")
            birth_date = input("请输入出生日期 (YYYY-MM-DD): ")
            department = input("请输入部门: ")
            add_teacher(teacher_id, name, gender, birth_date, department)

        elif choice == '2':
            teacher_id = int(input("请输入要删除的教师ID: "))
            delete_teacher(teacher_id)

        elif choice == '3':
            teacher_id = int(input("请输入要更新的教师ID: "))
            print("更新教师信息（输入新值，如果不更新某项，按回车跳过）")
            name = input("新的姓名: ")
            gender = input("新的性别: ")
            birth_date = input("新的出生日期 (YYYY-MM-DD): ")
            department = input("新的部门: ")
            update_teacher(teacher_id, name or None, gender or None, birth_date or None, department or None)

        elif choice == '4':
            teacher_id = input("请输入教师ID查询，或直接回车查询所有教师: ")
            if teacher_id:
                get_teacher(int(teacher_id))
            else:
                get_teacher()

        elif choice == '5':
            course_name = input("请输入课程名称: ")
            get_teachers_for_course(course_name)

        elif choice == '6':
            teacher_id = int(input("请输入教师ID查询成绩: "))
            get_grades_by_teacher(teacher_id)

        elif choice == '7':
            print("退出程序！")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == '__main__':
    main()
