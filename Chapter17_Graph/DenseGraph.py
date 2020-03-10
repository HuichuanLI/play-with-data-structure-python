class DenseGraph:
    def __init__(self, n, directed=False):
        self.n = n  # number of vertex
        self.m = 0  # number of edge
        self.directed = directed
        self.martix = [[0 for i in range(n)] for i in range(n)]

    def __str__(self):
        for line in self.martix:
            print(str(line))
        return ''  # __str__必须要返回字符串，否则报错。。。

    def V(self):
        return self.n

    def E(self):
        return self.m

    def addEdge(self, v, w):
        if 0 <= v < self.n and 0 <= w < self.n:
            if self.hasEdge(v, w):
                return
            self.martix[v][w] = 1
            if v != w and self.directed is False:
                self.martix[w][v] = 1
            self.m += 1
        else:
            raise Exception('Vertex not in the graph')

    def hasEdge(self, v, w):
        if 0 <= v < self.n and 0 <= w < self.n:
            return self.martix[v][w]
        else:
            raise Exception('Vertex not in the graph')
