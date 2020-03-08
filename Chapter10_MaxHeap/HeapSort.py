# 原地的堆排序
from Array import Array
from MaxHeap import MaxHeap
from time import time
import random


def HeapSort3(nums, n):
    for i in range((n - 1) // 2, -1, -1):
        __shiftDown(nums, i, len(nums))
    for i in range(n - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        __shiftDown(nums, 0, i)

    return nums


def __shiftDown(nums, index, n):
    if index < 0:
        raise ValueError("index should be positive")
    current_value = nums[index]
    while 2 * index + 1 < n:
        i = 2 * index + 1
        if 2 * index + 2 < n and nums[2 * index + 1] < nums[2 * index + 2]:
            i = 2 * index + 2
        if nums[i] >= current_value:
            nums[index] = nums[i]
            index = i
        else:
            break
    nums[index] = current_value


if __name__ == "__main__":
    start_time = time()
    list = [random.randint(-300, 300) for _ in range(10000)]
    heap = MaxHeap()
    for ele in list:
        heap.add(ele)
    for _ in range(len(list)):
        ele = heap.extract_max()

    print('Total time: {} seconds for HeapSort version 1'.format(time() - start_time))

    start_time = time()
    list = [random.randint(-300, 300) for _ in range(10000)]
    heap = MaxHeap(Array(list),10000)
    for _ in range(len(list)):
        ele = heap.extract_max()

    print('Total time: {} seconds for HeapSort version 2'.format(time() - start_time))

    start_time = time()
    list = [random.randint(-300, 300) for _ in range(10000)]
    nums = HeapSort3(list, len(list))
    print('Total time: {} seconds for HeapSort version 3'.format(time() - start_time))
