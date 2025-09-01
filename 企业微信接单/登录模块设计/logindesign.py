# 用户名和密码信息
users = {'zl': '123', 'ly': '123', 'wj': '123'}

# 信息列表
infos = [{'编号': '001', '名称': '苹果', '计算量1': 10, '计算量2': 20},
         {'编号': '002', '名称': '香蕉', '计算量1': 15, '计算量2': 25},
         {'编号': '003', '名称': '橙子', '计算量1': 8, '计算量2': 18}]

# 登录函数
def login():
    for i in range(3):
        username = input("请输入用户名：")
        if username not in users.keys():
            print("用户名不存在，请重新输入！")
        else:
            for j in range(3):
                password = input("请输入密码：")
                if password == users[username]:
                    print("登录成功！")
                    return True
                else:
                    print("密码错误，请重新输入！")
    print("登录失败！")
    return False

# 系统主界面
def main():
    while True:
        print("------系统主界面------")
        print("1. 添加信息")
        print("2. 查找信息")
        print("3. 删除信息")
        print("4. 修改信息")
        print("5. 排序信息")
        print("6. 统计信息")
        print("7. 显示所有信息")
        print("8. 退出系统")
        choice = input("请输入您的选择：")
        if choice == '1':
            add_info()
        elif choice == '2':
            search_info()
        elif choice == '3':
            delete_info()
        elif choice == '4':
            modify_info()
        elif choice == '5':
            sort_info()
        elif choice == '6':
            count_info()
        elif choice == '7':
            show_info()
        elif choice == '8':
            print("感谢使用！")
            break
        else:
            print("输入有误，请重新输入！")

# 添加信息函数
def add_info():
    print("添加信息")
    info = {}
    info['编号'] = input("请输入编号：")
    info['名称'] = input("请输入名称：")
    info['计算量1'] = int(input("请输入计算量1："))
    info['计算量2'] = int(input("请输入计算量2："))
    infos.append(info)
    print("添加成功！")

# 查找信息函数
def search_info():
    print("查找信息")
    choice = input("请选择查找条件（1.编号 2.名称）：")
    if choice == '1':
        num = input("请输入编号：")
        for info in infos:
            if info['编号'] == num:
                print(info)
                break
        else:
            print("未找到该信息！")
    elif choice == '2':
        name = input("请输入名称：")
        for info in infos:
            if info['名称'] == name:
                print(info)
                break
        else:
            print("未找到该信息！")
    else:
        print("输入有误，请重新选择！")

# 删除信息函数
def delete_info():
    print("删除信息")
    choice = input("请选择删除条件（1.编号 2.名称）：")
    if choice == '1':
        num = input("请输入编号：")
        for info in infos:
            if info['编号'] == num:
                infos.remove(info)
                print("删除成功！")
                break
        else:
            print("未找到该信息！")
    elif choice == '2':
        name = input("请输入名称：")
        for info in infos:
            if info['名称'] == name:
                infos.remove(info)
                print("删除成功！")
                break
        else:
            print("未找到该信息！")
    else:
        print("输入有误，请重新选择！")

# 修改信息函数
def modify_info():
    print("修改信息")
    choice = input("请选择修改条件（1.编号 2.名称）：")
    if choice == '1':
        num = input("请输入编号：")
        for info in infos:
            if info['编号'] == num:
                info['名称'] = input("请输入名称：")
                info['计算量1'] = int(input("请输入计算量1："))
                info['计算量2'] = int(input("请输入计算量2："))
                print("修改成功！")
                break
        else:
            print("未找到该信息！")
    elif choice == '2':
        name = input("请输入名称：")
        for info in infos:
            if info['名称'] == name:
                info['编号'] = input("请输入编号：")
                info['计算量1'] = int(input("请输入计算量1："))
                info['计算量2'] = int(input("请输入计算量2："))
                print("修改成功！")
                break
        else:
            print("未找到该信息！")
    else:
        print("输入有误，请重新选择！")

# 排序信息函数
def sort_info():
    print("排序信息")
    choice = input("请选择排序条件（1.计算量1升序 2.计算量2降序）：")
    if choice == '1':
        infos.sort(key=lambda x: x['计算量1'])
    elif choice == '2':
        infos.sort(key=lambda x: x['计算量2'], reverse=True)
    else:
        print("输入有误，请重新选择！")
        return
    print("排序后的信息为：")
    for info in infos:
        print(info)

# 统计信息函数
def count_info():
    print("统计信息")
    print("系统中共有%d条信息。" % len(infos))
    total1 = 0
    total2 = 0
    for info in infos:
        total1 += info['计算量1']
        total2 += info['计算量2']
    print("计算量1总和为：%d，计算量2总和为：%d。" % (total1, total2))
    max1 = max(infos, key=lambda x: x['计算量1'])
    max2 = max(infos, key=lambda x: x['计算量2'])
    print("计算量1最大值为：%d，对应信息为：%s。" % (max1['计算量1'], max1))
    print("计算量2最大值为：%d，对应信息为：%s。" % (max2['计算量2'], max2))

# 显示所有信息函数
def show_info():
    print("显示所有信息")
    for info in infos:
        print(info)

# 程序入口
if login():
    main()