class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [0] * len(s)
        self.getLps(s, res)
        print(res)
        return s[0:res[-1]]

    def getLps(self, s, res):
        res[0] = 0
        for i in range(1, len(s)):
            a = res[i - 1]
            while (a > 0 and s[i] != s[a]):
                a = res[a - 1]
            if s[i] == s[a]:
                res[i] = a + 1

        return res
