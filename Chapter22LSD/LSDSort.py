# -*- coding:utf-8 -*-
# @Time : 2021/2/27 4:27 下午
# @Author : huichuan LI
# @File : LSDSort.py
# @Software: PyCharm


class LSDSort:
    def __init__(self, arr, w):
        self.arr = arr
        self.w = w

    def sort(self):
        arr = self.arr
        for elem in arr:
            if len(elem) != self.w or not isinstance(elem, str):
                raise Exception("elem should be length w")
        R = 256

        for r in range(self.w - 1, -1, -1):
            cnt = [0] * R
            index = [0] * (R + 1)
            temp = [None] * len(arr)

            for elem in arr:
                cnt[ord(elem[r])] += 1

            for i in range(R):
                index[i + 1] = index[i] + cnt[i]
            for elem in arr:
                temp[index[ord(elem[r])]] = elem
                index[ord(elem[r])] += 1

            for i in range(len(arr)):
                arr[i] = temp[i]
        return arr


if __name__ == "__main__":
    arr = ["BCA", "CAB", "ACB", "BAC", "ABC", "CBA"]
    print(LSDSort(arr, 3).sort())
