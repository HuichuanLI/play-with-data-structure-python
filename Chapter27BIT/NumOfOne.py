# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:41
# @Author : huichuan LI
# @File : NumOfOne.py
# @Software: PyCharm
class NumOfOne:
    def numberOf1(self, n):
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret


if __name__ == '__main__':
    numOfOne = NumOfOne()
    print(numOfOne.numberOf1(14))
