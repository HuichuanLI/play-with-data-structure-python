from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = dict(Counter(s))
        for index, elem in enumerate(s):
            if arr[elem] == 1:
                return index
        return -1


if __name__ == "__main__":
    Solution().firstUniqChar("leetcode")
