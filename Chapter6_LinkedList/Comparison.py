from LinkedListStack import LinkedListStack
from ArrayStack import ArrayStack
from time import time
from random import randint


def test_push(stack, op_count):
    start_time = time()
    for i in range(op_count):
        stack.push(randint(1, 2000))
    return time() - start_time


def test_pop(stack, op_count):
    start_time = time()
    for i in range(op_count):
        stack.pop()
    return time() - start_time


op_count = 1000000
linked_stack = LinkedListStack()
array_stack = ArrayStack()

print('LinkedStack push: ', test_push(linked_stack, op_count))
print('ArrayStack push: ', test_push(array_stack, op_count))

print('LinkedStack Pop: ', test_pop(linked_stack, op_count))
print('ArrayStack Pop: ', test_pop(array_stack, op_count))
