import unittest
import random

import Btree as bt
from Btree import BNode, BTree


class BTreeTest(unittest.TestCase):
    def test_create(self):
        """
        创建B-Tree测试
        :return:
        """
        r = BTree()
        r.create()
        self.assertIsInstance(r.root, BNode, 'The root of tree is NOT instance of BNode!')

    def test_insert(self):
        """
        插入新结点测试
                        ________12_________
                      /                    \
                 ____6,9____           ____15,18____
                /     \     \         /      \      \
          1,2,3,4,5  7,8  10,11    13,14   16,17   19,20
        :return:
        """
        r = b_tree_generator()

        expect = [12, 6, 9, 15, 18, 1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]
        actual = b_tree_serialization(r)

        self.assertEqual(expect, actual, 'The tree is not created in B-Tree role!')

    def test_search(self):
        """
        键搜索测试
                  7
                /  \
             3,5    9
            / \ \  / \
         1,2  4 6 8  10
        :return:
        """
        r = b_tree_generator()

        # 键存在
        x, i = bt.search(r.root, 2)
        self.assertEqual((x, i), (r.root.c[0].c[0], 1), 'The result is NOT for key: %s' % 2)

        # 键不存在
        x, i = bt.search(r.root, 21)
        self.assertIsNone(x, 'There is NO key %s in tree, but found!' % 11)

    def test_delete(self):
        """
        删除键测试
                        ________12_________
                      /                    \
                 ____6,9____           ____15,18,21_____
                /     \     \         /     \     \     \
          1,2,3,4,5  7,8  10,11    13,14  16,17  19,20  22,23,24
        :return:
        """
        r = b_tree_generator(max_key=20)
        r.insert(21)
        r.insert(22)
        r.insert(23)
        r.insert(24)
        # 验证B-Tree创建是否正确
        print('Test start: init tree')
        bt.tree_print(r.root)
        expect = [12, 6, 9, 15, 18, 21, 1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24]
        actual = b_tree_serialization(r)
        self.assertEqual(expect, actual, 'The tree is NOT created in B-Tree role!')

        # 情况1测试，含情况3a
        ''' 删除2，删除后的树
                       ____________15___________
                      /                         \
                 ____6,9,12______           ____18,21_____
                /     \   \      \         /      \       \
            1,3,4,5  7,8  10,11  13,14  16,17   19,20  22,23,24
        '''
        r.delete(r.root, 2)
        print('Scene 1: delete 2')
        bt.tree_print(r.root)
        expect = [15, 6, 9, 12, 18, 21, 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24]
        actual = b_tree_serialization(r)
        self.assertEqual(expect, actual, 'The tree is NOT a B-Tree after delete key!')

        # 情况2a测试
        ''' 删除6，删除后的树
                       ____________15___________
                      /                         \
                 ____5,9,12_____           _____18,21____
                /    \   \      \         /      \       \
            1,3,4   7,8  10,11  13,14  16,17   19,20  22,23,24
        '''
        r.delete(r.root, 6)
        print('Scene 2a: delete 6')
        bt.tree_print(r.root)
        expect = [15, 5, 9, 12, 18, 21, 1, 3, 4, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24]
        actual = b_tree_serialization(r)
        self.assertEqual(expect, actual, 'The tree is NOT a B-Tree after delete key!')

        # 情况2b测试，含情况3a
        ''' 删除21，删除后的树
                       __________12_________
                      /                     \
                 ____5,9_____        _____15,18,22______
                /     \      \      /     /      \      \
            1,3,4    7,8   10,11  13,14  16,17  19,20  23,24
        '''
        r.delete(r.root, 21)
        print('Scene 2b: delete 21')
        bt.tree_print(r.root)
        expect = [12, 5, 9, 15, 18, 22, 1, 3, 4, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 23, 24]
        actual = b_tree_serialization(r)
        self.assertEqual(expect, actual, 'The tree is NOT a B-Tree after delete key!')

        # 情况2c测试
        ''' 删除9，删除后的树
                       __________15_________
                      /                     \
                 ____5,12_____          ____18,22____
                /      \      \        /      \      \
            1,3,4  7,8,10,11  13,14  16,17  19,20  23,24
        '''
        r.delete(r.root, 9)
        print('Scene 2c: delete 9')
        bt.tree_print(r.root)
        expect = [15, 5, 12, 18, 22, 1, 3, 4, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 23, 24]
        actual = b_tree_serialization(r)
        self.assertEqual(expect, actual, 'The tree is NOT a B-Tree after delete key!')

        # 情况3b测试
        ''' 删除17，删除后的树

                 ______________5,12,18,22___________
                /      /        /            \      \
            1,3,4  7,8,10,11  13,14,15,16   19,20  23,24
        '''
        r.delete(r.root, 17)
        print('Scene 3b: delete 17')
        bt.tree_print(r.root)
        expect = [5, 12, 18, 22, 1, 3, 4, 7, 8, 10, 11, 13, 14, 15, 16, 19, 20, 23, 24]
        actual = b_tree_serialization(r)
        self.assertEqual(expect, actual, 'The tree is NOT a B-Tree after delete key!')

    def test_delete_random(self):
        # 进行10次测试
        for i in range(10):
            print('=====Round %d=====' % i)
            tree = BTree(t=100)
            tree.create()
            # 随机结点数量
            r1 = random.randint(20, 10000)
            keys = []
            # 构建B-Tree
            for _ in range(r1):
                key = random.randint(0, r1)
                keys.append(key)
                tree.insert(key)
                # print('Insert key: %d' % key)

            # 三分之一结点删除测试
            for _ in range(int(len(keys) / 3)):
                key = keys[random.randint(0, len(keys) - 1)]
                tree.delete(tree.root, key)
                # print('Delete key: %d' % key)

    def test_minimum(self):
        """
        子树最小值测试
                        ________12_________
                      /                    \
                 ____6,9____           ____15,18____
                /     \     \         /      \      \
          1,2,3,4,5  7,8  10,11    13,14   16,17   19,20
        :return:
        """
        r = b_tree_generator()
        x, i = bt.minimum(r.root)
        self.assertEqual(x.keys[i], 1, 'The result is NOT the minimum of sub tree!')

    def test_maximum(self):
        """
        子树最大值测试
                        ________12_________
                      /                    \
                 ____6,9____           ____15,18____
                /     \     \         /      \      \
          1,2,3,4,5  7,8  10,11    13,14   16,17   19,20
        :return:
        """
        r = b_tree_generator()
        x, i = bt.maximum(r.root)
        self.assertEqual(x.keys[i], 20, 'The result is NOT the maximum of sub tree')

    def test_successor(self):
        """
        后继测试
                        ________12_________
                      /                    \
                 ____6,9____           ____15,18____
                /     \     \         /      \      \
          1,2,3,4,5  7,8  10,11    13,14   16,17   19,20
        :return:
        """
        r = b_tree_generator()
        x, i = bt.successor(r.root, 0)
        self.assertEqual(x.keys[i], 13, 'The result is NOT the successor of key: %d' % r.root.keys[0])

    def test_predecessor(self):
        """
        前驱测试
                        ________12_________
                      /                    \
                 ____6,9____           ____15,18____
                /     \     \         /      \      \
          1,2,3,4,5  7,8  10,11    13,14   16,17   19,20
        :return:
        """
        r = b_tree_generator()
        x, i = bt.predecessor(r.root, 0)
        self.assertEqual(x.keys[i], 11, 'The result is NOT the predecessor of key: %d' % r.root.keys[0])

    def test_tree_print(self):
        """
        树型打印测试
        :return:
        """
        r1 = random.randint(20, 1000)
        r = b_tree_generator(max_key=r1)
        bt.tree_print(r.root)


def b_tree_generator(t=3, max_key=20):
    r = BTree(t=t)
    r.create()
    for i in range(max_key, 0, -1):
        r.insert(i)
    return r


def b_tree_serialization(b_tree):
    nodes = [b_tree.root]
    actual = []
    while True:
        if len(nodes) > 0:
            n = nodes[0]
            del nodes[0]
            actual += [k for k in n.keys if k]
            nodes += [c for c in n.c if c]
        else:
            break

    return actual
