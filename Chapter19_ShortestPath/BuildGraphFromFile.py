# build Graph
import re
from DenseGraph import DenseGraph
from SparseGraph import SparseGraph


# 由于我们只需要定义一个函数就可以把数据生成图，所以就不定义成类了
# 并且文件中第一行顶点的数量和边的数量我删掉了，对python来说没意义。
def buildGraphFromFile(aGraph, filePath):
    graphList = []
    hasWeight = False
    with open(filePath, 'r', encoding='utf-8') as f:
        for line in f:
            graphList.append([float(x) for x in re.split(r'\s+', line.strip())])
    if len(graphList[0]) > 2:
        hasWeight = True
    for i in range(len(graphList)):
        if hasWeight:
            aGraph.addEdge(int(graphList[i][0]), int(graphList[i][1]), graphList[i][2])
        else:
            aGraph.addEdge(int(graphList[i][0]), int(graphList[i][1]))


if __name__ == "__main__":
    g1 = DenseGraph(8)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    buildGraphFromFile(g1, 'testG1.txt')
    print(g1)

    # g1 = SparseGraph(8)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    # buildGraphFromFile(g1, 'testG1.txt')
    # print(g1)
