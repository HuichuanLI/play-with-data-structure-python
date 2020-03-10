from BuildGraphFromFile import BuildGraphFromFile
from SparseGraph import SparseGraph
from DenseGraph import DenseGraph
from collections import deque


class bfs:
    def __init__(self, graph, s):
        self.graph = graph
        self.visited = [0] * self.graph.V()
        self.ord = [-1] * self.graph.V()
        self.path = [-1] * self.graph.V()
        self.s = s
        self.queue = deque()

        self.count = 0
        self._bfs(s)

    def _bfs(self, index):
        self.visited[index] = 1
        self.ord[index] = 0
        self.queue.append(index)
        while len(self.queue) > 0:
            v = self.queue.pop()
            for w in self.graph[v]:
                if self.visited[w] != 1:
                    self.queue.append(w)
                    self.visited[w] = 1
                    self.path[w] = v
                    self.ord[w] = self.ord[v] + 1


    def hasPath(self, w):
        return self.visited[w] == 1

    def pathFrom(self, w):
        if not self.hasPath(w):
            return []
        else:
            a = []
            while self.path[w] != -1:
                a.append(w)
                w = self.path[w]
            a.append(0)
            return list(reversed(a))

    def showPath(self, w):
        return "->".join(list(map(lambda ele: str(ele), self.pathFrom(w))))


if __name__ == "__main__":
    g1 = SparseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    BuildGraphFromFile(g1, 'testG2.txt')

    df = bfs(g1, 0)
    print(df.showPath(4))
