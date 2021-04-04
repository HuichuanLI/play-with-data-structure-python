# -*- coding:utf-8 -*-
# @Time : 2021/4/4 11:15 上午
# @Author : huichuan LI
# @File : BucketSort.py
# @Software: PyCharm

class BucketSort:
    def __init__(self, arr, B):
        if B <= 1:
            raise Exception("B must be larger than 1")
        self.arr = arr
        self.B = B

    def sort(self):
        temp = [0] * len(self.arr)
        self._sort(0, len(self.arr) - 1, self.B, temp)
        return self.arr


    def _sort(self, left, right, B, temp):
        if left >= right:
            return
        maxV = max(self.arr[left:right + 1])
        minV = min(self.arr[left:right + 1])

        if maxV == minV:
            return

        cnt = [0] * (B)
        index = [0] * (B + 1)
        d = (maxV - minV + 1) // B + (1 if (maxV - minV + 1) % B > 0 else 0)

        for elem in self.arr[left:right + 1]:
            cnt[(elem - minV) // d] += 1

        for i in range(B):
            index[i + 1] = index[i] + cnt[i]

        for elem in self.arr[left:right + 1]:
            p = (elem - minV) // d
            temp[left + index[p]] = elem
            index[p] += 1

        for i in range(left, right + 1):
            self.arr[i] = temp[i]

        self._sort(left, left + index[0] - 1, B, temp)
        for elem in range(B):
            self._sort(left + index[elem], left + index[elem + 1] - 1, B, temp)
