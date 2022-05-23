# -*- coding:utf-8 -*-
# @Time : 2022/5/23 22:01
# @Author : huichuan LI
# @File : KMP.py
# @Software: PyCharm
class Solution:
    def getNext(self, next, patterns):
        j = 0
        k = -1
        next[0] = -1
        while j < len(patterns) - 1:
            if k == -1 or patterns[j] == patterns[k]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]

    def kmp(self, A, B):
        # next数组，保存已匹配的字符串的最长公共前后缀
        next = [0] * (len(B))
        self.getNext(next, B)
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if j == -1 or A[i] == B[j]:
                i += 1
                j += 1
            else:
                # 模式串上的指针回溯到j位置
                j = next[j]
        if j == len(B):
            return i - j
        else:
            return -1

    def isMatch(self, A, B):
        lenOfA = len(A)
        lenOfB = len(B)
        if lenOfA != lenOfB:
            return False
        bigStr = A + A
        # 判断主串中是否包含模式串
        if self.kmp(bigStr, B) != -1:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("1234", "3412"))
    print(solution.isMatch("1234", "4312"))
    print(solution.isMatch("ABCBD", "BDABC"))
