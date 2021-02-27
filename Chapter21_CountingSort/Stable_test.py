# -*- coding:utf-8 -*-
# @Time : 2021/2/27 2:26 下午
# @Author : huichuan LI
# @File : Stable_test.py
# @Software: PyCharm
import random

from string import ascii_lowercase
from Student import Student

n = 26 * 26 * 26 * 26
students = []
for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
        for c3 in ascii_lowercase:
            for c4 in ascii_lowercase:
                students.append(Student(c1 + c2 + c3 + c4, random.randint(0, 100)))

R = 101
cnt = [0] * R
for elem in students:
    cnt[elem.getScore()] += 1

index = [0] * (R + 1)
for i in range(R):
    index[i + 1] = index[i] + cnt[i]

temp = [None] * n
for elem in students:
    temp[index[elem.getScore()]] = elem
    index[elem.getScore()] += 1


for i in range(1, n):
    if temp[i - 1].getScore() > temp[i].getScore():
        raise Exception("error")

print(temp)