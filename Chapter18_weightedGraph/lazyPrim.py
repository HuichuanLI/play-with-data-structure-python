from queue import PriorityQueue
import heapq
from BuildGraphFromFile import buildGraphFromFile
from SparseGraph import SparseGraph
from DenseGraph import DenseGraph


class LazyPrimMST:
    def __init__(self, g):
        self.graph = g
        self.pq = PriorityQueue()
        self.marked = [0] * self.graph.V()
        self.result = []
        self.weights = 0
        self._lazyPrimMST(0)
        while not self.pq.empty():
            e = self.pq.get()
            if self.marked[e.v()] == self.marked[e.w()]:
                continue
            self.result.append(e)
            if self.marked[e.v()] == 0:
                self._lazyPrimMST(e.v())
            else:
                self._lazyPrimMST(e.w())
        for w in self.result:
            self.weights += w.wt()

    def mstEdges(self):
        return self.result

    def weights(self):
        return self.weights

    def _lazyPrimMST(self, index):
        assert self.marked[index] == 0
        self.marked[index] = 1
        for w in self.graph[index]:
            if self.marked[w.other(index)] == 0:
                self.pq.put(w)

# 算法 时间复杂度 O(V+E)logE == O(E)logE

if __name__ == "__main__":
    g1 = SparseGraph(8)
    buildGraphFromFile(g1, 'testG1.txt')

    df = LazyPrimMST(g1)

    for w in df.mstEdges():
        print(w)
    print(df.weights)