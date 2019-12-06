data_list = [1, 2, 3, 4]

arranges = []

total = 0


def search(depth, datas):
    if depth == len(data_list) + 1:
        print(arranges)
        global total
        total += 1
    else:
        for element in datas:
            # 1.设置现场
            arranges.append(element)
            next_datas = datas[:]
            next_datas.remove(element)
            # 2.递归
            search(depth + 1, next_datas)
            # 3.恢复现场
            arranges.pop()


if __name__ == "__main__":
    search(1, data_list)
    print("有{}排列方式".format(total))
