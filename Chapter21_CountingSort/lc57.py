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


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        return CountingSort(0, 2, nums).sort()


