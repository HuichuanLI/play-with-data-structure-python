# -*- coding:utf-8 -*-
# @Time : 2022/5/23 22:01
# @Author : huichuan LI
# @File : RabinKarp.py
# @Software: PyCharm
import sys


class Solution:
    def isMatch(self, pattern, source):
        # 计算模式串的hash值
        hash = self.hashValue(pattern)
        pLen = len(pattern)
        i = 0
        while i + pLen <= len(source):
            # 计算子串的 hash 值
            tempHash = self.hashValue(source[i:i + pLen])
            if hash == tempHash:
                return True
            i += 1
        return False

    def hashValue(self, str):
        hash = 0
        for i in range(0, len(str)):
            hash = 31 * hash + ord(str[i])
        return hash % sys.maxsize


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("ABC", "ABABDABCD"))
