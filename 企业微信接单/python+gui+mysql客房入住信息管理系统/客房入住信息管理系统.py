import mysql.connector
from tkinter import *
from tkinter import messagebox

# 连接到MySQL数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="room"
)

# 创建游标
cursor = conn.cursor()


# 函数：添加入住信息
def add_customer():
    add_dialog = Toplevel(root)
    add_dialog.title("添加入住信息")

    customer_id_label = Label(add_dialog, text="客户ID:")
    customer_id_label.grid(row=0, column=0, padx=10, pady=10)
    customer_id_entry = Entry(add_dialog)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=10)

    room_id_label = Label(add_dialog, text="房间ID:")
    room_id_label.grid(row=1, column=0, padx=10, pady=10)
    room_id_entry = Entry(add_dialog)
    room_id_entry.grid(row=1, column=1, padx=10, pady=10)

    check_in_date_label = Label(add_dialog, text="入住日期:")
    check_in_date_label.grid(row=2, column=0, padx=10, pady=10)
    check_in_date_entry = Entry(add_dialog)
    check_in_date_entry.grid(row=2, column=1, padx=10, pady=10)

    check_out_date_label = Label(add_dialog, text="退房日期:")
    check_out_date_label.grid(row=3, column=0, padx=10, pady=10)
    check_out_date_entry = Entry(add_dialog)
    check_out_date_entry.grid(row=3, column=1, padx=10, pady=10)

    total_cost_label = Label(add_dialog, text="总费用:")
    total_cost_label.grid(row=4, column=0, padx=10, pady=10)
    total_cost_entry = Entry(add_dialog)
    total_cost_entry.grid(row=4, column=1, padx=10, pady=10)

    username_label = Label(add_dialog, text="客户姓名:")
    username_label.grid(row=5, column=0, padx=10, pady=10)
    username_entry = Entry(add_dialog)
    username_entry.grid(row=5, column=1, padx=10, pady=10)

    def add():
        customer_id = customer_id_entry.get()
        room_id = room_id_entry.get()
        check_in_date = check_in_date_entry.get()
        check_out_date = check_out_date_entry.get()
        total_cost = total_cost_entry.get()
        username = username_entry.get()

        # 插入入住信息到数据库
        sql = "INSERT INTO customer_info (customer_id, room_id, check_in_date, check_out_date, total_cost, username) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (customer_id, room_id, check_in_date, check_out_date, total_cost, username)

        try:
            cursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo('成功', '入住信息已添加')
            add_dialog.destroy()
        except Exception as e:
            conn.rollback()
            messagebox.showerror('错误', f'添加入住信息失败: {str(e)}')

    add_button = Button(add_dialog, text="添加", command=add)
    add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


# 函数：查询入住信息
# 函数：查询入住信息
def search_customer():
    search_dialog = Toplevel(root)
    search_dialog.title("查询入住信息")

    customer_id_label = Label(search_dialog, text="客户ID:")
    customer_id_label.grid(row=0, column=0, padx=10, pady=10)
    customer_id_entry = Entry(search_dialog)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=10)

    username_label = Label(search_dialog, text="客户姓名:")
    username_label.grid(row=1, column=0, padx=10, pady=10)
    username_entry = Entry(search_dialog)
    username_entry.grid(row=1, column=1, padx=10, pady=10)

    result_text = Text(search_dialog, height=10, width=50)
    result_text.grid(row=2, columnspan=2, padx=10, pady=10)

    def search():
        customer_id = customer_id_entry.get()
        username = username_entry.get()

        # 检查是否输入了客户ID或客户姓名
        if customer_id == '' and username == '':
            messagebox.showerror('错误', '请输入客户ID或客户姓名')
            return

        # 查询入住信息
        sql = "SELECT * FROM customer_info WHERE "

        if customer_id != '':
            sql += "customer_id = %s"
            values = (customer_id,)
        else:
            sql += "username = %s"
            values = (username,)

        try:
            cursor.execute(sql, values)
            results = cursor.fetchall()

            if results:
                result_text.delete(1.0, END)
                result_text.insert(END, f'共查询到{len(results)}条结果\n\n')

                for result in results:
                    result_text.insert(END, f'客户ID: {result[0]}\n')
                    result_text.insert(END, f'房间ID: {result[1]}\n')
                    result_text.insert(END, f'入住日期: {result[2]}\n')
                    result_text.insert(END, f'退房日期: {result[3]}\n')
                    result_text.insert(END, f'总费用: {result[4]}\n')
                    result_text.insert(END, f'客户姓名: {result[5]}\n')
                    result_text.insert(END, '----------------------\n')
            else:
                messagebox.showinfo('查询结果', '未找到符合条件的入住信息')

        except Exception as e:
            messagebox.showerror('错误', f'查询入住信息失败: {str(e)}')

    def search_by_username():
        username = username_entry.get()

        # 检查是否输入了客户姓名
        if username == '':
            messagebox.showerror('错误', '请输入客户姓名')
            return

        # 查询入住信息
        sql = "SELECT * FROM customer_info WHERE username = %s"

        try:
            cursor.execute(sql, (username,))
            results = cursor.fetchall()

            if results:
                result_text.delete(1.0, END)
                result_text.insert(END, f'共查询到{len(results)}条结果\n\n')

                for result in results:
                    result_text.insert(END, f'客户ID: {result[0]}\n')
                    result_text.insert(END, f'房间ID: {result[1]}\n')
                    result_text.insert(END, f'入住日期: {result[2]}\n')
                    result_text.insert(END, f'退房日期: {result[3]}\n')
                    result_text.insert(END, f'总费用: {result[4]}\n')
                    result_text.insert(END, f'客户姓名: {result[5]}\n')
                    result_text.insert(END, '----------------------\n')
            else:
                messagebox.showinfo('查询结果', '未找到符合条件的入住信息')

        except Exception as e:
            messagebox.showerror('错误', f'查询入住信息失败: {str(e)}')

    search_button = Button(search_dialog, text="查询", command=search)
    search_button.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")





# 函数：更新入住信息
def update_customer():
    update_dialog = Toplevel(root)
    update_dialog.title("更新入住信息")

    customer_id_label = Label(update_dialog, text="客户ID:")
    customer_id_label.grid(row=0, column=0, padx=10, pady=10)
    customer_id_entry = Entry(update_dialog)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=10)

    room_id_label = Label(update_dialog, text="房间ID:")
    room_id_label.grid(row=1, column=0, padx=10, pady=10)
    room_id_entry = Entry(update_dialog)
    room_id_entry.grid(row=1, column=1, padx=10, pady=10)

    check_in_date_label = Label(update_dialog, text="入住日期:")
    check_in_date_label.grid(row=2, column=0, padx=10, pady=10)
    check_in_date_entry = Entry(update_dialog)
    check_in_date_entry.grid(row=2, column=1, padx=10, pady=10)

    check_out_date_label = Label(update_dialog, text="退房日期:")
    check_out_date_label.grid(row=3, column=0, padx=10, pady=10)
    check_out_date_entry = Entry(update_dialog)
    check_out_date_entry.grid(row=3, column=1, padx=10, pady=10)

    total_cost_label = Label(update_dialog, text="总费用:")
    total_cost_label.grid(row=4, column=0, padx=10, pady=10)
    total_cost_entry = Entry(update_dialog)
    total_cost_entry.grid(row=4, column=1, padx=10, pady=10)

    username_label = Label(update_dialog, text="客户姓名:")
    username_label.grid(row=5, column=0, padx=10, pady=10)
    username_entry = Entry(update_dialog)
    username_entry.grid(row=5, column=1, padx=10, pady=10)

    def update():
        customer_id = customer_id_entry.get()
        room_id = room_id_entry.get()
        check_in_date = check_in_date_entry.get()
        check_out_date = check_out_date_entry.get()
        total_cost = total_cost_entry.get()
        username = username_entry.get()

        # 检查是否输入了所有字段
        if customer_id == '' or room_id == '' or check_in_date == '' or username == '':
            messagebox.showerror('错误', '请填写所有字段')
            return

        # 更新入住信息
        sql = "UPDATE customer_info SET room_id = %s, check_in_date = %s, check_out_date = %s, total_cost = %s, " \
              "username = %s WHERE customer_id = %s"
        values = (room_id, check_in_date, check_out_date, total_cost, username, customer_id)

        try:
            cursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo('成功', '入住信息已更新')
            update_dialog.destroy()
        except Exception as e:
            conn.rollback()
            messagebox.showerror('错误', f'更新入住信息失败: {str(e)}')

    update_button = Button(update_dialog, text="更新", command=update)
    update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


# 函数：删除入住信息
def delete_customer():
    delete_dialog = Toplevel(root)
    delete_dialog.title("删除入住信息")

    customer_id_label = Label(delete_dialog, text="客户ID:")
    customer_id_label.grid(row=0, column=0, padx=10, pady=10)
    customer_id_entry = Entry(delete_dialog)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=10)

    def delete():
        customer_id = customer_id_entry.get()

        # 检查是否输入了客户ID
        if customer_id == '':
            messagebox.showerror('错误', '请输入客户ID')
            return

        # 删除入住信息
        sql = "DELETE FROM customer_info WHERE customer_id = %s"
        values = (customer_id,)

        try:
            cursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo('成功', '入住信息已删除')
            delete_dialog.destroy()
        except Exception as e:
            conn.rollback()
            messagebox.showerror('错误', f'删除入住信息失败: {str(e)}')

    delete_button = Button(delete_dialog, text="删除", command=delete)
    delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# 函数：查询空房间
def search_vacant_rooms():
    search_dialog = Toplevel(root)
    search_dialog.title("查询空房间")

    result_text = Text(search_dialog, height=10, width=50)
    result_text.grid(row=0, padx=10, pady=10)

    # 查询空房间
    sql = "SELECT room_id FROM room_info WHERE room_id NOT IN (SELECT room_id FROM customer_info)"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            result_text.insert(END, f'共查询到{len(results)}个空房间\n\n')

            for result in results:
                result_text.insert(END, f'房间ID: {result[0]}\n')
                result_text.insert(END, '----------------------\n')
        else:
            messagebox.showinfo('查询结果', '未找到空房间')

    except Exception as e:
        messagebox.showerror('错误', f'查询空房间失败: {str(e)}')


# 函数：按照时间范围查询入住信息
def search_customer_by_date():
    search_dialog = Toplevel(root)
    search_dialog.title("按照时间查询入住信息")

    start_date_label = Label(search_dialog, text="起始日期:")
    start_date_label.grid(row=0, column=0, padx=10, pady=10)
    start_date_entry = Entry(search_dialog)
    start_date_entry.grid(row=0, column=1, padx=10, pady=10)

    end_date_label = Label(search_dialog, text="终止日期:")
    end_date_label.grid(row=1, column=0, padx=10, pady=10)
    end_date_entry = Entry(search_dialog)
    end_date_entry.grid(row=1, column=1, padx=10, pady=10)

    result_text = Text(search_dialog, height=10, width=50)
    result_text.grid(row=2, columnspan=2, padx=10, pady=10)

    def search():
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        # 查询入住信息
        sql = "SELECT * FROM customer_info WHERE check_in_date >= %s"
        values = [start_date]

        if end_date:
            sql += " AND check_in_date <= %s"
            values.append(end_date)

        try:
            cursor.execute(sql, values)
            results = cursor.fetchall()

            if results:
                result_text.delete(1.0, END)
                result_text.insert(END, f'共查询到{len(results)}条结果\n\n')

                for result in results:
                    result_text.insert(END, f'客户ID: {result[0]}\n')
                    result_text.insert(END, f'房间ID: {result[1]}\n')
                    result_text.insert(END, f'入住日期: {result[2]}\n')
                    result_text.insert(END, f'退房日期: {result[3]}\n')
                    result_text.insert(END, f'总费用: {result[4]}\n')
                    result_text.insert(END, f'客户姓名: {result[5]}\n')
                    result_text.insert(END, '----------------------\n')
            else:
                messagebox.showinfo('查询结果', '未找到符合条件的入住信息')

        except Exception as e:
            messagebox.showerror('错误', f'查询入住信息失败: {str(e)}')

    search_button = Button(search_dialog, text="查询", command=search)
    search_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# 创建GUI窗口
root = Tk()
root.title('客房入住信息管理系统')

# 菜单栏
menu = Menu(root)
root.config(menu=menu)

# 菜单：入住信息管理
customer_menu = Menu(menu)
menu.add_cascade(label='入住信息管理', menu=customer_menu)
customer_menu.add_command(label='添加', command=add_customer)
customer_menu.add_command(label='查询', command=search_customer)
customer_menu.add_command(label='更新', command=update_customer)
customer_menu.add_command(label='删除', command=delete_customer)

# 菜单：查询空房间
vacant_rooms_menu = Menu(menu)
menu.add_cascade(label='查询空房间', menu=vacant_rooms_menu)
vacant_rooms_menu.add_command(label='查询', command=search_vacant_rooms)

# 菜单：按照时间查询入住信息
date_menu = Menu(menu)
menu.add_cascade(label='按照时间查询入住信息', menu=date_menu)
date_menu.add_command(label='查询', command=search_customer_by_date)

# 查询结果文本框
result_text = Text(root, height=10, width=50)
result_text.grid(row=0, columnspan=2, padx=10, pady=10)

root.mainloop()

# 关闭数据库连接
cursor.close()
conn.close()
