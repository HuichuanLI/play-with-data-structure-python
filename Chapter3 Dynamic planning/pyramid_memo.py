pyramid = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]

datas = [13]
total_path = []
info = {}


def search_max(depth, y):
    if depth == 4:
        return pyramid[depth][y]
    # 1. 任务可以下分 2.最优化子结构 3.决策
    if "{}_{}".format(depth, y) in info:
        return info["{}_{}".format(depth, y)]
    else:
        left_max = search_max(depth + 1, y)
        right_max = search_max(depth + 1, y + 1)
        info["{}_{}".format(depth, y)] = pyramid[depth][y] + max(left_max, right_max)
    return pyramid[depth][y] + max(left_max, right_max)


if __name__ == "__main__":
    print(search_max(0, 0))
    print(info)
