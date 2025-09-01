#coding=utf-8
import random

# 第一题
def guess_number():
    target_number = random.randint(1, 10)
    chances = 3

    while chances > 0:
        guess = int(input("请输入一个1~10之间的数字: "))

        if guess == target_number:
            print("恭喜，猜对了！一共猜了", 4 - chances, "次")
            return

        if guess > target_number:
            print("猜大了！")
        else:
            print("猜小了！")

        chances -= 1

    print("游戏结束!")

# 测试第一题
guess_number()



