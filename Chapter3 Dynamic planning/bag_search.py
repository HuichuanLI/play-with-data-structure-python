# 背包问题解决

info = [
    [3, 8],
    [2, 5],
    [5, 12]
]

data = []
max_selects = []
max_value = 0


def search(depth, rest):
    if depth == 3:
        # print(data)
        values = [select * info[index][1] for index, select in enumerate(data)]
        global max_value
        if sum(values) > max_value:
            max_value = sum(values)
            global max_selects
            max_selects = data[:]
    else:
        # 1. 不放
        # 1。 设置现场
        data.append(0)
        search(depth + 1, rest)
        data.pop()
        # 2. 放
        if rest >= info[depth][0]:
            data.append(1)
            search(depth + 1, rest - info[depth][0])
            data.pop()


if __name__ == "__main__":
    search(0, 5)
    print(max_selects)
    print(max_value)
