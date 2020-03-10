from BuildGraphFromFile import BuildGraphFromFile
from SparseGraph import SparseGraph
from DenseGraph import DenseGraph


class dfs:
    def __init__(self, graph, s):
        self.graph = graph
        self.visited = [0] * self.graph.V()
        self.path = [-1] * self.graph.V()
        self.s = s
        # print(self.graph, self.visited)
        self._dfs(s)
        self.path[s] = -1

    def _dfs(self, index):
        self.visited[index] = 1
        for w in self.graph[index]:
            if not self.visited[w]:
                self.path[w] = index
                self._dfs(w)

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
        return "->".join(list(map(lambda ele:str(ele),self.pathFrom(w))))


if __name__ == "__main__":
    g1 = SparseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    BuildGraphFromFile(g1, 'testG2.txt')

    df = dfs(g1, 0)
    print(df.showPath(6))
    # for elem in g1[0]:
    #     print(elem)

    # print("-----")
    # g2 = DenseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    # BuildGraphFromFile(g2, 'testG1.txt')

    # for elem in g2[0]:
    #     print(elem)
    # df = dfs(g2)
    # print(df._ccount())
