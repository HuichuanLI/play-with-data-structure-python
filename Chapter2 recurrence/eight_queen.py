# 八皇后问题

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
total = 0


def can_place(x, y):
    # 判断x行是否能放皇后
    for i in range(0, y):
        if board[x][i] == 1:
            return False
    for i in range(0, x):
        if board[i][y] == 1:
            return False
    # 判断斜线"/"是否有
    for i in range(0, x):
        if x + y - i <= 7 and board[i][x + y - i] == 1:
            return False
    # 判断斜线"\"是否有
    for index, i in enumerate(range(x - 1, -1, -1)):
        s_y = y - (index + 1)
        if s_y >= 0 and board[i][s_y] == 1:
            return False
    return True


def print_board():
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                print("□", end=" ")
            else:
                print("■", end=" ")
        print()


def put_queen(step):
    for i in range(8):
        if step == 8:
            global total
            total += 1
            print_board()
            print("------下一个--------")
            return
        else:
            if can_place(step, i):
                # 1.设置现场
                board[step][i] = 1
                # 2.开始递归
                put_queen(step + 1)
                # 3. 回复现场
                board[step][i] = 0


# 判断当前是否能放当前的皇后

if __name__ == "__main__":
    put_queen(0)
    print("总共有{}".format(total))
