from datetime import datetime
from _collections import defaultdict

total = defaultdict(int)


# 记忆化搜索
def fib_test(k):
    assert k > 0, "k 必须大于0"
    if k in [1, 2]:
        return 1
    # 求解第k个数
    global total
    if k in total:
        return total[k]
    else:
        total[k] = fib_test(k - 1) + fib_test(k - 2)
        return total[k]


if __name__ == "__main__":
    # 搜索+记忆算法
    start_time = datetime.now()
    print(fib_test(100))
    print("递归时间:{}".format((datetime.now() - start_time).total_seconds()))
    print(total)

    # start_time = datetime.now()
    # print(fib_test2(35))
    # print("循环时间:{}".format((datetime.now() - start_time).total_seconds()))
    # # print(total)
