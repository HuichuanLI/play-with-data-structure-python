from MergeSort import __merge
import time
from SortTestHelper import RandomArray, NearlyOrderArray


# 自底向上的归并排序，是比自顶向下的归并排序要快的。
def mergeSortBu(alist):
    sz = 1
    while sz <= len(alist):
        for i in range(0, len(alist) - sz, 2 * sz):
            alist = __merge(alist, i, i + sz - 1, min(i + 2 * sz - 1, len(alist) - 1))
        sz = 2 * sz
    return alist


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    # nums = mergeSortBu(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = mergeSortBu(a)
    for w in a:
        print(w)

    # for w in nums:
    #     print(w)

    # time_start = time.time()
    #
    # nums = NearlyOrderArray(swap_times=0, number=50000)
    # nums = mergeSortBu(nums)
    # time_end = time.time()
    # print('Merge sort totally cost', time_end - time_start)
