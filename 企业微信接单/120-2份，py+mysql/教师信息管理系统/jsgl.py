# -*- coding: utf-8 -*-

import pymysql

# 连接数据库
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",  # 替换为你的数据库密码
        database="TeacherManagementSystem",
        charset="utf8mb4"
    )

# 菜单显示
def show_menu():
    print("\n欢迎使用教师信息管理系统")
    print("1. 增加教师信息")
    print("2. 修改教师信息")
    print("3. 删除教师信息")
    print("4. 查询教师信息")
    print("5. 增加课程信息")
    print("6. 查询课程信息")
    print("7. 增加部门信息")
    print("8. 查询部门信息")
    print("9. 退出")

# 增加教师信息
def add_teacher():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n增加教师信息")
    name = input("请输入教师姓名: ")
    gender = input("请输入教师性别 (Male/Female): ")
    dob = input("请输入出生日期 (格式: YYYY-MM-DD): ")
    department_id = input("请输入所属部门ID (可以为空，按Enter跳过): ") or None
    email = input("请输入教师邮箱: ")
    phone = input("请输入联系电话: ")
    hire_date = input("请输入入职日期 (格式: YYYY-MM-DD): ")

    sql = """
    INSERT INTO Teachers (TeacherName, Gender, DateOfBirth, DepartmentID, Email, PhoneNumber, HireDate)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (name, gender, dob, department_id, email, phone, hire_date))
    conn.commit()
    print("教师信息添加成功！")

    cursor.close()
    conn.close()

# 修改教师信息
def update_teacher():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n修改教师信息")
    teacher_id = input("请输入要修改的教师ID: ")
    print("请输入需要修改的内容 (按Enter跳过，不修改):")
    name = input("教师姓名: ")
    gender = input("性别 (Male/Female): ")
    dob = input("出生日期 (格式: YYYY-MM-DD): ")
    department_id = input("所属部门ID (可以为空): ") or None
    email = input("教师邮箱: ")
    phone = input("联系电话: ")
    hire_date = input("入职日期 (格式: YYYY-MM-DD): ")

    sql = "UPDATE Teachers SET "
    fields = []
    values = []

    if name:
        fields.append("TeacherName = %s")
        values.append(name)
    if gender:
        fields.append("Gender = %s")
        values.append(gender)
    if dob:
        fields.append("DateOfBirth = %s")
        values.append(dob)
    if department_id:
        fields.append("DepartmentID = %s")
        values.append(department_id)
    if email:
        fields.append("Email = %s")
        values.append(email)
    if phone:
        fields.append("PhoneNumber = %s")
        values.append(phone)
    if hire_date:
        fields.append("HireDate = %s")
        values.append(hire_date)

    if fields:
        sql += ", ".join(fields) + " WHERE TeacherID = %s"
        values.append(teacher_id)
        cursor.execute(sql, values)
        conn.commit()
        print("教师信息修改成功！")
    else:
        print("未修改任何信息！")

    cursor.close()
    conn.close()

# 删除教师信息
def delete_teacher():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n删除教师信息")
    teacher_id = input("请输入要删除的教师ID: ")

    sql = "DELETE FROM Teachers WHERE TeacherID = %s"
    cursor.execute(sql, (teacher_id,))
    conn.commit()
    print("教师信息删除成功！")

    cursor.close()
    conn.close()

# 查询教师信息
def query_teacher():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n查询教师信息")
    teacher_id = input("请输入要查询的教师ID (按Enter查询所有教师): ")

    if teacher_id:
        sql = "SELECT * FROM Teachers WHERE TeacherID = %s"
        cursor.execute(sql, (teacher_id,))
    else:
        sql = "SELECT * FROM Teachers"
        cursor.execute(sql)

    results = cursor.fetchall()
    if results:
        print("教师信息如下:")
        for row in results:
            print(row)
    else:
        print("未找到教师信息！")

    cursor.close()
    conn.close()

# 增加课程信息
def add_course():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n增加课程信息")
    name = input("请输入课程名称: ")
    credit_hours = input("请输入学分: ")
    teacher_id = input("请输入授课教师ID (可以为空): ") or None
    department_id = input("请输入所属部门ID (可以为空): ") or None
    semester = input("请输入学期信息: ")

    sql = """
    INSERT INTO Courses (CourseName, CreditHours, TeacherID, DepartmentID, Semester)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (name, credit_hours, teacher_id, department_id, semester))
    conn.commit()
    print("课程信息添加成功！")

    cursor.close()
    conn.close()

# 查询课程信息
def query_course():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n查询课程信息")
    course_id = input("请输入要查询的课程ID (按Enter查询所有课程): ")

    if course_id:
        sql = "SELECT * FROM Courses WHERE CourseID = %s"
        cursor.execute(sql, (course_id,))
    else:
        sql = "SELECT * FROM Courses"
        cursor.execute(sql)

    results = cursor.fetchall()
    if results:
        print("课程信息如下:")
        for row in results:
            print(row)
    else:
        print("未找到课程信息！")

    cursor.close()
    conn.close()

# 增加部门信息
def add_department():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n增加部门信息")
    name = input("请输入部门名称: ")
    head = input("请输入部门负责人姓名: ")
    year = input("请输入部门成立年份 (格式: YYYY): ")

    sql = """
    INSERT INTO Departments (DepartmentName, DepartmentHead, EstablishedYear)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (name, head, year))
    conn.commit()
    print("部门信息添加成功！")

    cursor.close()
    conn.close()

# 查询部门信息
def query_department():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n查询部门信息")
    department_id = input("请输入要查询的部门ID (按Enter查询所有部门): ")

    if department_id:
        sql = "SELECT * FROM Departments WHERE DepartmentID = %s"
        cursor.execute(sql, (department_id,))
    else:
        sql = "SELECT * FROM Departments"
        cursor.execute(sql)

    results = cursor.fetchall()
    if results:
        print("部门信息如下:")
        for row in results:
            print(row)
    else:
        print("未找到部门信息！")

    cursor.close()
    conn.close()

# 主程序
def main():
    while True:
        show_menu()
        choice = input("请选择操作: ")
        if choice == "1":
            add_teacher()
        elif choice == "2":
            update_teacher()
        elif choice == "3":
            delete_teacher()
        elif choice == "4":
            query_teacher()
        elif choice == "5":
            add_course()
        elif choice == "6":
            query_course()
        elif choice == "7":
            add_department()
        elif choice == "8":
            query_department()
        elif choice == "9":
            print("感谢使用教师信息管理系统！")
            break
        else:
            print("无效的选项，请重新选择！")

if __name__ == "__main__":
    main()
