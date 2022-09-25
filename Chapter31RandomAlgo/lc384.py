import random
import copy


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = copy.copy(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        data = copy.copy(self.nums)
        for i in range(len(data) - 1, -1, -1):
            j = int(random.random() * (i + 1))
            temp = data[j]
            data[j] = data[i]
            data[i] = temp
        return data
