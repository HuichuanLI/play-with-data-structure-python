import math


class NumArray:
    def __init__(self, data):
        self.data = data
        self.N = len(data)

        self.B = int(math.sqrt(len(data)))
        self.Bn = self.N // self.B + 1
        self.blocks = [0] * self.Bn

        for i in range(self.N):
            self.blocks[i // self.B] += data[i]

    def update(self, i, val):
        if i < 0 or i > self.N:
            return
        b = i // self.B
        self.blocks[b] -= self.data[i]
        self.blocks[b] += val
        self.data[i] = val

    def sumRange(self, i, j):
        if i < 0 or i >= self.N or j < 0 or j >= self.N or i > j:
            return 0

        bstart, bend = i // self.B, j // self.B
        res = 0
        if bstart == bend:
            for index in range(i, j + 1):
                res += self.data[index]
            return res
        else:
            for index in range(i, (bstart + 1) * self.B):
                res += self.data[index]
            for index in range(bend * self.B, j + 1):
                res += self.data[index]
            for index in range(bstart + 1, bend):
                res += self.blocks[index]
            return res
