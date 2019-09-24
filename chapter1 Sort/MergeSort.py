from SortTestHelper import RandomArray, NearlyOrderArray
from SelectionSort import selectionSort
import time


#
def __mergeSort(alist, left, right):
    if left >= right:
        return
    # 注意 left + right 可能比较大
    mid = int((left + right) / 2)
    __mergeSort(alist, left, mid)
    __mergeSort(alist, mid + 1, right)
    return __merge(alist, left, mid, right)


def __merge(alist, left, mid, right):
    alist2 = []
    for i in range(left, right + 1):
        alist2.append(alist[i])
    i = left
    j = mid + 1
    for k in range(left, right + 1):
        if i > mid:
            alist[k] = alist2[j - left]
            j += 1
        elif j > right:
            alist[k] = alist2[i - left]
            i += 1

        elif alist2[i - left] < alist2[j - left]:
            alist[k] = alist2[i - left]
            i += 1
        else:
            alist[k] = alist2[j - left]
            j += 1
    return alist


def MergeSort(alist):
    alist = __mergeSort(alist, 0, len(alist) - 1)
    return alist


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = MergeSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = MergeSort(a)
    for w in a:
        print(w)

    # for w in nums:
    #     print(w)

    time_start = time.time()

    nums = NearlyOrderArray(swap_times=100, number=10000)
    nums = MergeSort(nums)
    time_end = time.time()
    print('Bubble totally cost', time_end - time_start)

    time_start = time.time()

    # nums = NearlyOrderArray(swap_times=100, number=10000)
    # nums = BubbleSort(nums)
    # time_end = time.time()
    # print('Selection totally cost', time_end - time_start)
