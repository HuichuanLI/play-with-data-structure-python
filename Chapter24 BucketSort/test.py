# -*- coding:utf-8 -*-
# @Time : 2021/2/27 5:31 下午
# @Author : huichuan LI
# @File : test.py
# @Software: PyCharm

from BucketSort import BucketSort

arr = list(range(10000, 1, -1))

print(BucketSort(arr, 3).sort())
