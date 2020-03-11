from queue import PriorityQueue
import heapq
from BuildGraphFromFile import buildGraphFromFile
from SparseGraph import SparseGraph
from DenseGraph import DenseGraph
from IndexHeap import IndexHeap
from Edge import Edge


class PrimMST:
    def __init__(self, g):
        self.graph = g
        self.pq = IndexHeap(self.graph.V())
        for i in range(self.graph.V()):
            self.pq.add(i, 1000000)
        self.edgeTo = [-1] * self.graph.V()

        self.marked = [0] * self.graph.V()
        self.result = []
        self.weights = 0
        self._lazyPrimMST(0)
        while not self.pq.isEmpty():
            v = self.pq.extractMinIndex()
            self.result.append(self.edgeTo[v])
            self._lazyPrimMST(v)
        for w in self.result:
            if w != -1:
                self.weights += w.wt()

    def mstEdges(self):
        return self.result

    def weights(self):
        return self.weights

    def _lazyPrimMST(self, index):
        # assert self.marked[index] == 0
        self.marked[index] = 1
        for w in self.graph[index]:
            v = w.other(index)
            if self.marked[v] == 0:
                if not isinstance(self.edgeTo[v], Edge) and self.edgeTo[v] == -1:
                    self.pq.change(v, w.wt())
                    self.edgeTo[v] = w

                elif isinstance(self.edgeTo[v], Edge) and self.edgeTo[v] > w:
                    self.pq.change(v, w.wt())
                    self.edgeTo[v] = w


# 算法 时间复杂度 O(V+E)logE == O(E)logE

if __name__ == "__main__":
    g1 = SparseGraph(8)
    buildGraphFromFile(g1, 'testG1.txt')

    df = PrimMST(g1)

    for w in df.mstEdges():
        print(w)
    print(df.weights)
