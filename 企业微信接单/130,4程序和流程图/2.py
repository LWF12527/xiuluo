#coding=utf-8
def calculate_discount():
    amount = float(input("请输入消费金额: "))
    member_type = input("请输入会员编号（金卡、普通、非会员）: ")

    if member_type == "金卡":
        total_amount = amount * 0.9
    elif member_type == "普通":
        total_amount = amount * 0.95
    else:
        total_amount = amount * 0.99

    print("最后应付金额为: {:.2f}".format(total_amount))
# 测试第二题
calculate_discount()