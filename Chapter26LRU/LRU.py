# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:11
# @Author : huichuan LI
# @File : LRU.py
# @Software: PyCharm
class Node:
    def __init__(self, pre, next, key, value):
        self.pre = pre
        self.value = value
        self.key = key
        self.next = next


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentSize = 0
        self.head = Node(None, None, None, None)
        self.tail = self.head
        self.datas = {}

    def get(self, key):
        # 获取节点
        if key not in self.datas.keys():
            return None
        node = self.datas[key]
        if node is None:
            return None
        elif node.key == self.tail.key:
            return self.tail.value
        # 后一个节点
        nextNode = node.next
        # 前面一个节点
        prevNode = node.pre
        # 如果是第一个节点
        if node.key == self.head.key:
            nextNode.pre = None
            self.head = nextNode
        else:
            # 从链表移除
            prevNode.next = nextNode
            nextNode.pre = prevNode
        # 拼接到链表的尾部
        node.pre = self.tail
        self.tail.next = node
        self.tail = node
        self.tail.next = None
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
            del self.datas[self.head.key]
            self.head = self.head.next
            self.head.pre = None
        elif self.currentSize < self.capacity:
            if self.currentSize == 0:
                self.head = node
            self.currentSize += 1


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 返回1
    cache.put(3, 3)  # 该操作会使得key2作废
    print(cache.get(2))  # 返回 - 1(未找到)
    cache.put(4, 4)  # 该操作会使得key1作废
    print(cache.get(1))  # 返回 - 1(未找到)
    print(cache.get(3))  # 返回 - 1(未找到)
    print(cache.get(4))  # 返回4
