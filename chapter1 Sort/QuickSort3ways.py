import random
from SortTestHelper import RandomArray, NearlyOrderArray
from SelectionSort import selectionSort
from InsertionSort import insertionSort, insertionSortRange
import time


def quickSort3ways(nums):
    _quickSort3Ways(nums, 0, len(nums) - 1)


def _quickSort3Ways(arr, left, right):
    if left >= right:
        return
    index = random.randint(left, right)
    arr[left], arr[index] = arr[index], arr[left]
    cur = arr[left]
    lt = left  # arr[l+1,l] < v
    gt = right + 1  # arr[gt...r] > v
    i = left + 1  # arr[lt+1....i) == v
    while i < gt:
        if arr[i] < cur:
            arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > cur:
            arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
            gt -= 1
        else:
            i += 1
    arr[left], arr[lt] = arr[lt], arr[left]
    _quickSort3Ways(arr, left, lt - 1)
    _quickSort3Ways(arr, gt, right)


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = quickSort3ways(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quickSort3ways(a)
    for w in a:
        print(w)

    # for w in nums:
    #     print(w)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=0, number=5000)
    nums = quickSort3ways(nums)
    time_end = time.time()
    print('Quick sort totally cost', time_end - time_start)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=0, number=5000)
    nums = insertionSort(nums)
    time_end = time.time()
    print('Insertion sort totally cost', time_end - time_start)
