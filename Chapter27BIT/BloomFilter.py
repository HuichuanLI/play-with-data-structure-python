# -*- coding:utf-8 -*-
# @Time : 2022/5/22 21:55
# @Author : huichuan LI
# @File : BloomFilter.py
# @Software: PyCharm
from bitarray import bitarray


class HashFunction:
    size = 0
    # hash种子
    seed = 0

    def __init__(self, size, seed):
        self.size = size
        self.seed = seed

    # hash函数
    def hash(self, value):
        if value is None:
            return 0
        else:
            # hash值
            hash1 = hash(value)
            # 高位的hash值
            hash2 = hash1 >> 16
            # 合并hash值(相当于把高低位的特征结合)
            combine = hash1 ^ hash2
            # 相乘再取余
            return abs(combine * self.seed) % self.size


class MybloomFilter:
    # 默认大小
    DEFAULT_SIZE = 1000

    # 大小为默认大小
    SIZE = DEFAULT_SIZE

    # hash函数的种子因子
    HASH_SEEDS = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    # 位数组，0 / 1, 表示特征
    bitSet = bitarray(1000)

    # hash函数
    hashFunctions = []

    # 无参数初始化
    def __init__(self):
        # 按照默认大小
        self.init()

    # 带参数初始化
    def __init__(self, size):
        # 大小初始化小于最小的大小
        if (size >= self.DEFAULT_SIZE):
            self.SIZE = size
        self.init()

    def init(self):
        # 初始化位大小
        self.bitSet = bitarray(self.SIZE)
        # 初始化hash函数
        for i in range(len(self.HASH_SEEDS)):
            hashFunction = HashFunction(self.SIZE, self.HASH_SEEDS[i])
            self.hashFunctions.append(hashFunction)

    # 添加元素，相当于把元素的特征添加到位数组
    def add(self, value):
        for f in self.hashFunctions:
            # 将hash计算出来的位置为true
            self.bitSet[f.hash(value)] = 1

    # 判断元素的特征是否存在于位数组
    def contains(self, value):
        result = True
        for f in self.hashFunctions:
            result = result & self.bitSet[f.hash(value)]
            # hash函数只要有一个计算出为false，则直接返回
            if result is False:
                return result
        return result


if __name__ == '__main__':
    mybloomFilter = MybloomFilter(1000)
    print(mybloomFilter.contains("abc"))
    print(mybloomFilter.contains("def"))

    mybloomFilter.add("abc")
    mybloomFilter.add("def")

    print(mybloomFilter.contains("abc"))
    print(mybloomFilter.contains("def"))
    print(mybloomFilter.contains("ghi"))
