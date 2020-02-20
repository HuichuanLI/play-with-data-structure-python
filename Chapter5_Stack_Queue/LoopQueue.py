from base import QueueBase
from Array import Array


class LoopQueue(QueueBase):
    """必须浪费一个空间"""

    def __init__(self, capacity=10):
        """浪费一个空间"""
        self._data = [None] * (capacity + 1)
        self._front = 0
        self._tail = 0
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_capacity(self):
        return len(self._data) - 1

    def enqueue(self, e):
        if (self._tail + 1) % len(self._data) == self._front:
            self._resize(self.get_capacity() * 2)
        self._data[self._tail] = e
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def dequeue(self):
        # 使用循环队列出队时间复杂度为O(1)
        if self.is_empty():
            raise ValueError('Can not dequeue from an empty queue.')
        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:
            self._resize(self.get_capacity() // 2)
        return ret

    def _resize(self, new_capacity):
        new_data = [None] * (new_capacity + 1)
        for i in range(self._size):
            # 仔细体会，循环遍历
            new_data[i] = self._data[(i + self._front) % len(self._data)]
        self._data = new_data
        self._front = 0
        self._tail = self._size

    def get_front(self):
        if self.is_empty():
            raise ValueError('Can not get_front from an empty queue.')
        return self._data[self._front]

    def __str__(self):
        if self._tail >= self._front:
            return str('<chapter_05_Stack_Queue.queue.LoopQueue> : front {} tail, capacity: {}'.format(
                self._data[self._front:self._tail], self.get_capacity()))
        else:
            # presentation purpose only
            return str('<chapter_05_Stack_Queue.queue.LoopQueue> : front {} tail, capacity: {}'.format(
                str(self._data[self._front:] + self._data[:self._tail]), self.get_capacity()))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    queue = LoopQueue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(0)
    queue.enqueue(10)
    queue.enqueue(10)
    queue.enqueue(10)
    queue.enqueue(10)
    print(queue)

    queue.dequeue()
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)
