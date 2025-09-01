import mysql.connector
import xlwt

# 连接数据库
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='student'
)

# 获取游标
cursor = conn.cursor()

# 学生个人信息录入
def add_student():
    sno = input('请输入学号：')
    sname = input('请输入姓名：')
    sex = input('请输入性别：')
    birthday = input('请输入出生日期(格式：yyyy-mm-dd)：')
    hometown = input('请输入籍贯：')
    sql = f"INSERT INTO student VALUES ('{sno}', '{sname}', '{sex}', '{birthday}', '{hometown}')"
    cursor.execute(sql)
    conn.commit()
    print('添加成功！')

# 学生选课信息录入
def add_sc():
    sno = input('请输入学号：')
    cno = input('请输入课程号：')
    sc_time = input('请输入选课时间(格式：yyyy-mm-dd)：')
    sql = f"INSERT INTO sc VALUES ('{sno}', '{cno}', '{sc_time}')"
    cursor.execute(sql)
    conn.commit()
    print('添加成功！')

# 学生成绩录入
def add_score():
    sno = input('请输入学号：')
    cno = input('请输入课程号：')
    grade = input('请输入成绩：')
    sql = f"INSERT INTO score VALUES ('{sno}', '{cno}', '{grade}')"
    cursor.execute(sql)
    conn.commit()
    print('添加成功！')

# 班级学生成绩查询
def query_score():
    cno = input('请输入课程号：')
    sql = f"SELECT student.sno, sname, grade FROM student, score WHERE student.sno = score.sno AND cno = '{cno}'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('没有查询到相关数据！')
    else:
        # 将查询结果保存为Excel表格
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('Sheet1')
        sheet.write(0, 0, '学号')
        sheet.write(0, 1, '姓名')
        sheet.write(0, 2, '成绩')
        for i, row in enumerate(rows):
            sheet.write(i+1, 0, row[0])
            sheet.write(i+1, 1, row[1])
            sheet.write(i+1, 2, row[2])
        book.save('score.xls')
        print('查询成功！')

# 班级学生成绩均分+排名查询
def query_avg_rank():
    cno = input('请输入课程号：')
    sql = f"SELECT student.sno, sname, AVG(grade) AS avg_score FROM student, score WHERE student.sno = score.sno AND cno = '{cno}' GROUP BY student.sno ORDER BY avg_score DESC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('没有查询到相关数据！')
    else:
        # 将查询结果保存为Excel表格
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('Sheet1')
        sheet.write(0, 0, '排名')
        sheet.write(0, 1, '学号')
        sheet.write(0, 2, '姓名')
        sheet.write(0, 3, '平均成绩')
        for i, row in enumerate(rows):
            sheet.write(i+1, 0, i+1)
            sheet.write(i+1, 1, row[0])
            sheet.write(i+1, 2, row[1])
            sheet.write(i+1, 3, row[2])
        book.save('avg_rank.xls')
        print('查询成功！')

# 菜单
while True:
    print('1. 学生个人信息录入')
    print('2. 学生选课信息录入')
    print('3. 学生成绩录入')
    print('4. 班级学生成绩查询')
    print('5. 班级学生成绩均分+排名查询')
    print('0. 退出')
    choice = input('请输入选项：')
    if choice == '1':
        add_student()
    elif choice == '2':
        add_sc()
    elif choice == '3':
        add_score()
    elif choice == '4':
        query_score()
    elif choice == '5':
        query_avg_rank()
    elif choice == '0':
        break
    else:
        print('输入有误，请重新输入！')

# 关闭游标和连接
cursor.close()
conn.close()
