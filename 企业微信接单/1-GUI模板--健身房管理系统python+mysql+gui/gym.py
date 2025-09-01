import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# 连接MySQL数据库
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Gym_management"
)

# 创建主窗口
root = tk.Tk()
root.title("Gym Management System")
root.geometry("400x300")

# 创建ttk样式和主题
style = ttk.Style()
style.theme_use("clam")

# 设置控件的颜色
style.configure("TLabel", background="#f0f0f0")
style.configure("TEntry", fieldbackground="#ffffff")
style.configure("TButton", background="#4caf50", foreground="white")

# 设置控件的间距
style.layout("TButton", [("Button.padding", {"sticky": "nswe", "children":
    [("Button.label", {"sticky": "nswe"})]})])

# 创建标签和输入框
label_username = ttk.Label(root, text="Username:")
entry_username = ttk.Entry(root)

label_password = ttk.Label(root, text="Password:")
entry_password = ttk.Entry(root, show="*")

label_username.pack(pady=10)
entry_username.pack(pady=5)
label_password.pack()
entry_password.pack()

# 创建角色选择单选按钮
selected_role = tk.StringVar()

role_frame = ttk.Frame(root)
role_frame.pack(pady=10)

label_role = ttk.Label(role_frame, text="Select Role:")
label_role.pack()

button_member = ttk.Radiobutton(role_frame, text="会员", variable=selected_role, value="member")
button_member.pack()

button_staff = ttk.Radiobutton(role_frame, text="员工", variable=selected_role, value="staff")
button_staff.pack()

button_coach = ttk.Radiobutton(role_frame, text="教练", variable=selected_role, value="coach")
button_coach.pack()


def login():
    username = entry_username.get()
    password = entry_password.get()
    role = selected_role.get()

    if role == "member":
        show_member_menu(username, password)
    elif role == "staff":
        show_staff_menu(username, password)
    elif role == "coach":
        show_coach_menu(username, password)
    else:
        messagebox.showerror("Error", "Please select a role")


def show_staff_menu(username, password):
    # 创建工作人员菜单窗口
    staff_menu = tk.Toplevel(root)
    staff_menu.title("员工菜单")
    staff_menu.geometry("400x300")

    # 工作人员登录验证
    cursor = db.cursor()
    query = "SELECT * FROM gym WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if not result:
        messagebox.showerror("Error", "Invalid username or password")
        staff_menu.destroy()
        return

    gym_id = result[0]

    def manage_coaches():
        # 创建教练管理窗口
        coach_management = tk.Toplevel(staff_menu)
        coach_management.title("教练管理")
        coach_management.geometry("400x300")

        def add_coach():
            # 创建添加教练窗口
            add_coach_window = tk.Toplevel(coach_management)
            add_coach_window.title("增加教练")
            add_coach_window.geometry("300x400")

            label_username = tk.Label(add_coach_window, text="Username:")
            entry_username = tk.Entry(add_coach_window)
            label_password = tk.Label(add_coach_window, text="Password:")
            entry_password = tk.Entry(add_coach_window, show="*")
            label_name = tk.Label(add_coach_window, text="Name:")
            entry_name = tk.Entry(add_coach_window)
            label_phone = tk.Label(add_coach_window, text="Phone:")
            entry_phone = tk.Entry(add_coach_window)
            label_gender = tk.Label(add_coach_window, text="Gender:")
            entry_gender = tk.Entry(add_coach_window)
            label_birthdate = tk.Label(add_coach_window, text="Birthdate (YYYY-MM-DD):")
            entry_birthdate = tk.Entry(add_coach_window)
            label_coach_type = tk.Label(add_coach_window, text="Coach Type:")
            entry_coach_type = tk.Entry(add_coach_window)

            label_username.pack()
            entry_username.pack()
            label_password.pack()
            entry_password.pack()
            label_name.pack()
            entry_name.pack()
            label_phone.pack()
            entry_phone.pack()
            label_gender.pack()
            entry_gender.pack()
            label_birthdate.pack()
            entry_birthdate.pack()
            label_coach_type.pack()
            entry_coach_type.pack()

            def save_coach():
                username = entry_username.get()
                password = entry_password.get()
                name = entry_name.get()
                phone = entry_phone.get()
                gender = entry_gender.get()
                birthdate = entry_birthdate.get()
                coach_type = entry_coach_type.get()

                if username and password and name and phone and gender and birthdate and coach_type:
                    cursor = db.cursor()
                    query = "INSERT INTO coach (username, password, phone, gender, birthdate, coach_type, gym_id) " \
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (username, password, phone, gender, birthdate, coach_type, gym_id)
                    cursor.execute(query, values)
                    db.commit()

                    messagebox.showinfo("Success", "Coach added successfully")
                    add_coach_window.destroy()
                else:
                    messagebox.showerror("Error", "Please fill in all fields")

            button_save = tk.Button(add_coach_window, text="Save", command=save_coach)
            button_save.pack()

        def view_coaches():
            # 创建查看教练窗口
            view_coaches_window = tk.Toplevel(coach_management)
            view_coaches_window.title("查看教练")
            view_coaches_window.geometry("600x400")

            cursor = db.cursor()
            query = "SELECT * FROM coach WHERE gym_id = %s"
            cursor.execute(query, (gym_id,))
            coaches = cursor.fetchall()

            # 创建Treeview
            tree = ttk.Treeview(view_coaches_window,
                                columns=(
                                    "Coach ID", "Username", "Name", "Phone", "Gender", "Birthdate", "Coach Type"),
                                show="headings")
            tree.heading("Coach ID", text="Coach ID")
            tree.heading("Username", text="Username")
            tree.heading("Name", text="Name")
            tree.heading("Phone", text="Phone")
            tree.heading("Gender", text="Gender")
            tree.heading("Birthdate", text="Birthdate")
            tree.heading("Coach Type", text="Coach Type")

            tree.column("Coach ID", width=80)
            tree.column("Username", width=100)
            tree.column("Name", width=100)
            tree.column("Phone", width=100)
            tree.column("Gender", width=80)
            tree.column("Birthdate", width=100)
            tree.column("Coach Type", width=100)

            tree.pack(fill="both", expand=True)

            for coach in coaches:
                tree.insert("", tk.END, values=coach)

            cursor.close()

        button_add_coach = tk.Button(coach_management, text="添加教练", command=add_coach)
        button_view_coaches = tk.Button(coach_management, text="查看教练", command=view_coaches)

        button_add_coach.pack()
        button_view_coaches.pack()

    button_manage_coaches = tk.Button(staff_menu, text="教练管理", command=manage_coaches)
    button_manage_coaches.pack()

    def manage_members():
        # 创建会员管理窗口
        member_management = tk.Toplevel(staff_menu)
        member_management.title("会员管理")
        member_management.geometry("400x300")

        def add_member():
            # 创建添加会员窗口
            add_member_window = tk.Toplevel(member_management)
            add_member_window.title("添加会员")
            add_member_window.geometry("300x350")

            label_username = tk.Label(add_member_window, text="Username:")
            entry_username = tk.Entry(add_member_window)
            label_password = tk.Label(add_member_window, text="Password:")
            entry_password = tk.Entry(add_member_window, show="*")
            label_phone = tk.Label(add_member_window, text="Phone:")
            entry_phone = tk.Entry(add_member_window)
            label_gender = tk.Label(add_member_window, text="Gender:")
            entry_gender = tk.Entry(add_member_window)
            label_birthdate = tk.Label(add_member_window, text="Birthdate:")
            entry_birthdate = tk.Entry(add_member_window)
            label_member_type = tk.Label(add_member_window, text="Member Type:")
            entry_member_type = tk.Entry(add_member_window)

            label_username.pack()
            entry_username.pack()
            label_password.pack()
            entry_password.pack()
            label_phone.pack()
            entry_phone.pack()
            label_gender.pack()
            entry_gender.pack()
            label_birthdate.pack()
            entry_birthdate.pack()
            label_member_type.pack()
            entry_member_type.pack()

            def save_member():
                username = entry_username.get()
                password = entry_password.get()
                phone = entry_phone.get()
                gender = entry_gender.get()
                birthdate = entry_birthdate.get()
                member_type = entry_member_type.get()

                if username and password and phone and gender and birthdate and member_type:
                    cursor = db.cursor()
                    query = "INSERT INTO member (username, password, phone, gender, birthdate, member_type) " \
                            "VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (username, password, phone, gender, birthdate, member_type)
                    cursor.execute(query, values)
                    db.commit()

                    messagebox.showinfo("Success", "Member added successfully")
                    add_member_window.destroy()
                else:
                    messagebox.showerror("Error", "Please fill in all fields")

            button_save = tk.Button(add_member_window, text="Save", command=save_member)
            button_save.pack()

        def view_members():
            # 创建查看会员窗口
            view_members_window = tk.Toplevel(member_management)
            view_members_window.title("查看会员")
            view_members_window.geometry("600x400")

            cursor = db.cursor()
            query = "SELECT m.* " \
                    "FROM member m " \
                    "JOIN course_purchase cp ON m.member_id = cp.member_id " \
                    "JOIN course c ON cp.course_id = c.course_id " \
                    "JOIN coach co ON c.coach_id = co.coach_id " \
                    "JOIN gym g ON co.gym_id = g.gym_id " \
                    "WHERE g.gym_id = %s"
            cursor.execute(query, (gym_id,))
            members = cursor.fetchall()

            # 创建Treeview
            tree = ttk.Treeview(view_members_window,
                                columns=(
                                    "Member ID", "Username", "Password", "Phone", "Gender", "Birthdate", "Member Type"),
                                show="headings")
            tree.heading("Member ID", text="Member ID")
            tree.heading("Username", text="Username")
            tree.heading("Password", text="Password")
            tree.heading("Phone", text="Phone")
            tree.heading("Gender", text="Gender")
            tree.heading("Birthdate", text="Birthdate")
            tree.heading("Member Type", text="Member Type")

            tree.column("Member ID", width=80)
            tree.column("Username", width=100)
            tree.column("Password", width=100)
            tree.column("Phone", width=100)
            tree.column("Gender", width=80)
            tree.column("Birthdate", width=100)
            tree.column("Member Type", width=100)

            tree.pack(fill="both", expand=True)

            for member in members:
                tree.insert("", tk.END, values=member)

            cursor.close()

        button_add_member = tk.Button(member_management, text="增加会员", command=add_member)
        button_view_members = tk.Button(member_management, text="查看会员", command=view_members)

        button_add_member.pack()
        button_view_members.pack()

    def manage_courses():
        # 创建课程管理窗口
        course_management = tk.Toplevel(staff_menu)
        course_management.title("课程管理")
        course_management.geometry("400x300")

        def add_course():
            # 创建添加课程窗口
            add_course_window = tk.Toplevel(course_management)
            add_course_window.title("Add Course")
            add_course_window.geometry("300x400")

            label_course_id = tk.Label(add_course_window, text="Course ID:")
            entry_course_id = tk.Entry(add_course_window)
            label_name = tk.Label(add_course_window, text="Name:")
            entry_name = tk.Entry(add_course_window)
            label_description = tk.Label(add_course_window, text="Description:")
            entry_description = tk.Entry(add_course_window)
            label_price = tk.Label(add_course_window, text="Price:")
            entry_price = tk.Entry(add_course_window)
            label_max_capacity = tk.Label(add_course_window, text="Max Capacity:")
            entry_max_capacity = tk.Entry(add_course_window)
            label_coach_id = tk.Label(add_course_window, text="Coach ID:")
            entry_coach_id = tk.Entry(add_course_window)

            label_course_id.pack()
            entry_course_id.pack()
            label_name.pack()
            entry_name.pack()
            label_description.pack()
            entry_description.pack()
            label_price.pack()
            entry_price.pack()
            label_max_capacity.pack()
            entry_max_capacity.pack()
            label_coach_id.pack()
            entry_coach_id.pack()

            def save_course():
                course_id = int(entry_course_id.get())
                name = entry_name.get()
                description = entry_description.get()
                price = float(entry_price.get())
                max_capacity = int(entry_max_capacity.get())
                coach_id = int(entry_coach_id.get())

                if course_id and name and description and price and max_capacity and coach_id:
                    cursor = db.cursor()
                    query = "INSERT INTO course (course_id, name, description, price, max_capacity, coach_id, gym_id) " \
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (course_id, name, description, price, max_capacity, coach_id, gym_id)
                    cursor.execute(query, values)
                    db.commit()

                    messagebox.showinfo("Success", "Course added successfully")
                    add_course_window.destroy()
                else:
                    messagebox.showerror("Error", "Please fill in all fields")

            button_save = tk.Button(add_course_window, text="Save", command=save_course)
            button_save.pack()

        def view_courses():
            # 创建查看课程窗口
            view_courses_window = tk.Toplevel(course_management)
            view_courses_window.title("View Courses")
            view_courses_window.geometry("400x300")

            cursor = db.cursor()
            query = "SELECT * FROM course WHERE gym_id = %s"
            cursor.execute(query, (gym_id,))
            courses = cursor.fetchall()

            # 创建Treeview
            tree = ttk.Treeview(view_courses_window,
                                columns=("Course ID", "Name", "Description", "Price", "Max Capacity", "Coach ID"),
                                show="headings")
            tree.heading("Course ID", text="Course ID")
            tree.heading("Name", text="Name")
            tree.heading("Description", text="Description")
            tree.heading("Price", text="Price")
            tree.heading("Max Capacity", text="Max Capacity")
            tree.heading("Coach ID", text="Coach ID")

            tree.column("Course ID", width=80)
            tree.column("Name", width=100)
            tree.column("Description", width=150)
            tree.column("Price", width=80)
            tree.column("Max Capacity", width=100)
            tree.column("Coach ID", width=80)

            tree.pack(fill="both", expand=True)

            for course in courses:
                tree.insert("", tk.END, values=course)

            cursor.close()

        button_add_course = tk.Button(course_management, text="添加课程", command=add_course)
        button_view_courses = tk.Button(course_management, text="查看课程", command=view_courses)

        button_add_course.pack()
        button_view_courses.pack()

    def manage_orders():
        # 创建订单管理窗口
        order_management = tk.Toplevel(staff_menu)
        order_management.title("订单管理")
        order_management.geometry("400x300")

        def view_orders():
            # 创建查看订单窗口
            view_orders_window = tk.Toplevel(order_management)
            view_orders_window.title("查看订单")
            view_orders_window.geometry("600x400")

            cursor = db.cursor()
            query = "SELECT cp.purchase_id, cp.member_id, cp.course_id, cp.purchase_date, cp.price, m.username, c.name AS course_name, co.username AS coach_username " \
                    "FROM course_purchase cp " \
                    "JOIN member m ON cp.member_id = m.member_id " \
                    "JOIN course c ON cp.course_id = c.course_id " \
                    "JOIN coach co ON c.coach_id = co.coach_id " \
                    "JOIN gym g ON co.gym_id = g.gym_id " \
                    "WHERE g.gym_id = %s"

            cursor.execute(query, (gym_id,))
            orders = cursor.fetchall()

            # 创建Treeview
            tree = ttk.Treeview(view_orders_window,
                                columns=("Order ID", "Member ID", "Course ID", "Purchase Date", "Price", "Username",
                                         "Course Name", "Coach Username", ""),
                                show="headings")
            tree.heading("Order ID", text="Order ID")
            tree.heading("Member ID", text="Member ID")
            tree.heading("Course ID", text="Course ID")
            tree.heading("Purchase Date", text="Purchase Date")
            tree.heading("Price", text="Price")
            tree.heading("Username", text="Username")
            tree.heading("Course Name", text="Course Name")
            tree.heading("Coach Username", text="Coach Username")
            tree.heading("", text="")

            tree.column("Order ID", width=80)
            tree.column("Member ID", width=80)
            tree.column("Course ID", width=80)
            tree.column("Purchase Date", width=120)
            tree.column("Price", width=80)
            tree.column("Username", width=100)
            tree.column("Course Name", width=150)
            tree.column("Coach Username", width=100)
            tree.column("", width=80)

            tree.pack(fill="both", expand=True)

            for order in orders:
                tree.insert("", tk.END, values=order + ("",))

            def delete_order(order_id):
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this order?"):
                    cursor = db.cursor()
                    query = "DELETE FROM course_purchase WHERE purchase_id = %s"
                    cursor.execute(query, (order_id,))
                    db.commit()
                    messagebox.showinfo("Success", "Order deleted successfully")
                    view_orders()

            def delete_selected_order():
                selected_item = tree.focus()
                if selected_item:
                    item_values = tree.item(selected_item)["values"]
                    order_id = item_values[0]
                    delete_order(order_id)
                else:
                    messagebox.showerror("Error", "Please select an order")

            button_delete = tk.Button(view_orders_window, text="Delete", command=delete_selected_order)
            button_delete.pack()

        button_view_orders = tk.Button(order_management, text="查看订单", command=view_orders)
        button_view_orders.pack()

    button_manage_members = tk.Button(staff_menu, text="会员管理", command=manage_members)
    button_manage_courses = tk.Button(staff_menu, text="课程管理", command=manage_courses)
    button_manage_orders = tk.Button(staff_menu, text="订单管理", command=manage_orders)

    button_manage_members.pack()
    button_manage_courses.pack()
    button_manage_orders.pack()


def show_coach_menu(username, password):
    # 创建教练菜单窗口
    coach_menu = tk.Toplevel(root)
    coach_menu.title("教练菜单")
    coach_menu.geometry("400x300")

    # 教练登录验证
    cursor = db.cursor()
    query = "SELECT * FROM coach WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if not result:
        messagebox.showerror("Error", "Invalid username or password")
        coach_menu.destroy()
        return
    coach_id = result[0]
    gym_id = result[7]

    def publish_course():
        # 创建发布课程窗口
        publish_course_window = tk.Toplevel(coach_menu)
        publish_course_window.title("发布课程")
        publish_course_window.geometry("300x300")

        label_course_id = tk.Label(publish_course_window, text="Course ID:")
        entry_course_id = tk.Entry(publish_course_window)
        label_name = tk.Label(publish_course_window, text="Name:")
        entry_name = tk.Entry(publish_course_window)
        label_description = tk.Label(publish_course_window, text="Description:")
        entry_description = tk.Entry(publish_course_window)
        label_price = tk.Label(publish_course_window, text="Price:")
        entry_price = tk.Entry(publish_course_window)
        label_max_capacity = tk.Label(publish_course_window, text="Max Capacity:")
        entry_max_capacity = tk.Entry(publish_course_window)

        label_course_id.pack()
        entry_course_id.pack()
        label_name.pack()
        entry_name.pack()
        label_description.pack()
        entry_description.pack()
        label_price.pack()
        entry_price.pack()
        label_max_capacity.pack()
        entry_max_capacity.pack()

        def save_course():
            course_id = int(entry_course_id.get())
            name = entry_name.get()
            description = entry_description.get()
            price = float(entry_price.get())
            max_capacity = int(entry_max_capacity.get())

            if course_id and name and description and price and max_capacity:
                cursor = db.cursor()
                query = "INSERT INTO course (course_id, name, description, price, max_capacity, coach_id, gym_id) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (course_id, name, description, price, max_capacity, result[0], gym_id)
                cursor.execute(query, values)
                db.commit()

                messagebox.showinfo("Success", "Course published successfully")
                publish_course_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields")

        button_save = tk.Button(publish_course_window, text="Save", command=save_course)
        button_save.pack()

    def modify_course():
        # 创建修改课程窗口
        modify_course_window = tk.Toplevel(coach_menu)
        modify_course_window.title("修改课程")
        modify_course_window.geometry("300x300")

        label_course_id = tk.Label(modify_course_window, text="Course ID:")
        entry_course_id = tk.Entry(modify_course_window)
        label_name = tk.Label(modify_course_window, text="Name:")
        entry_name = tk.Entry(modify_course_window)
        label_description = tk.Label(modify_course_window, text="Description:")
        entry_description = tk.Entry(modify_course_window)
        label_price = tk.Label(modify_course_window, text="Price:")
        entry_price = tk.Entry(modify_course_window)
        label_max_capacity = tk.Label(modify_course_window, text="Max Capacity:")
        entry_max_capacity = tk.Entry(modify_course_window)

        label_course_id.pack()
        entry_course_id.pack()
        label_name.pack()
        entry_name.pack()
        label_description.pack()
        entry_description.pack()
        label_price.pack()
        entry_price.pack()
        label_max_capacity.pack()
        entry_max_capacity.pack()

        def save_course():
            course_id = int(entry_course_id.get())
            name = entry_name.get()
            description = entry_description.get()
            price = float(entry_price.get())
            max_capacity = int(entry_max_capacity.get())

            if course_id and name and description and price and max_capacity:
                cursor = db.cursor()
                query = "UPDATE course SET name = %s, description = %s, price = %s, max_capacity = %s " \
                        "WHERE course_id = %s AND gym_id = %s AND coach_id = %s"
                values = (name, description, price, max_capacity, course_id, gym_id, result[0])
                cursor.execute(query, values)
                db.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Course modified successfully")
                else:
                    messagebox.showerror("Error", "Course not found or you are not the coach of the course")

                modify_course_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields")

        button_save = tk.Button(modify_course_window, text="Save", command=save_course)
        button_save.pack()

    def view_students():
        # 创建查看学员窗口
        view_students_window = tk.Toplevel(coach_menu)
        view_students_window.title("View Students")
        view_students_window.geometry("500x400")

        cursor = db.cursor()
        query = "SELECT c.course_id, c.name AS course_name, c.description, c.price, c.max_capacity, m.member_id, m.username, m.phone, m.gender, m.birthdate, m.member_type " \
                "FROM course c " \
                "JOIN course_purchase cp ON c.course_id = cp.course_id " \
                "JOIN member m ON cp.member_id = m.member_id " \
                "WHERE c.coach_id = %s"

        cursor.execute(query, (coach_id,))

        students = cursor.fetchall()

        # 创建Treeview
        tree = ttk.Treeview(view_students_window,
                            columns=("Course ID", "Course Name", "Course Description", "Course Price", "Max Capacity",
                                     "Member ID", "Username", "Phone", "Gender", "Birthdate", "Member Type"),
                            show="headings")
        tree.heading("Course ID", text="Course ID")
        tree.heading("Course Name", text="Course Name")
        tree.heading("Course Description", text="Course Description")
        tree.heading("Course Price", text="Course Price")
        tree.heading("Max Capacity", text="Max Capacity")
        tree.heading("Member ID", text="Member ID")
        tree.heading("Username", text="Username")
        tree.heading("Phone", text="Phone")
        tree.heading("Gender", text="Gender")
        tree.heading("Birthdate", text="Birthdate")
        tree.heading("Member Type", text="Member Type")

        tree.column("Course ID", width=80)
        tree.column("Course Name", width=100)
        tree.column("Course Description", width=150)
        tree.column("Course Price", width=80)
        tree.column("Max Capacity", width=100)
        tree.column("Member ID", width=80)
        tree.column("Username", width=100)
        tree.column("Phone", width=100)
        tree.column("Gender", width=80)
        tree.column("Birthdate", width=100)
        tree.column("Member Type", width=100)

        tree.pack(fill="both", expand=True)

        for student in students:
            course_id, course_name, description, price, max_capacity, member_id, username, phone, gender, birthdate, member_type = student
            tree.insert("", tk.END, values=(
                course_id, course_name, description, price, max_capacity, member_id, username, phone, gender, birthdate,
                member_type))

        cursor.close()

    button_publish_course = tk.Button(coach_menu, text="发布课程", command=publish_course)
    button_modify_course = tk.Button(coach_menu, text="修改课程", command=modify_course)
    button_view_students = tk.Button(coach_menu, text="查看学员", command=view_students)

    button_publish_course.pack()
    button_modify_course.pack()
    button_view_students.pack()

def show_member_menu(username, password):
    # 会员登录验证
    cursor = db.cursor()
    query = "SELECT * FROM member WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if not result:
        messagebox.showerror("Error", "Invalid username or password")
        return

    member_id = result[0]

    # 查询所有课程
    cursor = db.cursor()
    query = "SELECT * FROM course"
    cursor.execute(query)
    courses = cursor.fetchall()

    # 创建会员菜单窗口
    member_menu = tk.Toplevel(root)
    member_menu.title("会员菜单")
    member_menu.geometry("600x400")

    def purchase_course(course_id, price):
        cursor = db.cursor()
        query = "INSERT INTO course_purchase (member_id, course_id, purchase_date, price) " \
                "VALUES (%s, %s, CURRENT_TIMESTAMP, %s)"
        values = (member_id, course_id, price)
        cursor.execute(query, values)
        db.commit()

        messagebox.showinfo("Success", "Course purchased successfully")

    # 创建Treeview
    tree = ttk.Treeview(member_menu, columns=("Course ID", "Name", "Description", "Price"), show="headings")
    tree.heading("Course ID", text="Course ID")
    tree.heading("Name", text="Name")
    tree.heading("Description", text="Description")
    tree.heading("Price", text="Price")

    tree.column("Course ID", width=80)
    tree.column("Name", width=120)
    tree.column("Description", width=300)
    tree.column("Price", width=80)

    tree.pack(fill="both", expand=True)

    for course in courses:
        tree.insert("", tk.END, values=course)

    def purchase_selected_course():
        selected_item = tree.focus()
        if selected_item:
            item_values = tree.item(selected_item)["values"]
            course_id = item_values[0]
            price = item_values[3]
            purchase_course(course_id, price)
        else:
            messagebox.showerror("Error", "Please select a course")

    button_purchase = tk.Button(member_menu, text="Purchase", command=purchase_selected_course)
    button_purchase.pack()

button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

root.mainloop()
