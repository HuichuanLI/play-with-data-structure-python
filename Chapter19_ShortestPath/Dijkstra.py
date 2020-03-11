from IndexHeap import IndexHeap
from SparseGraph import SparseGraph
from BuildGraphFromFile import buildGraphFromFile


class Dijstra:
    def __init__(self, graph, s):
        self.g = graph
        self.s = s
        self.visited = [0] * self.g.V()
        self.distTo = [0] * self.g.V()
        self.path = [None] * self.g.V()
        self.heap = IndexHeap(self.g.V())
        for i in range(self.g.V()):
            self.heap.add(i, 10000)

        self.distTo[s] = 0
        self.visited[s] = 1
        self.heap.add(s, self.distTo[s])
        while not self.heap.isEmpty():
            v = self.heap.extractMinIndex()

            self.visited[v] = 1
            for adj in self.g[v]:
                w = adj.other(v)
                # 松弛操作
                if not self.visited[w]:
                    if not self.path[w] or self.distTo[v] + adj.wt() < self.distTo[w]:
                        self.distTo[w] = self.distTo[v] + adj.wt()
                        self.path[w] = adj
                        if self.heap.contains(w):
                            self.heap.change(w, self.distTo[w])
                        else:
                            self.heap.add(w, self.distTo[w])

    def shortestWeight(self, w):
        return self.distTo[w]

    def hasPath(self, w):
        return self.visited[w] == 1

    def ShortestPath(self, w):
        if not self.hasPath(w):
            return []
        result = [w]
        while self.path[w].v():
            result.append(self.path[w].v())
            w = self.path[w].v()
        result.append(self.s)
        return list(reversed(result))

    def showPath(self, w):
        if not self.hasPath(w):
            return []
        return "->".join(map(lambda ele: str(ele), self.ShortestPath(w)))


if __name__ == "__main__":
    g = SparseGraph(5)
    buildGraphFromFile(g, 'testG1.txt')
    # print(g)
    Dij = Dijstra(g, 0)

    for i in range(1, 5):
        print(Dij.showPath(i), Dij.shortestWeight(i))
