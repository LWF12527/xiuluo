import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# MySQL数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'attendance'
}

# 创建数据库连接
db = mysql.connector.connect(**db_config)
cursor = db.cursor()


class AttendanceRecordForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.attendance_type_id = tk.StringVar()
        self.attendance_type_id.set("1")  # 默认选择第一个考勤类型

        self.employee_id = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        attendance_type_label = tk.Label(self, text="考勤类型:")
        attendance_type_label.pack()
        attendance_type_entry = tk.Entry(self, textvariable=self.attendance_type_id)
        attendance_type_entry.pack()

        employee_id_label = tk.Label(self, text="员工工号:")
        employee_id_label.pack()
        employee_id_entry = tk.Entry(self, textvariable=self.employee_id)
        employee_id_entry.pack()

        submit_button = tk.Button(self, text="提交", command=self.submit_attendance_record)
        submit_button.pack()

    def submit_attendance_record(self):
        attendance_type_id = self.attendance_type_id.get()
        employee_id = self.employee_id.get()

        if not attendance_type_id or not employee_id:
            messagebox.showerror("错误", "请填写完整的信息")
            return

        try:
            query = "INSERT INTO Attendance (EmployeeID, AttendanceTypeID) VALUES (%s, %s)"
            values = (employee_id, attendance_type_id)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("成功", "考勤记录已添加")
        except Exception as e:
            messagebox.showerror("错误", str(e))


class DeleteAttendanceRecordForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.attendance_id = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        attendance_id_label = tk.Label(self, text="考勤记录ID:")
        attendance_id_label.pack()
        attendance_id_entry = tk.Entry(self, textvariable=self.attendance_id)
        attendance_id_entry.pack()

        submit_button = tk.Button(self, text="提交", command=self.delete_attendance_record)
        submit_button.pack()

    def delete_attendance_record(self):
        attendance_id = self.attendance_id.get()

        if not attendance_id:
            messagebox.showerror("错误", "请填写考勤记录ID")
            return

        try:
            query = "DELETE FROM Attendance WHERE AttendanceID = %s"
            values = (attendance_id,)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("成功", "考勤记录已删除")
        except Exception as e:
            messagebox.showerror("错误", str(e))


class ModifyAttendanceRecordForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.attendance_id = tk.StringVar()
        self.attendance_type_id = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        attendance_id_label = tk.Label(self, text="考勤记录ID:")
        attendance_id_label.pack()
        attendance_id_entry = tk.Entry(self, textvariable=self.attendance_id)
        attendance_id_entry.pack()

        attendance_type_label = tk.Label(self, text="考勤类型:")
        attendance_type_label.pack()
        attendance_type_entry = tk.Entry(self, textvariable=self.attendance_type_id)
        attendance_type_entry.pack()

        submit_button = tk.Button(self, text="提交", command=self.modify_attendance_record)
        submit_button.pack()

    def modify_attendance_record(self):
        attendance_id = self.attendance_id.get()
        attendance_type_id = self.attendance_type_id.get()

        if not attendance_id or not attendance_type_id:
            messagebox.showerror("错误", "请填写完整的信息")
            return

        try:
            query = "UPDATE Attendance SET AttendanceTypeID = %s WHERE AttendanceID = %s"
            values = (attendance_type_id, attendance_id)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("成功", "考勤记录已修改")
        except Exception as e:
            messagebox.showerror("错误", str(e))


class QueryAttendanceRecordForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.query_type = tk.StringVar()
        self.query_value = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        query_type_label = tk.Label(self, text="查询类型:")
        query_type_label.pack()
        query_type_combobox = ttk.Combobox(self, textvariable=self.query_type, state="readonly")
        query_type_combobox['values'] = ('工号', '姓名')
        query_type_combobox.pack()

        query_value_label = tk.Label(self, text="查询值:")
        query_value_label.pack()
        query_value_entry = tk.Entry(self, textvariable=self.query_value)
        query_value_entry.pack()

        submit_button = tk.Button(self, text="提交", command=self.query_attendance_record)
        submit_button.pack()

    def query_attendance_record(self):
        query_type = self.query_type.get()
        query_value = self.query_value.get()

        if not query_type or not query_value:
            messagebox.showerror("错误", "请填写完整的信息")
            return

        try:
            if query_type == "工号":
                query = "SELECT * FROM AttendanceView WHERE EmployeeID = %s"
            elif query_type == "姓名":
                query = "SELECT * FROM AttendanceView WHERE Name = %s"
            else:
                messagebox.showerror("错误", "无效的查询类型")
                return

            values = (query_value,)
            cursor.execute(query, values)
            records = cursor.fetchall()

            if not records:
                messagebox.showinfo("提示", "未找到相关考勤记录")
            else:
                result = "考勤记录:\n"
                for record in records:
                    result += f"记录ID: {record[0]}, 日期: {record[1]}, 考勤类型: {record[2]},工号:{record[3]} 姓名: {record[4]}, 部门: {record[5]}, 职位: {record[6]}\n"
                messagebox.showinfo("查询结果", result)
        except Exception as e:
            messagebox.showerror("错误", str(e))


class AbsentEmployeesForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        start_date_label = tk.Label(self, text="开始日期(YYYY-MM-DD):")
        start_date_label.pack()
        start_date_entry = tk.Entry(self, textvariable=self.start_date)
        start_date_entry.pack()

        end_date_label = tk.Label(self, text="结束日期(YYYY-MM-DD):")
        end_date_label.pack()
        end_date_entry = tk.Entry(self, textvariable=self.end_date)
        end_date_entry.pack()

        submit_button = tk.Button(self, text="提交", command=self.get_absent_employees)
        submit_button.pack()

    def get_absent_employees(self):
        start_date = self.start_date.get()
        end_date = self.end_date.get()

        if not start_date or not end_date:
            messagebox.showerror("错误", "请填写完整的信息")
            return

        try:
            query = """
                SELECT Name, COUNT(*) AS AbsentCount FROM AttendanceView
                WHERE AttendanceTypeID = 1 AND Date BETWEEN %s AND %s
                GROUP BY Name
                ORDER BY AbsentCount DESC
            """
            values = (start_date, end_date)
            cursor.execute(query, values)
            records = cursor.fetchall()

            if not records:
                messagebox.showinfo("提示", "未找到旷工职员记录")
            else:
                result = "旷工职员统计:\n"
                for record in records:
                    result += f"姓名: {record[0]}, 旷工次数: {record[1]}\n"
                messagebox.showinfo("查询结果", result)
        except Exception as e:
            messagebox.showerror("错误", str(e))


class AbsentDepartmentsForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        start_date_label = tk.Label(self, text="开始日期(YYYY-MM-DD):")
        start_date_label.pack()
        start_date_entry = tk.Entry(self, textvariable=self.start_date)
        start_date_entry.pack()

        end_date_label = tk.Label(self, text="结束日期(YYYY-MM-DD):")
        end_date_label.pack()
        end_date_entry = tk.Entry(self, textvariable=self.end_date)
        end_date_entry.pack()

        submit_button = tk.Button(self, text="提交", command=self.get_absent_departments)
        submit_button.pack()

    def get_absent_departments(self):
        start_date = self.start_date.get()
        end_date = self.end_date.get()

        if not start_date or not end_date:
            messagebox.showerror("错误", "请填写完整的信息")
            return

        try:
            query = """
                SELECT Department, COUNT(*) AS AbsentCount FROM AttendanceView
                WHERE AttendanceTypeID = 1 AND Date BETWEEN %s AND %s
                GROUP BY Department
                ORDER BY AbsentCount DESC
            """
            values = (start_date, end_date)
            cursor.execute(query, values)
            records = cursor.fetchall()

            if not records:
                messagebox.showinfo("提示", "未找到旷工部门记录")
            else:
                result = "旷工部门统计:\n"
                for record in records:
                    result += f"部门: {record[0]}, 旷工人次: {record[1]}\n"
                messagebox.showinfo("查询结果", result)
        except Exception as e:
            messagebox.showerror("错误", str(e))


class AttendanceManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("公司考勤管理系统")
        self.geometry("400x300")

        # 创建一个容器
        container = tk.Frame(self)
        container.pack(side=tk.LEFT, padx=10, pady=10)

        # 使用pack布局管理器，使得按钮竖直排列
        record_attendance_button = tk.Button(container, text="记录考勤记录", command=self.record_attendance)
        record_attendance_button.pack(side=tk.TOP)

        delete_attendance_record_button = tk.Button(container, text="删除考勤记录", command=self.delete_attendance_record)
        delete_attendance_record_button.pack(side=tk.TOP)

        modify_attendance_record_button = tk.Button(container, text="修改考勤记录", command=self.modify_attendance_record)
        modify_attendance_record_button.pack(side=tk.TOP)

        query_attendance_record_button = tk.Button(container, text="查询考勤记录", command=self.query_attendance_record)
        query_attendance_record_button.pack(side=tk.TOP)

        get_absent_employees_button = tk.Button(container, text="旷工职员统计", command=self.get_absent_employees)
        get_absent_employees_button.pack(side=tk.TOP)

        get_absent_departments_button = tk.Button(container, text="旷工部门统计", command=self.get_absent_departments)
        get_absent_departments_button.pack(side=tk.TOP)

        # 创建一个容器用于显示功能窗体
        self.function_frame = tk.Frame(self)
        self.function_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # 设置背景色和文字颜色
        self.configure(background='lightblue')  # 背景色
        record_attendance_button.configure(background='blue', fg='white')  # 文字颜色为白色
        delete_attendance_record_button.configure(background='red', fg='white')  # 文字颜色为白色
        modify_attendance_record_button.configure(background='green', fg='white')  # 文字颜色为白色
        query_attendance_record_button.configure(background='purple', fg='white')  # 文字颜色为白色
        get_absent_employees_button.configure(background='orange', fg='black')  # 文字颜色为黑色
        get_absent_departments_button.configure(background='pink', fg='black')  # 文字颜色为黑色

    def clear_function_frame(self):
        # 清空功能窗体
        for widget in self.function_frame.winfo_children():
            widget.destroy()

    def record_attendance(self):
        self.clear_function_frame()
        form = AttendanceRecordForm(self.function_frame)
        form.pack()

    def delete_attendance_record(self):
        self.clear_function_frame()
        form = DeleteAttendanceRecordForm(self.function_frame)
        form.pack()

    def modify_attendance_record(self):
        self.clear_function_frame()
        form = ModifyAttendanceRecordForm(self.function_frame)
        form.pack()

    def query_attendance_record(self):
        self.clear_function_frame()
        form = QueryAttendanceRecordForm(self.function_frame)
        form.pack()

    def get_absent_employees(self):
        self.clear_function_frame()
        form = AbsentEmployeesForm(self.function_frame)
        form.pack()

    def get_absent_departments(self):
        self.clear_function_frame()
        form = AbsentDepartmentsForm(self.function_frame)
        form.pack()


if __name__ == "__main__":
    app = AttendanceManagementSystem()
    app.mainloop()