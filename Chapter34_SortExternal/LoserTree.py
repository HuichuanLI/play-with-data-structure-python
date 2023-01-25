from CompleteBinaryTree import CompleteBinaryTree


# 赢者树
class WinnerTree(CompleteBinaryTree):
    """
    赢者树
    与堆类似，空间和时间复杂度也和堆一样
    常用于多路归并
    赢者树也是完全二叉树结构，可以使用线性结构的数组来维护
    实现时，输入的原始序列A不作为树的叶子结点，而是使用一个新的数组ls来保存记录在A中的索引值。
    创建赢者树时，ls从后向前依次计算结点值(实际记录在A中的索引)。ls叶子结点的值通过A计算而来。
    修改记录时，由下向上依次调整结点，直至调整到位，或到达根结点。
    """

    @staticmethod
    def match(a, b):
        """
        比赛，定义输赢规则，返回前者是否赢后者
        :param a:
        :param b:
        :return:
        """
        return a < b

    def __init__(self, a, match=None):
        self.K = len(a) - 1  # 赢者树元素个数
        self.leaves = a  # 原始序列
        self.wt = [None] * self.K  # 初始化赢者树
        if match:
            self.match = match  # 用户自定义比赛
        # 构建赢者树
        self._build_tree()

    def _build_tree(self):
        """
        构建赢者树
        :return:
        """

        # 从后向前依次计算结点值，值为记录在原始序列中的索引
        for i in range(self.K - 1, -1, -1):
            self._adjust(i)

    def _adjust(self, i):
        """
        调整赢者树结点值
        :param i: 赢者树结点索引
        :return:
        """
        # 根据完全二叉树性质，计算结点i的左子结点位置
        li = self.left(i)
        '''
        记录在原始序列A中的位置索引
        因为存储结构的设计上，ls只存记录在A中的索引，且A被作为叶子结点使用，
        但在结构上不体现，所以有以下逻辑
        1. 如果li在ls范围内，则为ls位置li的值
        2. 如果li超出ls范围，则为li-K
        '''
        left = self.wt[li] if li < self.K else li - self.K

        # 同左子结点
        lr = self.right(i)
        right = self.wt[lr] if lr < self.K else lr - self.K

        # 左右结点比赛，选出赢者，将其索引写入ls位置为i的结点
        # 注意：完全二叉树的性质决定，其前二分之一结点中，最后一个结点可能没有右子结点，其他结点均有两个子结点。
        self.wt[i] = left if right >= self.K * 2 or self.match(self.leaves[left], self.leaves[right]) else right

    def modify_key(self, i, key):
        """
        修改原始序列记录值
        :param i:
        :param key:
        :return:
        """
        self.leaves[i] = key  # 更新原始序列
        parent = self.parent(i + self.K)  # 记录i父结点
        # 从下往上依次更新结点值
        while parent > -1:
            original = self.wt[parent]  # 结点原值
            self._adjust(parent)  # 调整结点
            if original == self.wt[parent]:
                # 如果结点值未改变，说明已经调整到位，退出
                break
            parent = self.parent(parent)  # 指针上移至父结点

    @property
    def winner(self):
        """
        赢者树的赢者
        :return:
        """
        return self.wt[0], self.leaves[self.wt[0]]

    def tree_check(self):
        """
        赢者树合规检查
        :return:
        """
        for i, v in enumerate(self.wt):
            # 获取左右结点的逻辑同_adjust
            li = self.left(i)
            left = self.wt[li] if li < self.K else li - self.K
            lr = self.right(i)
            right = self.wt[lr] if lr < self.K else lr - self.K
            if v != (left if right >= self.K * 2 or self.match(self.leaves[left], self.leaves[right]) else right):
                # 如果记录的不是左右结点的赢者，则该树不是有效赢者树
                return False
        return True



# 输者树
class LoserTree(CompleteBinaryTree):
    """
    输者树
    - 是赢者树的一种变体。
    - 在输者树中，用父结点记录左右子结点进行比赛的输者，而让胜者参加下一轮的比赛。
      输者树的根结点记录的是输者，需要增加一个结点来记录比赛的赢者。
    - 本实现中为了保持CompleteBinaryTree中的父子结点计算方法有效性，没有在输者树中增加结点，
      而是单独设置了一个属性来保存胜者。
    """
    EXTREMUM = float('-inf')  # 极值
    _winner = 0  # 赢者

    @staticmethod
    def match(a, b):
        """
        比赛，确定a是否赢b
        :param a:
        :param b:
        :return:
        """
        return a <= b

    @property
    def winner(self):
        """
        - 赢者属性，保存赢者信息。
        - 只读属性。
        :return: 返回真实值
        """
        return self._winner, self.leaves[self._winner]

    def __init__(self, a, match=None, extremum=None):
        if match:
            # 自定义比赛
            self.match = match
        if extremum:
            # 自定义极值。注意，如果自定义比赛，则必须同时指定极值
            self.EXTREMUM = extremum
        self.K = len(a) - 1  # 输者树结点个数
        # 叶节点，最后追加一个极值(赢者值)，辅助树生成
        self.leaves = a + [self.EXTREMUM]
        self.lt = [-1] * self.K  # 输者树

        # 构建输者树
        self._build_tree()

    def _adjust(self, i):
        """
        调整结点
        :param i: 叶节点索引(此处与赢者树不同)
        :return:
        """
        parent = i + self.K
        # 自下而上调整，直到根结点
        while True:
            parent = self.parent(parent)  # 父结点
            if parent > -1:
                # 赢者i与父结点进行比赛。
                # 第一次循环时，记录i没有进行过任何比赛，默认其即为赢者，也为输者。
                if not self.match(self.leaves[i], self.leaves[self.lt[parent]]):
                    # 记录i为输者，更新输信息
                    temp = self.lt[parent]  # 缓存父结点现值
                    self.lt[parent] = i  # 更新父结点为记录i
                    i = temp  # i指向赢者
            else:
                # 调整结束
                break
        # 更新赢者
        self._winner = i

    def _build_tree(self):
        """
        构建输者树
        :return:
        """
        for i in range(self.K, -1, -1):
            # 从后往前依次调整结点
            self._adjust(i)

    def modify_key(self, i, key):
        """
        修改记录值
        :param i:
        :param key:
        :return:
        """
        self.leaves[i] = key  # 修改记录
        self._adjust(i)  # 调整记录

    def tree_check(self):
        """
        输者树合规检查
        采用逆向验证策略；输者树是自下而上生成的，验证的时候自上而下。
        对于结点i，其两个子结点记录的是四个孙结点中的输者，但是i的值是由四个孙结点中的两个赢者进行比赛产生的输者。
        所以可以借助相同原始序列产生的赢者树(winner_tree)作为辅助；winner_tree中结点i的两个子结点left和right即为四个孙结点的赢者，
        因此left和right比赛的输者即为loser_tree中的结点i的值。
        :return:
        """
        # 使用输者树相同的原始序列生成对应的赢者树
        winner_tree = WinnerTree(self.leaves[:-1], match=self.match)  # 注意从叶结点中排除掉末尾的极值填充
        # 遍历检查输者树的每个结点
        for i in range(self.K):
            # 左子结点索引
            li = self.left(i)
            # winner_tree中的左子结点值
            left = winner_tree.leaves[winner_tree.wt[li]] if li < self.K else winner_tree.leaves[li - winner_tree.K]
            # 右子结点索引
            ri = self.right(i)
            # winner_tree中的右子结点值，如果右子结点不存在，则值为None
            right = None \
                if ri > 2 * self.K \
                else (winner_tree.leaves[winner_tree.wt[ri]] if ri < self.K else winner_tree.leaves[ri - winner_tree.K])
            # 验证loser_tree的结点i的值是否等于如上left和right中的输者，如果right为None，则输者自动为left
            if self.leaves[self.lt[i]] != (right if right is not None and self.match(left, right) else left):
                # 验证失败
                return False
        # 验证成功
        return True
