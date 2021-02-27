# -*- coding:utf-8 -*-
# @Time : 2021/2/27 5:31 下午
# @Author : huichuan LI
# @File : test.py
# @Software: PyCharm

import time
from SortHelper import SortHelper
from LSDSort import LSDSort

n = 1000000
w = 2

arr = SortHelper().generateRandomStringArray(n, w)
arr1 = arr.copy()
time_start = time.time()
LSDSort(arr, w).sort()

time_end = time.time()
print('time cost', time_end - time_start, 's')

time_start = time.time()
arr1.sort()
time_end = time.time()
print('time cost', time_end - time_start, 's')
