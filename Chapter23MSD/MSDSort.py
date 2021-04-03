# -*- coding:utf-8 -*-
# @Time : 2021/4/3 5:27 下午
# @Author : huichuan LI
# @File : MSDSort.py
# @Software: PyCharm
class MSDSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._sort(0, len(self.arr) - 1, 0)
        return self.arr

    def _sort(self, left, right, r):
        if left >= right:
            return
        R = 256
        cnt = [0] * (R + 1)
        index = [0] * (R + 2)
        temp = [None] * (right - left + 1)

        for elem in self.arr[left:right + 1]:
            if len(elem) <= r:
                cnt[0] += 1
            else:
                cnt[ord(elem[r]) + 1] += 1

        for i in range(R + 1):
            index[i + 1] = index[i] + cnt[i]

        for elem in self.arr[left:right + 1]:
            p = 0 if len(elem) <= r else ord(elem[r]) + 1
            temp[index[p]] = elem
            index[p] += 1

        for i in range(left, right + 1):
            self.arr[i] = temp[i - left]

        for elem in range(1, R + 1):
            self._sort(left + index[elem], left + index[elem + 1] - 1, r + 1)
