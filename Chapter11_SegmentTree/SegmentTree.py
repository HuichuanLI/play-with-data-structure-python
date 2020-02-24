class SegmentTree:
    def __init__(self, arr, merger):
        """线段树相当于将数组用一棵树重新表示"""
        if not isinstance(arr, list) or not arr or not merger:
            raise ValueError('Can not initialize empty array.')
        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)
        self._merger = merger
        self._build_segment_tree(tree_index=0, l=0, r=len(self._data) - 1)

    def get_size(self):
        return len(self._data)

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise ValueError('Index is illegal.')
        return self._data[index]

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    # 在tree_index位置创建表示区间[l...r]的线段树
    # 左右的端点l, r
    def _build_segment_tree(self, tree_index, l, r):
        if l == r:
            self._tree[tree_index] = self._data[l]
            return
        # 左子树的根节点
        left_tree_index = self._left_child(tree_index)
        # 右子树的根节点
        right_tree_index = self._right_child(tree_index)

        mid = l + (r - l) // 2
        self._build_segment_tree(left_tree_index, l, mid)
        self._build_segment_tree(right_tree_index, mid + 1, r)
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index],
            self._tree[right_tree_index],
        )

    def __str__(self):
        res = []
        res.append('[')
        for i in range(len(self._tree)):
            res.append(str(self._tree[i]))
            if i != len(self._tree) - 1:
                res.append(', ')
        res.append(']')
        return '<chapter_11_SegmentTree.segment_tree.SegmentTree>: ' + ''.join(res)

    def __repr__(self):
        return self.__str__()

    # [queryL,queryR]
    def query(self, queryL, queryR):
        if queryL < 0 or queryL >= len(self._data) or \
                queryR < 0 or queryR >= len(self._data) or \
                queryL > queryR:
            raise ValueError('Index is illegal.')
        return self._query(0, 0, len(self._data) - 1, queryL, queryR)

    # 在以tree_index为根的线段树中的(线段树本身)[l...r]的范围里，搜索区间(用户指定的)[query_l...query_r]的值
    def _query(self, treeIndex, l, r, queryL, queryR):
        if l == queryL and r == queryR:
            return self._tree[treeIndex]
        mid = l + (r - l) // 2
        leftTreeIndex = self._left_child(treeIndex)
        rightTreeIndex = self._right_child(treeIndex)
        if queryL >= mid + 1:
            return self._query(rightTreeIndex, mid + 1, r, queryL, queryR)
        elif queryR <= mid:
            return self._query(leftTreeIndex, l, mid, queryL, queryR)
        else:
            left_result = self._query(leftTreeIndex, l, mid, queryL, mid)
            right_result = self._query(rightTreeIndex, mid + 1, r, mid + 1, queryR)
            return self._merger(left_result, right_result)

    def setter(self, index, e):
        if index < 0 or index >= len(self._data):
            raise ValueError('Index is illegal.')
        self._data[index] = e
        self._setter(0, 0, len(self._data) - 1, index, e)

    def _setter(self, tree_index, l, r, index, e):
        if l == r:
            self._tree[tree_index] = e
            return
        mid = l + (r - l) // 2
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        if index >= mid + 1:
            self._setter(right_tree_index, mid + 1, r, index, e)
        else:
            self._setter(left_tree_index, l, mid, index, e)
        # 别忘了更新树上的该节点的值
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index],
            self._tree[right_tree_index],
        )


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    sum_merger = lambda a, b: a + b
    seg_tree = SegmentTree(arr=nums, merger=sum_merger)
    print(seg_tree)
    print(seg_tree.query(0, 3))
    print(seg_tree.query(2, 5))
    print(seg_tree.query(0, 5))

    seg_tree.setter(0, 1)
    print(seg_tree)
    print(seg_tree.query(0, 3))
