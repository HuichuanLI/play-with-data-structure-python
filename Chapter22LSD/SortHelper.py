# -*- coding:utf-8 -*-
# @Time : 2021/2/27 5:23 下午
# @Author : huichuan LI
# @File : SortHelper.py
# @Software: PyCharm

import random


class SortHelper:
    def generateRandomStringArray(self, n, w):
        arr = []
        for i in range(n):
            temp = ""
            for j in range(w):
                temp += chr(random.randint(33, 93))
            arr.append(temp)
        return arr


