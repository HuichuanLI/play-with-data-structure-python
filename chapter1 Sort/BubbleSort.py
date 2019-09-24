from SortTestHelper import RandomArray, NearlyOrderArray
from SelectionSort import selectionSort
import time


def BubbleSort(alist):
    flag = False
    for i in range(0, len(alist)):
        for j in range(len(alist) - 1, i, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                flag = True
        if not flag:
            break
    return alist


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = BubbleSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = BubbleSort(a)
    for w in a:
        print(w)

    # for w in nums:
    #     print(w)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=100, number=10000)
    nums = BubbleSort(nums)
    time_end = time.time()
    print('Bubble totally cost', time_end - time_start)

    time_start = time.time()

    # nums = NearlyOrderArray(swap_times=100, number=10000)
    # nums = BubbleSort(nums)
    # time_end = time.time()
    # print('Selection totally cost', time_end - time_start)

# 可见插入排序对近乎有序的数组很好
