import math

def calculate_distance():
    x = 0
    y = 0

    while True:
        direction = input("请输入移动方向（上、下、左、右）：")
        if direction.lower() == "q":
            break

        steps = int(input("请输入移动步数："))

        if direction.lower() == "上":
            y += steps
        elif direction.lower() == "下":
            y -= steps
        elif direction.lower() == "左":
            x -= steps
        elif direction.lower() == "右":
            x += steps

    distance = math.sqrt(x**2 + y**2)
    print("当前位置与原点的距离为：", round(distance))

calculate_distance()
