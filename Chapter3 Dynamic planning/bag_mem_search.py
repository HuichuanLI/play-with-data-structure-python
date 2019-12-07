# 背包问题解决记忆

info = [
    [3, 8],
    [2, 5],
    [5, 12]
]

mem = {}


def search(depth, rest):
    global mem
    if "{}_{}".format(depth, rest) in mem:
        return mem["{}_{}".format(depth, rest)]

    if depth == 2:
        data = info[depth][1] if rest >= info[depth][0] else 0
    else:
        # 1.分任务
        a = search(depth + 1, rest)
        if rest >= info[depth][0]:
            b = search(depth + 1, rest - info[depth][0]) + info[depth][1]
        # 2. 选最大
        data = max(a, b)
    if "{}_{}".format(depth, rest) not in mem:
        mem["{}_{}".format(depth, rest)] = data

    return data


if __name__ == "__main__":
    print(search(0, 5))
    print(mem)
