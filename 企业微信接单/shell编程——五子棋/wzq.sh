#!/bin/bash

# 定义棋盘大小
BOARD_SIZE=15

# 初始化空棋盘
initialize_board() {
    declare -gA board
    for ((i=0; i<BOARD_SIZE; i++)); do
        for ((j=0; j<BOARD_SIZE; j++)); do
            board[$i,$j]="."
        done
    done
}

# 打印棋盘
print_board() {
    # 打印列号
    printf "   "
    for ((j=0; j<BOARD_SIZE; j++)); do
        printf "%2d " $j  # 使用 %2d 确保每个列号占用两位字符空间
    done
    echo

    # 打印棋盘内容
    for ((i=0; i<BOARD_SIZE; i++)); do
        printf "%2d " $i  # 行号前加竖线，并确保行号占用两位字符空间
        for ((j=0; j<BOARD_SIZE; j++)); do
            printf " %s" "${board[$i,$j]}"  # 每个棋子后不加竖线，仅用空格分隔
        done
        echo
    done
}

# 获取玩家移动
get_move() {
    read -p "Player $1, enter your move (row col): " row col
    # 简单的输入验证
    if [[ ! $row =~ ^[0-9]+$ ]] || [[ ! $col =~ ^[0-9]+$ ]] || ((row < 0 || row >= BOARD_SIZE || col < 0 || col >= BOARD_SIZE)); then
        echo "Invalid input. Please enter numbers between 0 and $((BOARD_SIZE-1))."
        get_move $1
    fi
}

# 放置棋子
place_piece() {
    if [[ ${board[$row,$col]} == "." ]]; then
        board[$row,$col]=$1
    else
        echo "This position is already occupied. Try again."
        get_move $player
        place_piece $1
    fi
}

# 检查是否有玩家获胜
check_win() {
    local piece=$1
    # 检查行、列和对角线
    for ((i=0; i<BOARD_SIZE; i++)); do
        for ((j=0; j<=BOARD_SIZE-5; j++)); do
            # 行检查
            if [[ ${board[$i,$j]} == $piece && ${board[$i,$((j+1))]} == $piece && ${board[$i,$((j+2))]} == $piece && ${board[$i,$((j+3))]} == $piece && ${board[$i,$((j+4))]} == $piece ]]; then
                return 0
            fi
            # 列检查
            if [[ ${board[$j,$i]} == $piece && ${board[$((j+1)),$i]} == $piece && ${board[$((j+2)),$i]} == $piece && ${board[$((j+3)),$i]} == $piece && ${board[$((j+4)),$i]} == $piece ]]; then
                return 0
            fi
        done
    done
    # 对角线检查
    for ((i=0; i<=BOARD_SIZE-5; i++)); do
        for ((j=0; j<=BOARD_SIZE-5; j++)); do
            # 正对角线
            if [[ ${board[$i,$j]} == $piece && ${board[$((i+1)),$((j+1))]} == $piece && ${board[$((i+2)),$((j+2))]} == $piece && ${board[$((i+3)),$((j+3))]} == $piece && ${board[$((i+4)),$((j+4))]} == $piece ]]; then
                return 0
            fi
            # 反对角线
            if [[ ${board[$i,$((BOARD_SIZE-j-1))]} == $piece && ${board[$((i+1)),$((BOARD_SIZE-j-2))]} == $piece && ${board[$((i+2)),$((BOARD_SIZE-j-3))]} == $piece && ${board[$((i+3)),$((BOARD_SIZE-j-4))]} == $piece && ${board[$((i+4)),$((BOARD_SIZE-j-5))]} == $piece ]]; then
                return 0
            fi
        done
    done
    return 1
}

# 游戏循环
while true; do
    initialize_board
    player=1
    winner=0

    while [[ $winner -eq 0 ]]; do
        print_board
        get_move $player
        place_piece $player

        # 检查是否有玩家获胜
        if check_win $player; then
            print_board
            echo "Player $player wins!"
            winner=1
        fi

        # 切换玩家
        if [[ $player -eq 1 ]]; then
            player=2
        else
            player=1
        fi
    done

    # 游戏结束后询问玩家是否想再玩一次
    read -p "Do you want to play again? (y/n): " replay
    if [[ $replay != "y" && $replay != "Y" ]]; then
        break
    fi
done

echo "Thanks for playing!"