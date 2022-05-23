# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:47
# @Author : huichuan LI
# @File : HammingDistance.py
# @Software: PyCharm
class HammingDistance:
    def hammingDistance(sefl, x, y):
        return bin(x ^ y).count('1')
        return result;


if __name__ == '__main__':
    hammingDistance = HammingDistance()
    print("汉明距离：", hammingDistance.hammingDistance(83, 53))