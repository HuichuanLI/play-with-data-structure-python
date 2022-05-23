# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:40
# @Author : huichuan LI
# @File : BITadd.py
# @Software: PyCharm
class BitAdd:
    def add(self, num1, num2):
        while (num2 != 0):
            # 进位
            c = (num1 & num2) << 1
            # 不进位加和结果
            num1 = num1 ^ num2
            num2 = c
        return num1


if __name__ == '__main__':
    bitAdd = BitAdd()
    print(bitAdd.add(21, 27))
    print(bitAdd.add(21, -26))
