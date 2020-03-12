from IndexHeap import IndexHeap
from SparseGraph import SparseGraph
from BuildGraphFromFile import buildGraphFromFile
from Edge import Edge


class BellmanFord:
    def __init__(self, graph, s):
        self.g = graph
        self.s = s
        self.g = graph
        self.s = s
        self.distTo = [1000000] * self.g.V()
        self.path = [-1] * self.g.V()
        self.hasNegativeCycle = False
        self.distTo[s] = 0
        self.path[s] = s
        # Bellman-Ford
        for _ in range(1, self.g.V()):
            for i in range(self.g.V()):
                # 松弛操作
                for adj in self.g[i]:

                    if not isinstance(self.path[i], Edge) or self.distTo[i] + adj.wt() < self.distTo[adj.w()]:
                        self.distTo[adj.w()] = self.distTo[i] + adj.wt()
                        self.path[adj.w()] = adj
        self.hasNegativeCycle = self._hasnegativeCYcle()

    def _hasnegativeCYcle(self):
        for i in range(self.g.V()):
            for adj in self.g[i]:
                if not isinstance(self.path[i], Edge) or self.distTo[i] + adj.wt() < self.distTo[adj.w()]:
                    if i == self.s:
                        continue
                    return True
        return False

    def shortestWeight(self, w):
        return self.distTo[w]

    def hasPath(self, w):
        return self.distTo[w] != -1

    def negativeCycle(self):
        return self.hasNegativeCycle

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
        if not self.hasPath(w) or self.negativeCycle():
            return []
        return "->".join(map(lambda ele: str(ele), self.ShortestPath(w)))


if __name__ == "__main__":
    g = SparseGraph(5, True)
    buildGraphFromFile(g, 'testG2.txt')
    # print(g)
    Dij = BellmanFord(g, 0)
    print(Dij.distTo)

    for i in range(1, 5):
        print(Dij.showPath(i), Dij.shortestWeight(i))
    print(Dij.hasNegativeCycle)
