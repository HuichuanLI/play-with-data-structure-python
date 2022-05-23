# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:43
# @Author : huichuan LI
# @File : DifferentChar.py
# @Software: PyCharm
class DifferentChar:
    def findDifferentChar(sefl, a, b):
        ret = 0
        for i in a:
            ret ^= ord(i)
        for i in b:
            ret ^= ord(i)
        return chr(ret)


if __name__ == '__main__':
    differentChar = DifferentChar()
    print(differentChar.findDifferentChar("lasda", "daldas"))
