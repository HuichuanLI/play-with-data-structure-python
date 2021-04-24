# -*- coding:utf-8 -*-
# @Time : 2021/4/24 3:49 下午
# @Author : huichuan LI
# @File : SubStringMatch.py
# @Software: PyCharm
class SubStringMatch:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def bruteforec(self):
        if len(self.s) < len(self.t):
            return -1

        for i in range(0, len(self.s) - len(self.t) + 1):
            # if self.s[i:i + len(self.t) + 1] == self.t:
            #     return i
            for j in range(len(self.t)):
                if self.s[i + j] != self.t[j]:
                    break
            if j == len(self.t) - 1 and self.s[i + j] == self.t[j]:
                return i
        return -1


if __name__ == "__main__":
    s1 = "hello, this is lihuichuan."
    s2 = "lihuichuan"
    print(SubStringMatch(s1, s2).bruteforec())

    n = 1000000
    m = 10000
    s = ""
    for i in range(n):
        s += "a"
    s3 = ""
    for j in range(m - 1):
        s3 += "a"
    s3 += "b"
    # print(s, s3)
    print(SubStringMatch(s, s3).bruteforec())
