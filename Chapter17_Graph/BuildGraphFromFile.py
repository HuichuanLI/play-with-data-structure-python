# build Graph
import re
from DenseGraph import DenseGraph
from SparseGraph import SparseGraph


# 由于我们只需要定义一个函数就可以把数据生成图，所以就不定义成类了
# 并且文件中第一行顶点的数量和边的数量我删掉了，对python来说没意义。
def BuildGraphFromFile(aGraph, filePath):
    graphList = []
    with open(filePath, 'r', encoding='utf-8') as f:
        for line in f:
            graphList.append([int(x) for x in re.split(r'\s+', line.strip())])
    for i in range(len(graphList)):
        aGraph.addEdge(graphList[i][0], graphList[i][1])


# g1 = DenseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
# BuildGraphFromFile(g1, 'testG1.txt')
# print(g1)
#
#
# g1 = SparseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
# BuildGraphFromFile(g1, 'testG1.txt')
# print(g1)
