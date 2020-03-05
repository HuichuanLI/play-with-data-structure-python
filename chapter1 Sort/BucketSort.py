# 当每个桶的数据范围为1且数据皆为整数时，桶排序的时间复杂度在所有情况下都是O(n)，因为它是一个线性的排序算法。但是，它的空间需求要视排序数据的范围而定，所以极有可能浪费很多空间。

import time
from SortTestHelper import RandomArray, NearlyOrderArray


def BucketSort(nums):
    minv, maxv = min(nums), max(nums)
    countn = [0] * (maxv - minv + 1)
    result = []
    for i in nums:
        countn[i - minv] += 1
    for i in range(0, len(countn)):
        if countn[i] > 0:
            result += [i + minv] * countn[i]
    return result


if __name__ == "__main__":
    time_start = time.time()

    nums = RandomArray()
    nums = BucketSort(nums)
    time_end = time.time()
    print('totally cost', time_end - time_start)

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = BucketSort(a)
    for w in a:
        print(w)
