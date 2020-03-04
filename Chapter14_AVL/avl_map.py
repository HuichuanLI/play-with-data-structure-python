from .base import MapBase
from .AVLTree import AVLTree


class AVLMap(MapBase):
    def __init__(self):
        self._avl = AVLTree()

    def get_size(self):
        return self._avl.get_size()

    def is_empty(self):
        return self._avl.is_empty()

    def add(self, key, value):
        return self._avl.add(key, value)

    def contains(self, key):
        return self._avl.contains(key)

    def getter(self, key):
        return self._avl.getter(key)

    def setter(self, key, value):
        return self._avl.setter(key, value)

    def remove(self, key):
        return self._avl.remove(key)


if __name__ == '__main__':
    words = ''
    with open('./shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time

    start_time = time()
    avlMap = AVLMap()
    for word in words:
        if avlMap.contains(word):
            avlMap.setter(word, avlMap.getter(word) + 1)
        else:
            avlMap.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', avlMap.get_size())
    print('Contains word "they": ', avlMap.contains('they'))
    ## 耗时1.39秒左右
    print('Total time: {} seconds'.format(time() - start_time))

    # avlMap.remove('they')
    print(avlMap.contains('they'))
    # avlMap.setter('they', 100)
    # print(avlMap.getter('they'))

    print(avlMap._avl.is_banlanced())
