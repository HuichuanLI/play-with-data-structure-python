import random
import time


class TreapNode:
    def __init__(self, val):
        self.val = val
        self.rank = random.randint(1, 1000000)
        self.leftChild = None
        self.rightChild = None
        self.parent = None


class Treap:
    def __init__(self):
        self.root = None

    def treapRotate(self, root, a):
        b = a.parent
        if not b:
            return root

        if a == b.leftChild:
            b.leftChild = a.rightChild
            if a.rightChild:
                a.rightChild.parent = b
            a.rightChild = b
        else:
            b.rightChild = a.leftChild
            if a.leftChild:
                a.leftChild.parent = b
            a.leftChild = b
        if b.parent:
            if b == b.parent.leftChild:
                b.parent.leftChild = a
            else:
                b.parent.rightChild = a
        a.parent = b.parent
        b.parent = a
        if root == b:
            root = a
        return root

    def treapFind(self, number):
        current = self.root
        while current:
            if current.val == number:
                return current
            elif current.val > number:
                current = current.leftChild
            else:
                current = current.rightChild
        return None

    def treapDelete(self, node):
        while node.leftChild or node.rightChild:
            child = node.leftChild
            if not child or node.rightChild and node.rightChild.rank > child.rank:
                child = node.rightChild
            self.root = self.treapRotate(self.root, child)
        if node.parent:
            if node.parent.leftChild == node:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        if self.root == node:
            self.root = None
        del node
        return self.root

    def printBst(self, fout, node):
        if not node:
            return
        self.printBst(fout, node.leftChild)
        fout.write(str(node.val) + '\n')
        self.printBst(fout, node.rightChild)

    def treapInsert(self, number):
        current = self.root
        previous = None
        while current:
            previous = current
            if current.val >= number:
                current = current.leftChild
            else:
                current = current.rightChild
        node = TreapNode(number)
        node.leftChild = None
        node.rightChild = None
        node.parent = None
        node.rank = random.randint(1, 1000000)
        if not previous:
            self.root = node
            return node
        node.parent = previous
        if previous.val >= node.val:
            previous.leftChild = node
        else:
            previous.rightChild = node

        while node.parent and node.parent.rank < node.rank:
            self.root = self.treapRotate(self.root, node)
        return self.root


if __name__ == '__main__':
    start_time = time.time()

    treap = Treap()
    root = treap.root
    with open('/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/Treap/data/5.in') as fin:
        n = int(fin.readline().strip())
        for i in range(n):
            number = int(fin.readline().strip())
            treap.treapInsert(number)

    root = treap.root
    with open('/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/Treap/data/5.out', 'w') as fout:
        treap.printBst(fout, root)

    with open('/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/Treap/data/5.in') as fin:
        n = int(fin.readline().strip())
        for i in range(n):
            number = int(fin.readline().strip())
            node = treap.treapFind(number)
            if not node:
                print(f"Cannot find number {number}")
            else:
                root = treap.treapDelete(node)

    print(f"Empty Tree?: {'Yes' if root is None else 'No'}")
    end_time = time.time()
    print(f"Total time: {(end_time - start_time):.3f}(s)")
