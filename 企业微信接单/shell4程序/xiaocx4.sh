#!/bin/bash

# 定义函数：打印Shell常用命令
shell_commands() {
    echo "常用的Shell命令如下："
    echo "1) ls：列出当前目录下的文件和文件夹"
    echo "   示例：ls"
    echo
    echo "2) cd：切换当前目录"
    echo "   示例：cd /path/to/directory"
    echo
    echo "3) cp：复制文件或目录"
    echo "   示例：cp source_file target_file"
    echo
    echo "4) rm：删除文件或目录"
    echo "   示例：rm file_or_directory"
    echo
    echo "5) mv：移动文件或目录"
    echo "   示例：mv source_file target_file"
}

# 定义函数：石头剪刀布游戏
shell_stonegame() {
    echo "欢迎进入石头剪刀布游戏！"
    echo "请根据提示选择你的手势："
    echo "1) 石头"
    echo "2) 剪刀"
    echo "3) 布"
  
    read -p "请输入数字选择手势：" gesture

    case $gesture in
        1)
            user_gesture="石头"
            ;;
        2)
            user_gesture="剪刀"
            ;;
        3)
            user_gesture="布"
            ;;
        *)
            echo "无效的输入，请重新运行游戏。"
            return
            ;;
    esac

    computer_gesture=$((RANDOM % 3 + 1))
    case $computer_gesture in
        1)
            computer_gesture="石头"
            ;;
        2)
            computer_gesture="剪刀"
            ;;
        3)
            computer_gesture="布"
            ;;
    esac

    echo "你选择了：$user_gesture"
    echo "电脑选择了：$computer_gesture"

    if [[ $user_gesture == $computer_gesture ]]; then
        echo "平局！"
    elif [[ ($user_gesture == "石头" && $computer_gesture == "剪刀") || ($user_gesture == "剪刀" && $computer_gesture == "布") || ($user_gesture == "布" && $computer_gesture == "石头") ]]; then
        echo "你赢了！"
    else
        echo "你输了！"
    fi
}

# 定义函数：加减乘除计算器
shell_calculator() {
    read -p "请输入第一个数字：" num1
    read -p "请输入第二个数字：" num2

    echo "请选择运算操作："
    echo "1) 加法"
    echo "2) 减法"
    echo "3) 乘法"
    echo "4) 除法"

    read -p "请输入数字选择运算操作：" operation

    case $operation in
        1)
            result=$(($num1 + $num2))
            operator="+"
            ;;
        2)
            result=$(($num1 - $num2))
            operator="-"
            ;;
        3)
            result=$(($num1 * $num2))
            operator="*"
            ;;
        4)
            result=$(($num1 / $num2))
            operator="/"
            ;;
        *)
            echo "无效的输入，请重新运行计算器。"
            return
            ;;
    esac

    echo "$num1 $operator $num2 = $result"
}

# 定义函数：学生成绩管理系统
student_score() {
    while true; do
        echo "请选择操作："
        echo "1) 录入学生信息"
        echo "2) 从文件读取学生信息"
        echo "3) 打印学生信息"
        echo "4) 保存学生信息到文件"
        echo "5) 返回主菜单"

        read -p "请输入数字选择操作：" choice

        case $choice in
            1)
                read -p "请输入学生姓名：" name
                read -p "请输入学生成绩：" score
                echo "$name $score" >> students.txt
                echo "学生信息已录入。"
                ;;
            2)
                if [[ -f "students.txt" ]]; then
                    echo "从文件中读取的学生信息如下："
                    cat students.txt
                else
                    echo "文件不存在或为空。"
                fi
                ;;
            3)
                if [[ -f "students.txt" ]]; then
                    echo "学生信息如下："
                    cat students.txt
                else
                    echo "文件不存在或为空。"
                fi
                ;;
            4)
                if [[ -f "students.txt" ]]; then
                    cp students.txt students_backup.txt
                    echo "学生信息已保存到文件students_backup.txt。"
                else
                    echo "文件不存在或为空。"
                fi
                ;;
            5)
                return
                ;;
            *)
                echo "无效的输入，请重新选择操作。"
                ;;
        esac
    done
}

# 主菜单
echo "欢迎使用Shell脚本功能选择程序！"

while true; do
    echo "请选择功能："
    echo "1) Shell常用命令"
    echo "2) 石头剪刀布游戏"
    echo "3) 加减乘除计算器"
    echo "4) 学生成绩管理系统"
    echo "5) 退出程序"

    read -p "请输入数字选择功能：" option

    case $option in
        1)
            shell_commands
            ;;
        2)
            shell_stonegame
            ;;
        3)
            shell_calculator
            ;;
        4)
            student_score
            ;;
        5)
            echo "程序已退出。"
            exit
            ;;
        *)
            echo "无效的输入，请重新选择功能。"
            ;;
    esac

    echo
done

