class Solution(object):
    # solution 1 - 时间复杂度: O(N)- 空间复杂度: O(N)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = '([{'
        rightP = ')]}'
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []
    # - 时间复杂度: O(N^2)- 空间复杂度: O(N)
    class Solution:
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            while '[]' in s or '()' in s or '{}' in s:
                s = s.replace('[]', '').replace('()', '').replace('{}', '')
            return len(s) == 0
