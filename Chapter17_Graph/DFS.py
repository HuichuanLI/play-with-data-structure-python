from BuildGraphFromFile import BuildGraphFromFile
from SparseGraph import SparseGraph
from DenseGraph import DenseGraph


class dfs:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [0] * self.graph.V()
        self.count = 0
        # print(self.graph, self.visited)
        for i in self.graph:
            if not self.visited[i]:
                self._dfs(i)
                self.count += 1

    def _dfs(self, index):
        self.visited[index] = 1
        for w in self.graph[index]:
            if not self.visited[w]:
                self._dfs(w)

    def _ccount(self):
        return self.count


if __name__ == "__main__":
    g1 = SparseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    BuildGraphFromFile(g1, 'testG1.txt')

    df = dfs(g1)
    print(df._ccount())
    # for elem in g1[0]:
    #     print(elem)

    print("-----")
    g2 = DenseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    BuildGraphFromFile(g2, 'testG1.txt')

    # for elem in g2[0]:
    #     print(elem)
    df = dfs(g2)
    print(df._ccount())
