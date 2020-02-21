from base import QueueBase
from Array import Array


class ArrayQueue(QueueBase):

    def __init__(self, capacity=0):
        self._array = Array(capacity)

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self.get_capacity()

    def enqueue(self, e):
        self._array.add_last(e)

    def dequeue(self):
        return self._array.remove_first()

    def get_front(self):
        return self._array.get_first()

    def __str__(self):
        return str('<chapter_05_Stack_Queue.queue.ArrayQueue> : {}'.format(self._array))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    queue = ArrayQueue()
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
