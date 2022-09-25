# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7() - 1
            b = rand7() - 1
            t = a * 7 + b
            if t >= 40:
                continue
            return t % 10 + 1
