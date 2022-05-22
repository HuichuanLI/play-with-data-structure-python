# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:01
# @Author : huichuan LI
# @File : LFU.py
# @Software: PyCharm
import collections


class Node:
    def __init__(self, usedCount, lastUsedTime, key, value):
        self.usedCount = usedCount
        self.lastUsedTime = lastUsedTime
        self.key = key
        self.value = value

    def __lt__(self, other):
        # 如果使用次数一样，就按照最后使用时间戳排序
        if self.usedCount != other.usedCount:
            return self.lastUsedTime > other.lastUsedTime
        else:
            return self.usedCount > other.usedCount


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.timeStamp = 0
        self.frequencyNodes = set()

    def get(self, key):
        # 如果不包含，直接返回
        if not key in self.map.keys():
            return None
        # 获取值
        node = self.map.get(key)
        # 删掉旧的值
        self.frequencyNodes.remove(node)
        # 更新使用次数
        node.usedCount += 1
        # 更新最后一次使用的时间
        self.timeStamp += 1
        node.lastUsedTime = self.timeStamp
        # 重新添加
        self.frequencyNodes.add(node)
        # 更新节点的值
        self.map[key] = node
        sorted(self.frequencyNodes)
        return node.value

    def put(self, key, value):
        # 容量是不是等于0
        if self.capacity == 0:
            return
        # 之前不包含该key
        if key not in self.map.keys():
            # 容量超出
            if len(self.map) == self.capacity:
                sorted(self.frequencyNodes)
                tempNode = self.frequencyNodes.pop()
                # 移除第一个值（使用频率最低）
                del self.map[tempNode.key]
            # 创建新节点
            self.timeStamp += 1
            node = Node(1, self.timeStamp, key, value)
            # 添加
            self.map[key] = node
            self.frequencyNodes.add(node)
        else:
            node = map[key]
            # 移除掉，为了更新频率
            del self.frequencyNodes[node]
            # 更新使用次数
            node.usedCount += 1
            self.frequencyNodes += 1
            node.lastUsedTime = self.timeStamp
            node.value = value
            self.frequencyNodes[node] = node
            # 添加
            self.map[key] = node


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    # 2的使用频率增加
    print(cache.get(2))
    # 移除1
    cache.put(3, 3)
    # 1已经被移除
    print(cache.get(1))
    # 2还在
    print(cache.get(2))
    # 增加3的频次
    print(cache.get(3))
    print(cache.get(3))
    print(cache.get(3))
    # 移除2 ，新增4
    cache.put(4, 4)
    print(cache.get(3))
