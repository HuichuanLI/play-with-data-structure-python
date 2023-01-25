import unittest

from LoserTree import WinnerTree, LoserTree


# 赢者树测试
class WinnerTreeTest(unittest.TestCase):
    def setUp(self):
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.winner_tree = WinnerTree(self.a)
        self.assertTrue(self.winner_tree.tree_check(), 'The tree is NOT a winner tree!')

    def test_tree_check(self):
        self.assertTrue(self.winner_tree.tree_check(), 'The tree is NOT a winner tree!')

        self.winner_tree.wt[0] = 1
        self.assertFalse(self.winner_tree.tree_check(), 'The tree is a NOT winner tree, by tree_check return True!')

    def test_custom_match_extremum(self):
        winner_tree = WinnerTree(self.a, match=lambda a, b: a > b)
        self.assertTrue(winner_tree.tree_check(), 'The tree is NOT a winner tree!')

    # 赢者测试
    def test_winner(self):
        """
        赢者测试
        :return:
        """
        self.assertEqual(-987, self.winner_tree.winner[1], 'The result is NOT the winner!')

    # 修改记录值测试
    def test_modify_key(self):
        """
        修改记录值测试
        :return:
        """
        self.winner_tree.modify_key(4, float('inf'))
        self.assertTrue(self.winner_tree.tree_check(), 'The tree is NOT a winner tree after modify key!')
        self.assertEqual(-20, self.winner_tree.winner[1], 'The result is NOT the winner!')

        self.winner_tree.modify_key(3, 1)
        self.assertTrue(self.winner_tree.tree_check(), 'The tree is NOT a winner tree after modify key!')


# 输者树测试
class LoserTreeTest(unittest.TestCase):
    def setUp(self):
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.loser_tree = LoserTree(self.a)
        self.assertTrue(self.loser_tree.tree_check(), 'The tree is NOT a loser tree!')

    def test_custom_match_extremum(self):
        loser_tree = LoserTree(self.a, match=lambda a, b: a >= b, extremum=float('inf'))
        self.assertTrue(loser_tree.tree_check(), 'The tree is NOT a loser tree!')

    def test_tree_check(self):
        self.assertTrue(self.loser_tree.tree_check(), 'The tree is NOT a loser tree!')

        self.loser_tree.lt[0] = 0
        self.assertFalse(self.loser_tree.tree_check(), 'The tree is NOT a loser tree, by tree_check return True')

    # 赢者测试
    def test_winner(self):
        """
        赢者测试
        :return:
        """
        expect = -987
        _, actual = self.loser_tree.winner
        self.assertEqual(expect, actual, 'The actual is NOT the winner of tree!')

    # 修改记录值测试
    def test_modify_key(self):
        """
        修改记录值测试
        :return:
        """
        self.loser_tree.modify_key(4, 1)
        self.assertTrue(self.loser_tree.tree_check(), 'The tree is NOT a loser tree after modify key!')
        self.assertEqual(-20, self.loser_tree.winner[1], 'The result is NOT the winner of tree!')
