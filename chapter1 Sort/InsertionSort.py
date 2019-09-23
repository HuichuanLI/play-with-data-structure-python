from SortTestHelper import RandomArray
import time


def insertionSort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                break
    return alist


if __name__ == "__main__":
    time_start = time.time()
    
    nums = RandomArray()
    nums = insertionSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = insertionSort(a)
    for w in a:
        print(w)
    # for w in nums:
    #     print(w)
