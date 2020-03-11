class Edge:
    def __init__(self, a=None, b=None, weight=0):
        self.a = a
        self.b = b
        self.weight = weight

    def v(self):
        return self.a

    def w(self):
        return self.b

    def wt(self):
        return self.weight

    def other(self, x):
        assert x == self.b or x == self.a
        return self.b if x == self.a else self.a

    def __le__(self, other):
        return self.weight < other.wt()

    def __eq__(self, other):
        if other == -1:
            return False
        return self.weight == other.wt()

    def __gt__(self, other):
        return self.weight > other.wt()

    def __str__(self):
        print('({} -> {} weight:{}) '.format(self.a, self.b, self.weight), end='')
        return ''


if __name__ == "__main__":
    e = Edge(1, 2, 3)
    e2 = Edge(1, 2, 4)
    if e > e2:
        print(e)
    else:
        print(e2)