from SortTestHelper import RandomArray
import time


def selectionSort(alist):
    for i in range(len(alist)):
        minposition = i
        for j in range(i, len(alist)):
            if alist[minposition] > alist[j]:
                minposition = j
        alist[i], alist[minposition] = alist[minposition], alist[i]
    return alist


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = selectionSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    # for w in nums:
    #     print(w)
