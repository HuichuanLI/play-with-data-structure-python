from Array import Array
from random import randint


class IndexHeap:
    def __init__(self, capacity):
        # data 表示为元素的数组
        self._data = Array(capacity=capacity)
        # index[i] 数组表示为对堆中第i的位置上的元素
        self._index = Array(capacity=capacity)
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
                index = max_index
            else:
                break
        self._index.set(index, cur_index)

    def _shiftUp(self, index):
        if index < 0:
            raise ValueError("index should be postive")
        cur = self._data.get(self._index.get(index))
        cur_index = self._index.get(index)
        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self._data.get(self._index.get(parent)) < cur:
                self._index.set(index, self._index.get(parent))
                index = (index - 1) // 2
            else:
                break
        self._index.set(index, cur_index)

    def extractMaxIndex(self):
        if self.count < 0:
            raise ValueError("capacity should be >0")
        ele = self._index.get_size()
        self._index.set(0, self._index.get_last())
        self.count -= 1
        if self.count != 0:
            self._index.remove_last()
        self._shiftDown(0)
        return ele

    def getItem(self, index):
        return self._data.get(index)

    def change(self, i, item):
        self._data.set(i, item)
        # 找到index中的i的位置 index[j] == i
        # 之后shiftUp(j),shiftDown(j)
        # o(n)
        for j, w in enumerate(self._index):
            if w == i:
                self._shiftDown(j)
                self._shiftUp(j)
                return

    def __str__(self):
        return str(' heap_index: {}, heap_value:{},capacity: {},size:{}'.format(self._data, self._index, self.capacity,
                                                                                self.count))


if __name__ == "__main__":
    indexHeap = IndexHeap(100000)
    random_list = [randint(-100, 100) for _ in range(10000)]
    for index,i in enumerate(random_list):
        indexHeap.add(index, i)

    # print(indexHeap.getItem(9))

    for _ in range(len(random_list)):
        print(indexHeap.extractMax())
        # print(indexHeap)
