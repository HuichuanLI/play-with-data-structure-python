from queue import PriorityQueue
from UnionFind import UnionFind6
from SparseGraph import SparseGraph
from DenseGraph import DenseGraph
from BuildGraphFromFile import buildGraphFromFile
from Edge import Edge


class kruskalMST:
    def __init__(self, graph):
        self.g = graph
        self.pq = PriorityQueue()
        self.result = []
        for i in range(self.g.V()):
            for elem in self.g[i]:
                if isinstance(elem, Edge) and elem.v() < elem.w():
                    self.pq.put(elem)

        self.uf = UnionFind6(self.g.V())
        while not self.pq.empty() and len(self.result) < self.g.V() - 1:
            ele = self.pq.get()
            if self.uf.is_connected(ele.v(), ele.w()):
                continue
            self.result.append(ele)
            self.uf.union_elements(ele.v(), ele.w())
        self.weights = 0

        for w in self.result:
            self.weights += w.wt()

    def mstEdges(self):
        return self.result

    def weights(self):
        return self.weights


if __name__ == "__main__":
    g1 = SparseGraph(8)
    buildGraphFromFile(g1, 'testG1.txt')
    # print(g1)
    df = kruskalMST(g1)
    # print("lalla")
    for w in df.mstEdges():
        print(w)
    print(df.weights)
