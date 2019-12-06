num = 7

datas = []


def search(rest):
    if rest <= 0:
        print(datas)
    else:
        for i in range(1, rest + 1):
            datas.append(i)
            search(rest - i)
            datas.pop()


search(num)
