from datetime import datetime
from _collections import defaultdict

total = defaultdict(int)


def fib_test(k):
    assert k > 0, "k 必须大于0"
    if k in [1, 2]:
        return 1
    # 求解第k个数
    global total
    total[k] += 1
    return fib_test(k - 1) + fib_test(k - 2)


def fib_test2(k):
    assert k > 0, "k 必须大于0"
    if k in [1, 2]:
        return k
    k_1 = 1
    k_2 = 1
    for i in range(3, k + 1):
        temp = k_2
        k_2 = k_1 + k_2
        k_1 = temp
    return k_2


if __name__ == "__main__":
    start_time = datetime.now()
    print(fib_test(35))
    print("递归时间:{}".format((datetime.now() - start_time).total_seconds()))
    print(total)

    start_time = datetime.now()
    print(fib_test2(35))
    print("循环时间:{}".format((datetime.now() - start_time).total_seconds()))
    # print(total)
