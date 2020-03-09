from Array import Array
from random import randint


class IndexHeap:
    def __init__(self, capacity):
        # data 表示为元素的数组
        self._data = Array(capacity=capacity)
        # index[i] 数组表示为对堆中第i的位置上的元素
        self._index = Array(capacity=capacity)
        # reversed[i] 为i的在索引堆位置是index逆运算
        self._reversed = Array(capacity=capacity)
        for i in range(capacity):
            self._reversed.add(i, -1)
        self.capacity = capacity
        self.count = 0

    def getSize(self):
        return self.count

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.count == 0

    def add(self, i, ele):
        self._data.add(i, ele)

        self._index.add_last(i)
        self._reversed.set(i, self.count)
        self.count += 1
        self._shiftUp(self._data.get_size() - 1)

    def extractMax(self):
        if self.count < 0:
            raise ValueError("capacity should be >0")
        ele = self._data.get(self._index.get_first())
        self._index.set(0, self._index.get_last())
        self.count -= 1
        if self.count != 0:
            self._index.remove_last()
        self._shiftDown(0)
        return ele

    def leftChid(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def _shiftDown(self, index):
        if index < 0:
            raise ValueError("index should be postive")
        cur = self._data.get(self._index.get(index))
        cur_index = self._index.get(index)
        while self.leftChid(index) < self._index.get_size():
            max_index = self.leftChid(index)
            if self.rightChild(index) < self._index.get_size() and self._data.get(
                    self._index.get(self.rightChild(index))) > self._data.get(self._index.get(self.leftChid(index))):
                max_index = self.rightChild(index)
            if self._data.get(self._index.get(max_index)) > cur:
                self._index.set(index, self._index.get(max_index))
                self._reversed.set(self._index.get(max_index), index)
                index = max_index
            else:
                break
        self._index.set(index, cur_index)
        self._reversed.set(self._index.get(index), cur_index)

    def _shiftUp(self, index):
        if index < 0:
            raise ValueError("index should be postive")
        cur = self._data.get(self._index.get(index))
        cur_index = self._index.get(index)
        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self._data.get(self._index.get(parent)) < cur:
                self._index.set(index, self._index.get(parent))
                self._reversed.set(self._index.get(index), index)
                index = (index - 1) // 2
            else:
                break
        self._index.set(index, cur_index)
        self._reversed.set(self._index.get(index), index)

    def extractMaxIndex(self):
        if self.count < 0:
            raise ValueError("capacity should be >0")
        ele = self._index.get_size()
        self._index.set(0, self._index.get_last())
        self._reversed.set(self._index.get(0), 0)
        self._reversed.set(self._index.get_last(), -1)
        self.count -= 1

        if self.count != 0:
            self._index.remove_last()
        self._shiftDown(0)
        return ele

    def contains(self, index):
        return self._reversed[index] != -1

    def getItem(self, index):
        assert self.contains(index)
        return self._data.get(index)

    def change(self, i, item):
        assert self.contains(i)
        self._data.set(i, item)
        # 找到index中的i的位置 index[j] == i
        # 之后shiftUp(j),shiftDown(j)
        # o(n)
        # for j, w in enumerate(self._index):
        #     if w == i:
        #         self._shiftDown(j)
        #         self._shiftUp(j)
        #         return
        j = self._reversed[i]
        self._shiftUp(j)
        self._shiftDown(j)

    def __str__(self):
        return str(
            ' heap_index: {}, heap_value:{},capacity: {},size:{}'.format(self._data, self._index, self.capacity,
                                                                         self.count))


if __name__ == "__main__":
    indexHeap = IndexHeap(100000)
    random_list = [randint(-1000, 1000) for _ in range(10000)]
    for index, i in enumerate(random_list):
        indexHeap.add(index, i)

    # print(indexHeap.getItem(9))

    for _ in range(len(random_list)):
        print(indexHeap.extractMax())
        # print(indexHeap)
