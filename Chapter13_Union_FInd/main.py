from UnionFind1 import UnionFind1
from UnionFind2 import UnionFind2
from UnionFind3 import UnionFind3
from UnionFind4 import UnionFind4
from UnionFind5 import UnionFind5
from UnionFind6 import UnionFind6
from time import time
from random import randint


def test_uf(uf, m):
    size = uf.get_size()
    start_time = time()
    for _ in range(m):
        # python randint [a, b] random number with inclusive range
        a = randint(0, size - 1)
        b = randint(0, size - 1)
        uf.union_elements(a, b)
    for _ in range(m):
        a = randint(0, size - 1)
        b = randint(0, size - 1)
        uf.is_connected(a, b)
    end_time = time()
    print('Time cost: {}'.format(end_time - start_time))


if __name__ == '__main__':
    size = 1000000
    m = 1000000
    # uf1 = UnionFind1(size)
    # uf2 = UnionFind2(size)
    uf3 = UnionFind3(size)
    uf4 = UnionFind4(size)
    uf5 = UnionFind5(size)
    uf6 = UnionFind6(size)
    # test_uf(uf1, m)
    # test_uf(uf2, m)
    test_uf(uf3, m)
    test_uf(uf4, m)
    test_uf(uf5, m)
    test_uf(uf6, m)
    #
