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

    def getLps(self, s, res):
        res[0] = 0
        for i in range(1, len(s)):
            a = res[i - 1]
            while (a > 0 and s[i] != s[a]):
                a = res[a - 1]
            if s[i] == s[a]:
                res[i] = a + 1

    def kmp(self):
        if len(self.s) < len(self.t):
            return -1
        res = len(self.t) * [0]
        self.getLps(self.t, res)
        i = 0
        j = 0
        while (i < len(self.s)):
            if (self.s[i] == self.t[j]):
                i += 1
                j += 1
                if (j == len(self.t)):
                    return i - len(self.t)
            elif (j > 0):
                j = res[j - 1]
            else:
                i += 1

        return -1


if __name__ == "__main__":
    s1 = "hello, this is lihuichuan."
    s2 = "lihuichuan"
    print(SubStringMatch(s1, s2).kmp())

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
    print(SubStringMatch(s, s3).kmp())
