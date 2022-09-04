# -*- coding:utf-8 -*-
# @Time : 2022/6/4 17:53
# @Author : huichuan LI
# @File : BinomialHeap.py
# @Software: PyCharm


import math as _math


class FibonacciHeapNode:
    '''
    斐波那契堆结点
    '''

    def __init__(self, key=None, degree=None, p=None, child=None, \
                 left=None, right=None, mark=None):
        '''
        斐波那契堆结点

        Args
        ===
        `key` : 关键字值

        `degree` : 子结点的个数

        `p` : 父结点

        `child` : 任意一个子结点

        `left` : 左兄弟结点

        `right` : 右兄弟结点

        `mark` : 自从x上一次成为另一个结点子女以来，它是否失掉了一个孩子

        '''
        self.key = key
        self.degree = degree
        self.p = p
        self.child = child
        self.left = left
        self.right = right
        self.mark = mark

    def __str__(self):
        return str({"key": self.key, \
                    "degree": self.degree})


def make_fib_node(key):
    '''
    创建斐波那契堆的结点
    Example
    ===
    ```python
    import fibonacciheap as fh
    >>> node = fh.make_fib_node()
    ```
    '''
    node = FibonacciHeapNode()
    node.key = key
    node.degree = 0
    node.left = node
    node.right = node
    node.p = None
    node.child = None
    return node


def make_fib_heap():
    '''
    创建一个新的空的斐波那契堆

    平摊代价和实际代价都为`O(1)`

    Example
    ===
    ```python
    import fibonacciheap as fh
    heap = fh.make_fib_heap()
    ```
    '''
    heap = FibonacciHeap()
    heap.keynum = 0
    heap.maxdegree = 0
    heap.min = None
    heap.cons = None
    return heap


def node_add(node: FibonacciHeapNode, root: FibonacciHeapNode):
    '''
    将单个结点`node``加入链表`root`之前

    此处`node`是单个结点，`root`是双向链表

    '''
    if node is None or root is None:
        return
    node.left = root.left
    root.left.right = node
    node.right = root
    root.left = node


def node_remove(node: FibonacciHeapNode):
    '''
    将单个结点`node`从双链表中移除
    '''
    node.left.right = node.right
    node.right.left = node.left


def node_cat(a: FibonacciHeapNode, b: FibonacciHeapNode):
    '''
    将双向链表`b`链接到双向链表`a`的后面
    '''
    tmp = a.right
    a.right = b.right
    b.right.left = a
    b.right = tmp
    tmp.left = b


def link(node: FibonacciHeapNode, root: FibonacciHeapNode):
    '''
    将`node`链接到`root`根结点
    '''
    FibonacciHeap.node_remove(node)
    if root is None:
        return
    if root.child == None:
        root.child = node
    else:
        FibonacciHeap.node_add(node, root.child)
    node.p = root
    root.degree += 1
    node.mark = False


class FibonacciHeap:
    '''
    斐波那契堆 不涉及删除元素的可合并堆操作仅需要`O(1)`的平摊时间,这是斐波那契堆的优点
    '''

    def __init__(self):
        '''
        斐波那契堆 不涉及删除元素的可合并堆操作仅需要`O(1)`的平摊时间,这是斐波那契堆的优点
        '''
        self.min = None
        self.cons = []
        self.keynum = 0
        self.maxdegree = 0

    @classmethod
    def make_fib_heap(self):
        '''
        创建一个新的空的斐波那契堆

        平摊代价和实际代价都为`O(1)`

        Example
        ===
        ```python
        heap = FibonacciHeap.make_fib_heap()
        ```
        '''
        heap = FibonacciHeap()
        heap.keynum = 0
        heap.maxdegree = 0
        heap.min = None
        heap.cons = None
        return heap

    @classmethod
    def make_fib_node(self, key):
        '''
        创建斐波那契堆的结点
        Example
        ===
        ```python
        node = FibonacciHeap.make_fib_node()
        ```
        '''
        node = FibonacciHeapNode()
        node.key = key
        node.degree = 0
        node.left = node
        node.right = node
        node.p = None
        node.child = None
        return node

    @classmethod
    def node_add(self, node: FibonacciHeapNode, root: FibonacciHeapNode):
        '''
        将单个结点`node``加入链表`root`之前

        此处`node`是单个结点，`root`是双向链表

        '''
        if node is None or root is None:
            return
        node.left = root.left
        root.left.right = node
        node.right = root
        root.left = node

    @classmethod
    def node_remove(self, node: FibonacciHeapNode):
        '''
        将单个结点`node`从双链表中移除
        '''
        node.left.right = node.right
        node.right.left = node.left

    @classmethod
    def node_cat(self, a: FibonacciHeapNode, b: FibonacciHeapNode):
        '''
        将双向链表`b`链接到双向链表`a`的后面
        '''
        tmp = a.right
        a.right = b.right
        b.right.left = a
        b.right = tmp
        tmp.left = b

    @classmethod
    def union(self, h1, h2):
        '''
        将`h1`和`h2`合并成一个堆，并返回合并后的堆
        '''
        tmp = None
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h2.maxdegree > h1.maxdegree:
            tmp = h1
            h1 = h2
            h2 = tmp

        if h1.min is None:
            h1.min = h2.min
            h1.keynum = h2.keynum
            del h2.cons
            del h2
        elif h2.min is None:
            del h2.cons
            del h2
        else:
            FibonacciHeap.node_cat(h1.min, h2.min)
            if h1.min.key > h2.min.key:
                h1.min = h2.min
            h1.keynum += h2.keynum
            del h2.cons
            del h2
        return h1

    def insertkey(self, key):
        '''
        插入一个关键字为`key`结点`x`
        '''
        node = FibonacciHeap.make_fib_node(key)
        self.insert(node)

    def insert(self, node: FibonacciHeapNode):
        '''
        插入一个结点`node`到斐波那契堆heap
        '''
        if self.keynum == 0:
            self.min = node
        else:
            FibonacciHeap.node_add(node, self.min)
            if node.key < self.min.key:
                self.min = node
        self.keynum += 1

    def unionwith(self, h2):
        '''
        将`self`和`h2`合并成一个堆，并返回合并后的堆
        '''
        tmp = None
        if self is None:
            return h2
        if h2 is None:
            return self

        if h2.maxdegree > self.maxdegree:
            tmp = self
            self = h2
            h2 = tmp

        if self.min is None:
            self.min = h2.min
            self.keynum = h2.keynum
            del h2.cons
            del h2
        elif h2.min is None:
            del h2.cons
            del h2
        else:
            FibonacciHeap.node_cat(self.min, h2.min)
            if self.min.key > h2.min.key:
                self.min = h2.min
            self.keynum += h2.keynum
            del h2.cons
            del h2
        return self

    def removemin(self):
        '''
        将堆的最小节点从根链表中移除

        意味着将最小结点所属的树移除
        '''
        min = self.min
        if self.min == min.right:
            self.min = None
        else:
            FibonacciHeap.node_remove(min)
            self.min = min.right
        min.right = min
        min.left = min.right
        return min

    def link(self, node: FibonacciHeapNode, root: FibonacciHeapNode):
        '''
        将`node`链接到`root`根结点
        '''
        FibonacciHeap.node_remove(node)
        if root.child == None:
            root.child = node
        else:
            FibonacciHeap.node_add(node, root.child)
        node.p = root
        root.degree += 1
        node.mark = False

    def cons_make(self):
        '''
        创建CONSOLIDATE过程所需空间
        '''
        old = self.maxdegree
        self.maxdegree = int(_math.log2(self.keynum) + 1)
        if old >= self.maxdegree:
            return
        self.cons = []
        for i in range(self.maxdegree + 1):
            self.cons.append(None)

    def consolidate(self):
        '''
        合并斐波那契堆的根链表中左右相同的度数
        '''
        i, d, D = 0, 0, 0
        x, y, tmp = None, None, None
        self.cons_make()
        D = self.maxdegree + 1
        for i in range(D):
            self.cons[i] = None
        while self.min is not None:
            x = self.removemin()
            d = x.degree
            while self.cons[d] is not None:
                y = self.cons[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y, x)
                self.cons[d] = None
                d += 1
            self.cons[d] = x
        self.min = None
        for i in range(D):
            if self.cons[i] is not None:
                if self.min is None:
                    self.min = self.cons[i]
                else:
                    FibonacciHeap.node_add(self.cons[i], self.min)
                    if self.cons[i].key < self.min.key:
                        self.min = self.cons[i]

    def __extractmin(self):
        '''
        移除最小节点，并返回最小结点
        '''
        if self is None or self.min is None:
            return None
        child = None
        min = self.min
        while min.child is not None:
            child = min.child
            FibonacciHeap.node_remove(child)
            if child.right == child:
                min.child = None
            else:
                min.child = child.right
            FibonacciHeap.node_add(child, self.min)
            child.p = None

        FibonacciHeap.node_remove(min)
        if min.right == min:
            self.min = None
        else:
            self.min = min.right
            self.consolidate()
        self.keynum -= 1
        return min

    def extractmin(self):
        '''
        移除最小节点，并返回最小结点
        '''
        if self.min is None:
            return
        node = self.__extractmin()
        if node is not None:
            del node

    def get_min_key(self):
        '''
        获取最小结点关键字值
        '''
        if self.min is None:
            return None
        return self.min.key

    @classmethod
    def renew_degree(self, parent: FibonacciHeapNode, degree: int):
        '''
        修改度数
        '''
        parent.degree -= degree
        if parent.p is not None:
            self.renew_degree(parent.p, degree)

    def cut(self, node: FibonacciHeapNode, parent: FibonacciHeapNode):
        '''
        将`node`从父结点`parent`的子链接中剥离出来,并使`node`成为
        '''
        FibonacciHeap.node_remove(node)
        FibonacciHeap.renew_degree(parent, node.degree)
        if node == node.right:
            parent.child = None
        else:
            parent.child = node.right
        node.p = None
        node.left = node
        node.right = node
        node.mark = False
        FibonacciHeap.node_add(node, self.min)

    def cascading_cut(self, node: FibonacciHeapNode):
        '''
        对节点`node``进行级联剪切

        级联剪切：如果减小后的结点破坏了最小堆的性质，则把它切下来
        (即从所在双向链表中删除，并将其插入到由最小树根结点形成的双向链表中)，
        然后再从被切结点的父结点到所在树根结点递归执行级联裁剪
        '''
        parent = node.p
        if parent is not None:
            return
        if node.mark == False:
            node.mark = True
        else:
            self.cut(node, parent)
            self.cascading_cut(parent)

    def decrease(self, node: FibonacciHeapNode, key):
        '''
        将斐波那契堆heap中结点`node`的值减少为`key`
        '''
        if self.min is None or node is None:
            return
        assert key < node.key
        node.key = key
        parent = node.p
        if parent is not None and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)
        if node.key < self.min.key:
            self.min = node

    def increase(self, node: FibonacciHeapNode, key):
        '''
        将斐波那契堆heap中结点`node`的值增加为`key`
        '''
        if self.min is None or node is None:
            return
        assert key > node.key
        while node.child is not None:
            child = node.child
            FibonacciHeap.node_remove(child)
            if child.right == child:
                node.child = None
            else:
                node.child = child.right
            FibonacciHeap.node_add(child, self.min)
            child.p = None
        node.degree = 0
        node.key = key
        parent = node.p
        if parent is not None:
            self.cut(node, parent)
            self.cascading_cut(parent)
        elif self.min == node:
            right = node.right
            while right is not node:
                if node.key > right.key:
                    self.min = right
                right = right.right

    def update(self, node: FibonacciHeapNode, key):
        '''
        更新二项堆heap的结点`node`的键值为`key`
        '''
        if key < node.key:
            self.decrease(node, key)
        elif key > node.key:
            self.increase(node, key)
        else:
            pass

    def updatekey(self, oldkey, newkey):
        '''
        更新二项堆heap的结点`node`的键值为`key`
        '''
        pass

    @classmethod
    def search_fromroot(self, root: FibonacciHeapNode, key):
        '''
        在最小堆`root`中查找键值为`key`的结点
        '''
        t = root
        p = None
        if root is None:
            return root
        while t != root.left:
            if t.key == key:
                p = t
                break
            else:
                p = self.search_fromroot(t.child, key)
                if p is not None:
                    break
                t = t.right
        else:
            if t.key == key:
                p = t
            else:
                p = self.search_fromroot(t.child, key)
        return p

    def search(self, key):
        '''
        在斐波那契堆heap中查找键值为`key`的节点
        '''
        if self.min is None:
            return None
        return self.search_fromroot(self.min, key)

    def delete(self, node: FibonacciHeapNode):
        '''
        删除结点`node`
        '''
        if self.min is None:
            return
        min = self.min
        self.decrease(node, min.key - 1)
        self.extractmin()
        del node

    def deletekey(self, key):
        '''
        删除关键字为`key`的结点`node`
        '''
        if self.min is None:
            return
        node = self.search(key)
        if node is None:
            return
        self.delete(node)

    @classmethod
    def destroynode(self, node: FibonacciHeapNode):
        '''
        销毁斐波那契堆
        '''
        if node is None:
            return
        start = node
        while node != start.left:
            self.destroy(node.child)
            node = node.right
            del node.left
        else:
            self.destroy(node.child)
            node = node.right
            del node.left

    def destroy(self):
        '''
        销毁斐波那契堆
        '''
        FibonacciHeap.destroynode(self.min)
        del self.cons

    @classmethod
    def print_node(self, node: FibonacciHeapNode, prev: FibonacciHeapNode, direction: int):
        '''
        打印"斐波那契堆"结点

        Args
        ===
        `node` : 当前结点

        `prev` : 当前结点的前一个结点(父结点或者兄弟结点)

        `direction` : 1表示当前结点是一个左孩子；2表示当前结点是一个兄弟结点

        '''
        start = node
        if node is None:
            return
        while node != start.left:
            if direction == 1:
                print('%8d(%d) is %2d\'s child' % (node.key, node.degree, prev.key))
            elif direction == 2:
                print('%8d(%d) is %2d\'s child' % (node.key, node.degree, prev.key))
            if node.child is not None:
                self.print_node(node.child, node, 1)
            prev = node
            node = node.right
            direction = 2
        else:
            if direction == 1:
                print('{}({}) is {}\'s child'.format(
                    node.key, node.degree, prev.key))
            elif direction == 2:
                print('{}({}) is {}\'s next'.format(node.key, node.degree, prev.key))
            if node.child is not None:
                self.print_node(node.child, node, 1)
            prev = node
            node = node.right
            direction = 2

    def print(self):
        '''
        打印"斐波那契堆"结点
        '''
        if self.min is None:
            return
        p = self.min
        i = 0
        while p != self.min.left:
            i += 1
            print("%2d. %4d(%d) is root " % (i, p.key, p.degree))
            FibonacciHeap.print_node(p.child, p, 1)
            p = p.right
        else:
            i += 1
            print("%2d. %4d(%d) is root " % (i, p.key, p.degree))
            FibonacciHeap.print_node(p.child, p, 1)
            p = p.right


def test():
    '''
    test
    '''
    print('FibonacciHeappNode and FibonacciHeap test')
    heap = FibonacciHeap.make_fib_heap()
    heap.insertkey(3)
    heap.insertkey(1)
    heap.insertkey(2)
    heap.insertkey(8)
    print(heap.min)
    heap.extractmin()
    print(heap.min)
    heapwillunion = FibonacciHeap.make_fib_heap()
    heapwillunion.insertkey(4)
    heapwillunion.insertkey(6)
    heapwillunion.insertkey(1)
    heapwillunion.insertkey(7)
    heap.unionwith(heapwillunion)
    print(heap.min)
    heap.deletekey(7)
    print(heap.min)
    heap.print()


if __name__ == '__main__':
    test()
else:
    pass
