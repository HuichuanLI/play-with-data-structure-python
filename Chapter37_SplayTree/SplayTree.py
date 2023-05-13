import random


class SplayNode:
    def __init__(self, val=None):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None


class Splay:
    def __init__(self):
        self.root = None

    def rotate(self, root, a):
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
            self.root = a
            root = a
        return root

    def splayInsert(self, number):
        current = self.root
        previous = None
        while current:
            previous = current
            if current.val >= number:
                current = current.leftChild
            else:
                current = current.rightChild

        node = SplayNode(number)
        node.leftChild = None
        node.rightChild = None
        node.parent = None
        if not previous:
            self.root = node
            return node

        node.parent = previous
        if previous.val >= node.val:
            previous.leftChild = node
        else:
            previous.rightChild = node

        return self.splay(self.root, node)

    def splay(self, root, node):
        while node != root:
            if node.parent == root:
                root = self.rotate(root, node)
            elif node == node.parent.leftChild and node.parent == node.parent.parent.leftChild \
                    or node == node.parent.rightChild and node.parent == node.parent.parent.rightChild:
                root = self.rotate(root, node.parent)
                root = self.rotate(root, node)
            else:
                root = self.rotate(root, node)
                root = self.rotate(root, node)
        return root

    def splayFind(self, root, number):
        current = root
        while current:
            if current.val == number:
                return current
            elif current.val > number:
                current = current.leftChild
            else:
                current = current.rightChild
        return None

    def printSplay(self, fout, node):
        if node is None:
            return
        self.printSplay(fout, node.leftChild)
        fout.write(str(node.val) + "\n")
        self.printSplay(fout, node.rightChild)

    def splayDelete(self, root, node):
        root = self.splay(root, node)
        if root.leftChild:
            root.leftChild.parent = None
        if root.rightChild:
            root.rightChild.parent = None
        root = self.splayMerge(root.leftChild, root.rightChild)
        del node
        return root

    def splayMerge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        newRoot = None
        if random.randrange(2) == 0:
            newRoot = a
            while newRoot.rightChild:
                newRoot = newRoot.rightChild
            newRoot = self.splay(a, newRoot)
            newRoot.rightChild = b
            b.parent = newRoot
        else:
            newRoot = b
            while newRoot.leftChild:
                newRoot = newRoot.leftChild
            newRoot = self.splay(b, newRoot)
            newRoot.leftChild = a
            a.parent = newRoot
        return newRoot


if __name__ == '__main__':
    import time
    import random

    start_time = time.time()
    splay = Splay()
    root = splay.root
    number = []
    with open("/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/Splay/data/5.in", "r") as fin:
        n = int(fin.readline())
        for i in range(n):
            number.append(int(fin.readline()))
            root = splay.splayInsert(number[i])

    with open("/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/Splay/data/5.out", "w") as fout:
        splay.printSplay(fout, root)

    for i in range(n - 1, -1, -1):
        node = splay.splayFind(root, number[i])
        if not node:
            print(f"Cannot find number {number[i]}")
        else:
            root = splay.splayDelete(root, node)

    print("Empty Tree?:" + ("Yes" if root is None else "No"))
    end_time = time.time()
    print(f"Total time: {(end_time - start_time):.3f}(s)")
