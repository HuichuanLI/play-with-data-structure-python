from SortTestHelper import RandomArray, NearlyOrderArray
from SelectionSort import selectionSort
from InsertionSort import insertionSort, insertionSortRange
import time

import sys

sys.setrecursionlimit(1000000)


#
def __quickSort(alist, left, right):
    if left > right:
        return
    p = None
    p = __partion(alist, left, right)
    __quickSort(alist, left, p - 1)
    __quickSort(alist, p + 1, right)
    return alist


# 对 arr[l,r] 进行partiton 操做
def __partion(alist, left, right):
    current = alist[left]
    j = left

    for i in range(j + 1, right + 1):
        if alist[i] < current:
            alist[j + 1], alist[i] = alist[i], alist[j + 1]
            j += 1
    alist[j], alist[left] = alist[left], alist[j]

    return j


def quickSort(alist):
    alist = __quickSort(alist, 0, len(alist) - 1)
    return alist


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = quickSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = quickSort(a)
    for w in a:
        print(w)

    # for w in nums:
    #     print(w)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=0, number=5000)
    nums = quickSort(nums)
    time_end = time.time()
    print('Quick sort totally cost', time_end - time_start)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=0, number=5000)
    nums = insertionSort(nums)
    time_end = time.time()
    print('Insertion sort totally cost', time_end - time_start)
