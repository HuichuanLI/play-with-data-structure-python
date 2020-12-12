import time
from SortTestHelper import RandomArray, NearlyOrderArray


class CountingSort:
    # 能处理取值范围[L,R]范围的技术
    def __init__(self, L, R, nums):
        self.L = L
        self.R = R
        self.cnt = [0] * (R - L + 1)
        self.nums = nums
        self.index = [0] * (R - L + 2)

    def sort(self):
        for elem in self.nums:
            self.cnt[elem - self.L] += 1

        for i in range(self.L, self.R + 1):
            self.index[i - self.L + 1] = self.index[i - self.L] + self.cnt[i - self.L]

        for i in range(self.L, self.R + 1):
            for j in range(self.index[i - self.L], self.index[i + 1 - self.L]):
                self.nums[j] = i
        return self.nums


if __name__ == "__main__":
    time_start = time.time()

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = CountingSort(1, 10, a).sort()
    for w in a:
        print(w)

    time_end = time.time()

    print('Counting  sort totally cost', time_end - time_start)

    nums = NearlyOrderArray(swap_times=0, number=5000)
    nums = CountingSort(0, 5000, nums).sort()

    for w in nums:
        print(w)

    time_end = time.time()
