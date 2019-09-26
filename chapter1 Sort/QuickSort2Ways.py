from SortTestHelper import RandomArray, NearlyOrderArray
from SelectionSort import selectionSort
from InsertionSort import insertionSort, insertionSortRange
import time

import sys
import random

sys.setrecursionlimit(1000000)


#
def __quickSort(alist, left, right):
    if right - left <= 15:
        return insertionSortRange(alist, left, right)
    p = None
    p = __partion(alist, left, right)
    __quickSort(alist, left, p - 1)
    __quickSort(alist, p + 1, right)
    return alist


# 对 arr[l,r] 进行partiton 操做
def __partion(alist, left, right):
    index = random.randint(left, right)
    current = alist[index]
    alist[left], alist[index] = alist[index], alist[left]
    i = left + 1
    j = right
    while True:
        while alist[i] < current and i <= right:
            i += 1
        while alist[j] > current and j > left:
            j -= 1
        if i > j: break
        alist[i], alist[j] = alist[j], alist[i]
        i += 1
        j -= 1

    alist[left], alist[j] = alist[j], alist[left]
    return j


def quickSort(alist_1):
    alist_1 = __quickSort(alist_1, 0, len(alist_1) - 1)
    return alist_1


if __name__ == "__main__":
    # time_start = time.time()
    #
    # nums = RandomArray()
    # nums = quickSort(nums)
    # time_end = time.time()
    # print('totally cost', time_end - time_start)

    alist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    alist = quickSort(alist)
    for w in alist:
        print(w)

    # for w in nums:
    #     print(w)

    # time_start = time.time()
    #
    # nums = NearlyOrderArray(swap_times=0, number=5000)
    # nums = quickSort(nums)
    # time_end = time.time()
    # print('Quick sort totally cost', time_end - time_start)
    #
    # time_start = time.time()
    #
    # nums = NearlyOrderArray(swap_times=0, number=5000)
    # nums = insertionSort(nums)
    # time_end = time.time()
    # print('Insertion sort totally cost', time_end - time_start)
