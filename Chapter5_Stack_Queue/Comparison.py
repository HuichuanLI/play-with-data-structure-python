from ArrayQueue import ArrayQueue
from LoopQueue import LoopQueue
from time import time
from random import randint


def test_enqueue(queue, op_count):
    start_time = time()
    for i in range(op_count):
        queue.enqueue(randint(1, 2000))
    return time() - start_time


def test_dequeue(queue, op_count):
    start_time = time()
    for i in range(op_count):
        queue.dequeue()
    return time() - start_time


op_count = 10000
array_queue = ArrayQueue()
loop_queue = LoopQueue()

print('ArrayQueue enqueue: ', test_enqueue(array_queue, op_count))
print('LoopQueue enqueue: ', test_enqueue(loop_queue, op_count))

print('ArrayQueue dequeue: ', test_dequeue(array_queue, op_count))
print('LoopQueue dequeue: ', test_dequeue(loop_queue, op_count))
