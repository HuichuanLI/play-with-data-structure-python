# -*- coding:utf-8 -*-
# @Time : 2021/4/24 11:58 下午
# @Author : huichuan LI
# @File : lc1147.py
# @Software: PyCharm

class Solution:
    def longestDecomposition(self, text: str) -> int:
        return self.solve(s, 0, len(text) - 1)

    def solve(self, s, left, right):
        if left > right:
            return 0
        i = left
        j = right
        while i < j:
            if s[left:i + 1] == s[j:right + 1]:
                return self.solve(s, i + 1, j - 1) + 2
            i += 1
            j -= 1

        return 1
