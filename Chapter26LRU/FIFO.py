# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:00
# @Author : huichuan LI
# @File : FIFO.py
# @Software: PyCharm
class Node:
    def __init__(self, pre, next, key, value):
        self.pre = pre
        self.value = value
        self.key = key
        self.neext = next


class FIFOCache:
    def __init__(self, capacity):
        # 容量
        self.capacity = capacity
        # 当前的大小为0
        self.currentSize = 0
        # 头节点初始化
        self.head = Node(None, None, None, None)
        self.tail = self.head
        # hash容器
        self.datas = {}

    def get(self, key):
        # 获取节点
        node = self.datas.get(key)
        if node is None:
            return None
        else:
            return node.value

    def put(self, key, value):
        # 如果已经包含
        if key in self.datas.keys():
            return
        # 新建节点，拼接到链表的尾部
        node = Node(self.tail, None, key, value)
        self.tail.next = node
        self.datas[key] = node
        self.tail = node

        # 空间超出
        if self.currentSize == self.capacity:
            # 移除头结点
            self.datas.pop(self.head.key)
            self.head = self.head.next
            self.head.pre = None
        elif self.currentSize < self.capacity:
            if self.currentSize == 0:
                self.head = node
            self.currentSize += 1


if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    # 删除1，加入3
    cache.put(3, 3)
    # 1被删除了
    print(cache.get(1))
    # 打印2
    print(cache.get(2))
    # 打印3
    print(cache.get(3))
