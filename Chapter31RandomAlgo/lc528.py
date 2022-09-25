import random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.presum = [0] * len(w)
        self.sum = 0
        for i in range(1, len(w)):
            self.presum[i] = self.presum[i - 1] + w[i - 1]
        self.sum = self.presum[-1] + w[-1]

    def pickIndex(self):
        """
        :rtype: int
        """

        x = int(random.random()) * self.sum
        left = 0
        right = len(self.sum) - 1
        while (left < right):
            mid = (left + right + 1) // 2
            if self.presum[mid] <= x:
                left = mid
            else:
                mid - 1
        return left

# obj = Solution(w)
# param_1 = obj.pickIndex()
