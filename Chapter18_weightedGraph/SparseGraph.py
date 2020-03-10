from Edge import Edge


class SparseGraph:
    def __init__(self, n, directed=False):
        self.n = n  # number of vertex
        self.m = 0  # number of edge
        self.directed = directed
        self.graph = [[] for i in range(n)]

    def __str__(self):
        for index, line in enumerate(self.graph):
            print('Vertx {}:  '.format(index), end='')
            for ele in line:
                print(ele, end='')
            print(' ')
        return ''  # __str__必须要返回字符串，否则报错。。。

    def V(self):
        return self.n

    def E(self):
        return self.m

    def addEdge(self, v, w, weight):
        if 0 <= v < self.n and 0 <= w < self.n:
            if self.hasEdge(v, w):
                return
            self.graph[v].append(Edge(v, w, weight))
            if v != w and self.directed is False:
                self.graph[w].append(Edge(v, w, weight))
            self.m += 1
        else:
            raise Exception('Vertex not in the graph')

    # O(ns)
    def hasEdge(self, v, w):
        if 0 <= v < self.n and 0 <= w < self.n:
            for ele in self.graph[v]:
                if ele.w() == w:
                    return True
            return False
        else:
            raise Exception('Vertex not in the graph')

    def __iter__(self):
        return iter(range(self.m))

    def __getitem__(self, item):
        return iter(self.graph[item])
