import tkinter.ttk as ttk
from tkinter import messagebox, scrolledtext
import mysql.connector
from tkinter import *

# 连接MySQL数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="medicine"
)

# 创建主窗口
root = Tk()
root.title("药房库存管理系统")
root.geometry("600x400")

# 获取游标
mycursor = mydb.cursor()

# 添加药品分类
def add_category():
    def save_category():
        category_name = entry_category.get()

        # 添加药品分类
        sql = "INSERT INTO drug_category (name) VALUES (%s)"
        val = (category_name,)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("提示", "药品分类添加成功！")
        category_window.destroy()

    category_window = Toplevel(root)
    category_window.title("添加药品分类")

    label_category = Label(category_window, text="药品分类名称：")
    label_category.pack()

    entry_category = Entry(category_window)
    entry_category.pack()

    button_save = Button(category_window, text="保存", command=save_category)
    button_save.pack()

# 添加药品
def add_drug():
    def save_drug():
        name = entry_name.get()
        manufacturer = entry_manufacturer.get()
        price = float(entry_price.get())
        dosage_form = entry_dosage_form.get()
        specification = entry_specification.get()
        quantity = entry_inventory_quantity.get()

        # 添加药品分类
        sql = "INSERT INTO drug_category (name) VALUES (%s)"
        val = (combobox_category.get(),)
        mycursor.execute(sql, val)
        mydb.commit()

        # 获取药品分类ID
        category_id = mycursor.lastrowid

        # 添加药品
        sql = "INSERT INTO drug (name, manufacturer, price, dosage_form, specification) VALUES (%s, %s, %s, %s, %s)"
        val = (name, manufacturer, price, dosage_form, specification)
        mycursor.execute(sql, val)
        mydb.commit()

        # 添加药品分类关联
        drug_id = mycursor.lastrowid
        sql = "INSERT INTO drug_category_relation (drug_id, category_id) VALUES (%s, %s)"
        val = (drug_id, category_id)
        mycursor.execute(sql, val)
        mydb.commit()

        # 添加药品库存信息
        sql = "INSERT INTO drug_inventory (drug_id, inventory_quantity) VALUES (%s, %s)"
        val = (drug_id, quantity)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("提示", "药品添加成功！")
        drug_window.destroy()

    drug_window = Toplevel(root)
    drug_window.title("添加药品")

    label_name = Label(drug_window, text="药品名称：")
    label_name.grid(row=0, column=0, padx=5, pady=5)

    entry_name = Entry(drug_window)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    label_manufacturer = Label(drug_window, text="药品生产厂家：")
    label_manufacturer.grid(row=1, column=0, padx=5, pady=5)

    entry_manufacturer = Entry(drug_window)
    entry_manufacturer.grid(row=1, column=1, padx=5, pady=5)

    label_price = Label(drug_window, text="药品进价：")
    label_price.grid(row=2, column=0, padx=5, pady=5)

    entry_price = Entry(drug_window)
    entry_price.grid(row=2, column=1, padx=5, pady=5)

    label_dosage_form = Label(drug_window, text="药品剂型：")
    label_dosage_form.grid(row=3, column=0, padx=5, pady=5)

    entry_dosage_form = Entry(drug_window)
    entry_dosage_form.grid(row=3, column=1, padx=5, pady=5)

    label_specification = Label(drug_window, text="药品规格：")
    label_specification.grid(row=4, column=0, padx=5, pady=5)

    entry_specification = Entry(drug_window)
    entry_specification.grid(row=4, column=1, padx=5, pady=5)

    # 显示药品分类列表供选择
    mycursor.execute("SELECT * FROM drug_category")
    categories = mycursor.fetchall()

    label_category = Label(drug_window, text="药品分类：")
    label_category.grid(row=5, column=0, padx=5, pady=5)

    combobox_category = ttk.Combobox(drug_window, values=[category[1] for category in categories])
    combobox_category.grid(row=5, column=1, padx=5, pady=5)

    label_inventory_quantity = Label(drug_window, text="药品库存数量：")
    label_inventory_quantity.grid(row=6, column=0, padx=5, pady=5)

    entry_inventory_quantity = Entry(drug_window)
    entry_inventory_quantity.grid(row=6, column=1, padx=5, pady=5)

    button_save = Button(drug_window, text="保存", command=save_drug)
    button_save.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# 查询药品
def query_drug():
    def search_drug():
        name = entry_name.get()

        # 查询药品信息
        sql = "SELECT drug.id, drug.name, drug.manufacturer, drug.price, drug.dosage_form, drug.specification, drug_inventory.inventory_quantity FROM drug INNER JOIN drug_inventory ON drug.id = drug_inventory.drug_id WHERE drug.name = %s"
        val = (name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            result_text.delete(1.0, END)
            result_text.insert(END, f"药品编号：{result[0]}\n药品名称：{result[1]}\n药品生产厂家：{result[2]}\n药品进价：{result[3]}\n药品剂型：{result[4]}\n药品规格：{result[5]}\n药品库存数量：{result[6]}")
        else:
            messagebox.showerror("错误", "没有找到该药品！")

    query_window = Toplevel(root)
    query_window.title("查询药品")

    label_name = Label(query_window, text="药品名称：")
    label_name.grid(row=0, column=0, padx=5, pady=5)

    entry_name = Entry(query_window)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    button_search = Button(query_window, text="查询", command=search_drug)
    button_search.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    result_text = scrolledtext.ScrolledText(query_window, width=60, height=10)
    result_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


# 删除药品


def delete_drug():
    def confirm_delete():
        drug_name = entry_drug_name.get()

        # 检查药品是否存在
        sql = "SELECT id FROM drug WHERE name = %s"
        val = (drug_name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if not result:
            messagebox.showerror("错误", "没有找到该药品！")
            delete_window.destroy()
            return

        # 删除药品分类关联记录
        sql = "DELETE FROM drug_category_relation WHERE drug_id = %s"
        val = (result[0],)
        mycursor.execute(sql, val)
        mydb.commit()

        # 删除药品销售记录
        sql = "DELETE FROM drug_sale WHERE drug_id = %s"
        mycursor.execute(sql, val)
        mydb.commit()

        # 删除药品进货记录
        sql = "DELETE FROM drug_purchase WHERE drug_id = %s"
        mycursor.execute(sql, val)
        mydb.commit()

        # 删除药品库存记录
        sql = "DELETE FROM drug_inventory WHERE drug_id = %s"
        mycursor.execute(sql, val)
        mydb.commit()

        # 删除药品
        sql = "DELETE FROM drug WHERE name = %s"
        val = (drug_name,)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("提示", "药品删除成功！")
        delete_window.destroy()

    def confirm_delete_message():
        result = messagebox.askquestion("确认删除", "将删除所有关于该药品的记录，是否确认删除？")
        if result == 'yes':
            confirm_delete()

    delete_window = Toplevel(root)
    delete_window.title("删除药品")

    label_drug_name = Label(delete_window, text="药品名称：")
    label_drug_name.grid(row=0, column=0, padx=5, pady=5)

    entry_drug_name = Entry(delete_window)
    entry_drug_name.grid(row=0, column=1, padx=5, pady=5)

    button_confirm = Button(delete_window, text="确认删除", command=confirm_delete_message)
    button_confirm.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


# 添加药品销售记录
def add_sale():
    def save_sale():
        drug_name = entry_drug_name.get()
        sale_quantity = int(entry_sale_quantity.get())
        sale_price = float(entry_sale_price.get())
        sale_date = entry_sale_date.get()

        # 获取药品ID
        sql = "SELECT id FROM drug WHERE name = %s"
        val = (drug_name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if not result:
            messagebox.showerror("错误", "没有找到该药品！")
            return
        drug_id = result[0]

        # 添加销售记录
        sql = "INSERT INTO drug_sale (drug_id, sale_date, sale_quantity, sale_price) VALUES (%s, %s, %s, %s)"
        val = (drug_id, sale_date, sale_quantity, sale_price)
        mycursor.execute(sql, val)
        mydb.commit()

        # 更新药品库存记录
        sql = "UPDATE drug_inventory SET inventory_quantity = inventory_quantity - %s WHERE drug_id = %s"
        val = (sale_quantity, drug_id)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("提示", "销售记录添加成功！")
        sale_window.destroy()

    sale_window = Toplevel(root)
    sale_window.title("添加药品销售记录")

    label_drug_name = Label(sale_window, text="药品名称：")
    label_drug_name.grid(row=0, column=0, padx=5, pady=5)

    entry_drug_name = Entry(sale_window)
    entry_drug_name.grid(row=0, column=1, padx=5, pady=5)

    label_sale_quantity = Label(sale_window, text="销售数量：")
    label_sale_quantity.grid(row=1, column=0, padx=5, pady=5)

    entry_sale_quantity = Entry(sale_window)
    entry_sale_quantity.grid(row=1, column=1, padx=5, pady=5)

    label_sale_price = Label(sale_window, text="销售单价：")
    label_sale_price.grid(row=2, column=0, padx=5, pady=5)

    entry_sale_price = Entry(sale_window)
    entry_sale_price.grid(row=2, column=1, padx=5, pady=5)

    label_sale_date = Label(sale_window, text="销售日期（YYYY-MM-DD）：")
    label_sale_date.grid(row=3, column=0, padx=5, pady=5)

    entry_sale_date = Entry(sale_window)
    entry_sale_date.grid(row=3, column=1, padx=5, pady=5)

    button_save = Button(sale_window, text="保存", command=save_sale)
    button_save.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# 添加药品进货记录
def add_purchase():
    def save_purchase():
        drug_name = entry_drug_name.get()
        purchase_quantity = int(entry_purchase_quantity.get())
        purchase_price = float(entry_purchase_price.get())
        purchase_date = entry_purchase_date.get()

        # 获取药品ID
        sql = "SELECT id FROM drug WHERE name = %s"
        val = (drug_name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if not result:
            messagebox.showerror("错误", "没有找到该药品！")
            return
        drug_id = result[0]

        # 添加进货记录
        sql = "INSERT INTO drug_purchase (drug_id, purchase_date, purchase_quantity, purchase_price) VALUES (%s, %s, %s, %s)"
        val = (drug_id, purchase_date, purchase_quantity, purchase_price)
        mycursor.execute(sql, val)
        mydb.commit()

        # 更新药品库存记录
        sql = "UPDATE drug_inventory SET inventory_quantity = inventory_quantity + %s WHERE drug_id = %s"
        val = (purchase_quantity, drug_id)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("提示", "进货记录添加成功！")
        purchase_window.destroy()

    purchase_window = Toplevel(root)
    purchase_window.title("添加药品进货记录")

    label_drug_name = Label(purchase_window, text="药品名称：")
    label_drug_name.grid(row=0, column=0, padx=5, pady=5)

    entry_drug_name = Entry(purchase_window)
    entry_drug_name.grid(row=0, column=1, padx=5, pady=5)

    label_purchase_quantity = Label(purchase_window, text="进货数量：")
    label_purchase_quantity.grid(row=1, column=0, padx=5, pady=5)

    entry_purchase_quantity = Entry(purchase_window)
    entry_purchase_quantity.grid(row=1, column=1, padx=5, pady=5)

    label_purchase_price = Label(purchase_window, text="进货单价：")
    label_purchase_price.grid(row=2, column=0, padx=5, pady=5)

    entry_purchase_price = Entry(purchase_window)
    entry_purchase_price.grid(row=2, column=1, padx=5, pady=5)

    label_purchase_date = Label(purchase_window, text="进货日期（YYYY-MM-DD）：")
    label_purchase_date.grid(row=3, column=0, padx=5, pady=5)

    entry_purchase_date = Entry(purchase_window)
    entry_purchase_date.grid(row=3, column=1, padx=5, pady=5)

    button_save = Button(purchase_window, text="保存", command=save_purchase)
    button_save.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# 查询药品销售信息
def query_sale():
    def search_sale():
        start_date = entry_start_date.get()
        end_date = entry_end_date.get()

        # 查询销售信息
        sql = "SELECT drug.name, SUM(drug_sale.sale_quantity), SUM(drug_sale.sale_quantity * drug_sale.sale_price) FROM drug_sale INNER JOIN drug ON drug_sale.drug_id = drug.id WHERE sale_date BETWEEN %s AND %s GROUP BY drug.name"
        val = (start_date, end_date)
        mycursor.execute(sql, val)
        results = mycursor.fetchall()
        if results:
            result_text.delete(1.0, END)
            result_text.insert(END, "药品名称\t销售数量\t销售总金额\n")
            for result in results:
                result_text.insert(END, f"{result[0]}\t{result[1]}\t{result[2]}\n")
        else:
            messagebox.showerror("错误", "没有找到销售信息！")

    sale_window = Toplevel(root)
    sale_window.title("查询药品销售信息")

    label_start_date = Label(sale_window, text="起始日期（YYYY-MM-DD）：")
    label_start_date.grid(row=0, column=0, padx=5, pady=5)

    entry_start_date = Entry(sale_window)
    entry_start_date.grid(row=0, column=1, padx=5, pady=5)

    label_end_date = Label(sale_window, text="结束日期（YYYY-MM-DD）：")
    label_end_date.grid(row=1, column=0, padx=5, pady=5)

    entry_end_date = Entry(sale_window)
    entry_end_date.grid(row=1, column=1, padx=5, pady=5)

    button_search = Button(sale_window, text="查询", command=search_sale)
    button_search.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    result_text = scrolledtext.ScrolledText(sale_window, width=60, height=10)
    result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 查询药品进货信息
def query_purchase():
    def search_purchase():
        start_date = entry_start_date.get()
        end_date = entry_end_date.get()

        # 查询进货信息
        sql = "SELECT drug.name, SUM(drug_purchase.purchase_quantity), SUM(drug_purchase.purchase_quantity * drug_purchase.purchase_price) FROM drug_purchase INNER JOIN drug ON drug_purchase.drug_id = drug.id WHERE purchase_date BETWEEN %s AND %s GROUP BY drug.name"
        val = (start_date, end_date)
        mycursor.execute(sql, val)
        results = mycursor.fetchall()
        if results:
            result_text.delete(1.0, END)
            result_text.insert(END, "药品名称\t进货数量\t进货总金额\n")
            for result in results:
                result_text.insert(END, f"{result[0]}\t{result[1]}\t{result[2]}\n")
        else:
            messagebox.showerror("错误", "没有找到进货信息！")

    purchase_window = Toplevel(root)
    purchase_window.title("查询药品进货信息")

    label_start_date = Label(purchase_window, text="起始日期（YYYY-MM-DD）：")
    label_start_date.grid(row=0, column=0, padx=5, pady=5)

    entry_start_date = Entry(purchase_window)
    entry_start_date.grid(row=0, column=1, padx=5, pady=5)

    label_end_date = Label(purchase_window, text="结束日期（YYYY-MM-DD）：")
    label_end_date.grid(row=1, column=0, padx=5, pady=5)

    entry_end_date = Entry(purchase_window)
    entry_end_date.grid(row=1, column=1, padx=5, pady=5)

    button_search = Button(purchase_window, text="查询", command=search_purchase)
    button_search.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    result_text = scrolledtext.ScrolledText(purchase_window, width=60, height=10)
    result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 查询药品库存信息
def query_inventory():
    # 查询库存信息
    sql = "SELECT drug.name, drug.manufacturer, drug_inventory.inventory_quantity, drug.price, drug.dosage_form, drug.specification FROM drug INNER JOIN drug_inventory ON drug.id = drug_inventory.drug_id"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    if results:
        result_text.delete(1.0, END)
        result_text.insert(END, "药品名称\t生产厂家\t库存数量\t进价\t剂型\t规格\n")
        for result in results:
            result_text.insert(END, f"{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}\t{result[4]}\t{result[5]}\n")
    else:
        messagebox.showerror("错误", "没有找到库存信息！")

# 创建菜单栏
menu_bar = Menu(root)
root.config(menu=menu_bar)

# 创建退出菜单
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="退出", menu=file_menu)
file_menu.add_command(label="退出", command=root.quit)

# 创建药品分类菜单
category_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="药品分类", menu=category_menu)
category_menu.add_command(label="添加药品分类", command=add_category)

# 创建药品菜单
drug_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="药品", menu=drug_menu)
drug_menu.add_command(label="添加药品", command=add_drug)
drug_menu.add_command(label="查询药品", command=query_drug)
drug_menu.add_command(label="删除药品", command=delete_drug)


# 创建销售菜单
sale_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="销售", menu=sale_menu)
sale_menu.add_command(label="添加销售记录", command=add_sale)
sale_menu.add_command(label="查询销售信息", command=query_sale)

# 创建进货菜单
purchase_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="进货", menu=purchase_menu)
purchase_menu.add_command(label="添加进货记录", command=add_purchase)
purchase_menu.add_command(label="查询进货信息", command=query_purchase)

# 创建库存菜单
inventory_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="库存", menu=inventory_menu)
inventory_menu.add_command(label="查询库存信息", command=query_inventory)

# 创建查询结果文本框和滚动条
result_frame = Frame(root)
result_frame.pack(fill=BOTH, expand=True)

result_text = scrolledtext.ScrolledText(result_frame, width=60, height=20)
result_text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(result_frame)
scrollbar.pack(side=RIGHT, fill=Y)

result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

# 主循环
root.mainloop()
