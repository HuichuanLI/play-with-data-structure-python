from collections import deque


class BST:
    """这里的BST实现不包括重复元素（为了演示原理方便）"""

    class _Node:
        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # 添加
    def add(self, e):
        self._root = self._add(self._root, e)

    def _add(self, node, e):

        # if node.e == e:
        #     return
        # elif node.e > e and not node.left:
        #     node.left = self._Node(e)
        #     self._size += 1
        #     return
        # elif node.e < e and not node.right:
        #     node.right = self._Node(e)
        #     self._size += 1
        #     return
        # # 递归条件
        # if node.e > e:
        #     self._add(node.left, e)
        # else:
        #     self._add(node.right, e)

        if not node:
            self._size += 1
            return self._Node(e)
        elif node.e > e:
            node.left = self._add(node.left, e)
        elif node.e < e:
            node.right = self._add(node.right, e)

        return node

    def contains(self, e):
        """以root为根有没有e"""
        return self._contains(self._root, e)

    def _contains(self, node, e):
        """以node为根有没有e"""
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)

    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node):
        if not node:
            return node
        print(node.e)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order_NR(self):
        """使用栈实现非递归的栈"""
        stack = []
        stack.append(self._root)
        while stack:
            curr = stack.pop()
            print(curr.e)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    def in_order(self):
        return self._in_order(self._root)

    def _in_order(self, node):
        if not node:
            return
        self._in_order(node.left)
        print(node.e)
        self._in_order(node.right)

    def post_order(self):
        """一个应用是释放内存"""
        return self._post_order(self._root)

    def _post_order(self, node):
        if not node:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.e)

    def level_order(self):
        """层序便利"""
        queue = deque()
        queue.append(self._root)
        while queue:
            curr = queue.popleft()
            print(curr.e)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def minimum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        self._maximum(self._root)

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def _generate_depth_string(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def _generate_BST_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.e) + '\n')
        self._generate_BST_string(node.left, depth + 1, res)
        self._generate_BST_string(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self._generate_BST_string(self._root, 0, res)
        return '<chapter_08_BST.bst.BST>:\n' + ''.join(res)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    bst = BST()
    nums = [5, 3, 6, 8, 4, 2, 2]
    for num in nums:
        bst.add(num)
    bst.pre_order()
    print(bst)

    # bst.pre_order_NR()

    bst.level_order()
