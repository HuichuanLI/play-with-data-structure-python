from SortTestHelper import RandomArray, NearlyOrderArray
from SelectionSort import selectionSort
import time


def insertionSort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                break
    return alist


def insertionSortRange(alist, left, right):
    for i in range(left + 1, right + 1):
        currentvalue = alist[i]
        for j in range(i, left - 1, -1):
            if alist[j - 1] > currentvalue:
                alist[j] = alist[j - 1]
            else:
                break
        alist[j] = currentvalue
    return alist


def insertionSortUpdate(alist):
    for i in range(1, len(alist)):
        currentvalue = alist[i]
        for j in range(i, -1, -1):
            if alist[j - 1] > currentvalue:
                alist[j] = alist[j - 1]
            else:
                break
        alist[j] = currentvalue
    return alist


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = insertionSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = insertionSortUpdate(a)
    for w in a:
        print(w)

    # for w in nums:
    #     print(w)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=100, number=10000)
    nums = insertionSortUpdate(nums)
    time_end = time.time()
    print('Insertion totally cost', time_end - time_start)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=100, number=10000)
    nums = selectionSort(nums)
    time_end = time.time()
    print('Selection totally cost', time_end - time_start)

# 可见插入排序对近乎有序的数组很好
