# -*- coding:utf-8 -*-
# @Time : 2022/6/4 17:53
# @Author : huichuan LI
# @File : HuffmanTree.py
# @Software: PyCharm
import collections

try:
    import Queue as Q  # python version < 3.0
except ImportError:
    import queue as Q  # python3.*


class Tree:
    root = None

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root


# 节点（实现 Comparable可排序）
class Node:
    chars = ""
    # 字符出现的频率
    frequence = 0
    # 父节点
    parent = None
    # 左节点
    left = None
    # 右节点
    right = None

    def __lt__(self, other):
        return self.frequence < other.frequence

    # 叶子节点
    def isLeaf(self):
        return len(self.chars) == 1

    # 根节点
    def isRoot(self):
        return self.parent is None

    # 是否是左节点
    def isLeftChild(self):
        return self.parent is not None and self == self.parent.left


class HuffmanTree:
    def __init__(self, frequenceMap):
        if str is None or len(str) == 0:
            return ""
        # 叶子节点
        leafs = []
        # 建树
        self.buildTree(frequenceMap, leafs)
        # 编码之后的信息，每个字符对应二进制
        self.binaryMap = self.buildBinaryInfo(leafs)

    def encode(self, str):
        # 拼接起来
        buffer = ""
        print(self.binaryMap)
        for i in range(0, len(str)):
            buffer = buffer + self.binaryMap[str[i]]
        return buffer

    # 1011000111
    def decode(self, binary, frequenceMap):
        if binary is None or len(binary) == 0:
            return ""
        binaryList = collections.deque()
        size = len(binary)
        # 转列表
        for i in range(0, len(binary)):
            binaryList.append(binary[i])
        leafs = []
        # 重建树
        tree = self.buildTree(frequenceMap, leafs)
        buffer = ""
        # 只要还有二进制字符
        while len(binaryList) > 0:
            # 回到根节点
            node = tree.root
            # 只要不是叶子节点，就一直循环，到叶子节点结束
            first = True
            while not node.isLeaf() or first:
                # 移除第一个二进制字符
                c = binaryList.popleft()
                if c == '0':
                    # 左子树
                    node = node.left
                else:
                    # 右子树
                    node = node.right
                first = False
            # 添加当前节点的字符
            buffer = buffer + node.chars
            # 转字符串
        return buffer

    # 统计字符出现的次数/频率
    @classmethod
    def getFrequency(cls, chars):
        map = {}
        for i in range(len(chars)):
            c = chars[i]
            # 已经出现过
            if c in map:
                # 频次加一
                map[c] = map[c] + 1
            else:
                # 首次出现，频次为 1
                map[c] = 1
        return map

    # 打印
    @classmethod
    def printFrequency(cls, frequencyMap):
        for key in frequencyMap.keys():
            print(key, " ", frequencyMap[key])

    # 对每个字符进行编码，也就是按照二进制来匹配
    def buildBinaryInfo(self, leafs):
        binaryMap = {}
        for i in range(len(leafs)):
            node = leafs[i]
            # 获取节点的第一个字符（其实叶子节点只有一个字符）
            c = node.chars[0]
            binary = ""
            # 暂存当前节点
            tempNode = node
            # 从叶子节点，开始往上，到根节点
            first = True
            while tempNode.parent is not None or first:
                # 如果是左节点，则是 0
                if tempNode.isLeftChild():
                    binary = "0" + binary
                else:
                    # 右节点，是 1
                    binary = "1" + binary
                # 到上一层
                tempNode = tempNode.parent
                first = False
                # 存储起来
            binaryMap[c] = binary
        return binaryMap

    # 按照出现频率建树
    def buildTree(self, frequencyMap, leafs):
        # 转字符数组
        keys = frequencyMap.keys()

        # 初始化节点加到优先队列，频率高的在前面
        queue = Q.PriorityQueue()

        for c in keys:
            node = Node()
            # 字符
            node.chars = c
            # 出现频率
            node.frequence = frequencyMap[c]
            # 添加到队列
            queue.put(node)
            # 添加到叶子节点
            leafs.append(node)
        while queue.qsize() > 1:
            # 弹出两个最低频的接点
            node1 = queue.get()
            node2 = queue.get()
            # 合成新的节点
            parent = Node()
            # 字符串合并
            parent.chars = node1.chars + node2.chars
            # 频率合并
            parent.frequence = node1.frequence + node2.frequence
            parent.left = node1
            parent.right = node2

            node1.parent = parent
            node2.parent = parent
            queue.put(parent)
        tree = Tree()
        # 最后一个是根节点
        tree.root = queue.get()
        return tree


if __name__ == '__main__':
    str = "Hello"
    print("原字符串：", str)
    # 出现频率统计
    frequenceMap = HuffmanTree.getFrequency(list(str))
    HuffmanTree.printFrequency(frequenceMap)
    ht = HuffmanTree(frequenceMap)
    # 编码二进制字符串
    binary = ht.encode(str)
    # 解码
    decode = ht.decode(binary, frequenceMap)
    print("编码后二进制：", binary)
    print("解压字符串：", decode)
    print("长度变化：", len(bytes(str, encoding='utf-8')) * 8, " ===> ", len(binary))
