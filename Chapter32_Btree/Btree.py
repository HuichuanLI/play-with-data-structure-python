class BNode(object):
    """
    B-Tree 结点
    """
    keys = []  # 键
    data = []  # 卫星数据
    c = []  # 子结点
    n = 0  # 关键字个数
    leaf = True  # 是否为叶子结点

    def insert_key(self, i, k):
        j = self.n - 1
        while j >= i:
            self.keys[j + 1] = self.keys[j]
            j -= 1
        self.keys[i] = k
        self.n += 1

    def insert_c(self, i, cn):
        j = (self.c.index(None) if None in self.c else len(self.c)) - 1
        while j >= i:
            self.c[j + 1] = self.c[j]
            j -= 1
        self.c[i] = cn

    def append_key(self, k):
        self.keys[self.n] = k
        self.n += 1

    def append_c(self, cn):
        idx = (self.c.index(None) if None in self.c else len(self.c))
        self.c[idx] = cn

    def del_key(self, i):
        while i < self.n - 1:
            self.keys[i] = self.keys[i + 1]
            i += 1
        self.pop_key()

    def del_c(self, i):
        idx = (self.c.index(None) if None in self.c else len(self.c)) - 1
        while i < idx:
            self.c[i] = self.c[i + 1]
            i += 1
        self.c[idx] = None

    def pop_key(self):
        key = self.keys[self.n - 1]
        self.keys[self.n - 1] = None
        self.n -= 1
        return key

    def pop_c(self):
        idx = (self.c.index(None) if None in self.c else len(self.c)) - 1
        c = self.c[idx]
        self.c[idx] = None
        return c

    def __init__(self, t=5):
        self.keys = [None] * (2 * t - 1)
        self.c = [None] * (2 * t)


class BTree(object):
    """
    B-Tree
    """

    def __init__(self, root=None, t=3):
        self.root = root  # 根结点
        self.t = t  # 最小度数

    def create(self):
        """
        创建B-Tree
        :return:
        """
        x = ALLOCATE_NODE(t=self.t)
        DISK_WRITE(x)
        self.root = x

    def _split_node(self, x, i):
        """
        拆分满结点
        :param x:
        :param i:
        :return:
        """
        z = ALLOCATE_NODE(t=self.t)  # type:BNode # 分配新的结点
        y = x.c[i]  # type:BNode # 待分割的结点
        z.leaf = y.leaf  # 新结点与待分割结点处在同一层级
        z.n = 0  # 新结点当前为空

        # 将结点y中的后半部分key转移到z中
        for _ in range(self.t - 1):
            z.insert_key(0, y.pop_key())

        # 如果y不是叶子结点，将y的后半部分子结点转移到z中
        if not y.leaf:
            for _ in range(self.t):
                z.insert_c(0, y.pop_c())

        # 父结点x的子结点列表空出i位置，插入z
        x.insert_c(i + 1, z)

        # 父结点x的键列表空出i位置，插入y的中间 键
        x.insert_key(i, y.pop_key())

        # 修改过的结点写入磁盘
        DISK_WRITE(x)
        DISK_WRITE(y)
        DISK_WRITE(z)

    def _insert_non_full(self, x, k):
        """
        插入新结点(非满结点)
        :param x:
        :param k:
        :return:
        """
        i = x.n - 1
        # 如果是叶子结点，直接在适当位置插入新键
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.insert_key(i + 1, k)
            DISK_WRITE(x)
        else:
            # 不是叶子结点，向下逐层迭代

            # 找到需要键区间。
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            DISK_READ(x.c[i])
            # 如果子结点为满结点，进行拆分
            if x.c[i].n >= 2 * self.t - 1:
                self._split_node(x, i)
                if k > x.keys[i]:
                    i += 1

            # 向下迭代
            self._insert_non_full(x.c[i], k)

    def insert(self, k):
        """
        插入新结点
        :param k:
        :return:
        """
        r = self.root
        if r.n >= 2 * self.t - 1:
            # 如果根结点已满，先拆分，再插入
            s = ALLOCATE_NODE(t=self.t)  # type: BNode
            self.root = s
            s.c[0] = r
            s.leaf = False
            self._split_node(s, 0)
            self._insert_non_full(s, k)
        else:
            # 直接按照非满规则插入
            self._insert_non_full(r, k)

    def delete(self, x, k):
        if k in x.keys:
            i = x.keys.index(k)

            if x.leaf:
                # 情况1：k存在于x中，且x为叶子结点
                x.del_key(i)
                return  # 成功删除k
            else:
                # 情况2：k存在于x中，且x为内部结点
                y = x.c[i]  # k的左子结点（简化表述）
                z = x.c[i + 1]  # k的右子结点（简化表述）
                if y.n > self.t - 1:
                    # 情况2a：k的左子结点至少包含t个关键字
                    # 解决方案：找到k在y为根的子树中的前驱k'，递归删除k'，并在x中使用k'替代k
                    x.keys[i] = y.keys[y.n - 1]
                    self.delete(y, y.keys[y.n - 1])
                elif z.n > self.t - 1:
                    # 情况2b：k的右子结点至少包含t个关键字
                    # 解决方案：找到k在y为根的子树中的后继k'，递归删除k'，并在x中使用k'替代k
                    x.keys[i] = z.keys[0]
                    self.delete(z, z.keys[0])
                else:
                    # 情况2c：y和z都只含有t-1个关键字
                    # 解决方案：将k和z都合并进y，这样x失去k和指向z的指针。然后释放z并递归从y中删除k
                    y.append_key(x.keys[i])

                    for key in [key for key in z.keys if key]:
                        y.append_key(key)
                    for c in [c for c in z.c if c]:
                        y.append_c(c)

                    x.del_key(i)
                    x.del_c(i + 1)
                    self.delete(y, k)
        else:
            if x.leaf:
                return  # k不在该树中

            # 找到k所属的子树
            i = x.n - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1

            if x.c[i].n == self.t - 1:
                ln = x.c[i - 1].n if i > 0 else -1
                rn = x.c[i + 1].n if i < x.n else -1

                if ln > self.t - 1:
                    # 情况3a(左)：x.c[i]只有t-1个关键字，相邻的左兄弟结点有至少t个关键字
                    # 解决方案：
                    #   1. x中的第i-1个关键字下降至x.c[i]，成为第一个关键字
                    #   2. x.c[i-1](x.c[i]的左兄弟结点)中的最后一个关键字提升至x，成为第i-1个关键字
                    #   3. 子结点再平衡，将x.c[i-1]的最后一个子结点指针，转移至x.c[i]，成为第一个子结点

                    # 将x的第i-1个key降至x.c[i]的第一个key
                    x.c[i].insert_key(0, x.keys[i - 1])

                    # x.c[i-1]的最后一个key提升至x的第i-1个key位置
                    x.keys[i - 1] = x.c[i - 1].keys[x.c[i - 1].n - 1]

                    # 删除x.c[i-1]的最后一个key
                    x.c[i - 1].pop_key()

                    # 相应的将x.c[i-1]的最后一个子结点指针转移至x.c[i]的第一个字节点指针位置
                    x.c[i].insert_c(0, x.c[i - 1].pop_c())
                elif rn > self.t - 1:
                    # 情况3a(右)：同如上3a(左)对称

                    # 将x的第i个关键字降至x.c[i]，成为最后一个关键字
                    x.c[i].append_key(x.keys[i])

                    # 将x.c[i+1](x.c[i]的右兄弟结点)中的第一个关键字提升至x，成为第i个关键字
                    x.keys[i] = x.c[i + 1].keys[0]

                    # 删除x.c[i+1]的第一个关键字
                    x.c[i + 1].del_key(0)

                    # 相应的将x.c[i+1]的第一个子结点的指针转移至x.c[i]，成为最后一个子结点
                    x.c[i].append_c(x.c[i + 1].c[0])

                    # 删除x.c[i+1]的第一个子结点指针
                    x.c[i + 1].del_c(0)
                else:
                    # 情况3b：x.c[i]只有t-1个关键字，且其相邻的兄弟结点都只有t-1个关键字
                    # 解决方案：x.c[i]与其中一个相邻的兄弟结点合并，x中的一个key降至新的结点，使之成为该结点的中间关键字

                    if ln > -1:
                        # 情况3b(左)

                        # 将x中的第i-1个关键字降至新结点，成为中间关键字
                        x.c[i - 1].append_key(x.keys[i - 1])

                        # 将x.c[i]合并进x.c[i-1]，形成新的结点
                        # 将x.c[i]的关键字合并进x.c[i-1]
                        for key in [key for key in x.c[i].keys if key]:
                            x.c[i - 1].append_key(key)
                        # 将x.c[i]的子结点指针合并进x.c[i-1]
                        for c in [c for c in x.c[i].c if c]:
                            x.c[i - 1].append_c(c)

                        # 删除x中的第i-1个关键字
                        x.del_key(i - 1)
                        # 删除x的第i个子结点指针
                        x.del_c(i)

                        # 目标子结点指向i-1
                        i -= 1
                    elif rn > -1:
                        # 情况3b(右)

                        # 将x中的第i个关键字降至新结点，成为中间关键字
                        x.c[i].append_key(x.keys[i])

                        # 将x.c[i+1]合并进x.c[i]，形成新的结点
                        # 将x.c[i+1]的关键字合并进x.c[i]
                        for key in [key for key in x.c[i + 1].keys if key]:
                            x.c[i].append_key(key)
                        # 将x.c[i+1]的子结点指针合并进x.c[i]
                        for c in [c for c in x.c[i + 1].c if c]:
                            x.c[i].append_c(c)

                        # 删除x中的第i个关键字
                        x.del_key(i)
                        # 删除x中的第i+1个子结点指针
                        x.del_c(i + 1)

            self.delete(x.c[i], k)

        if x.n <= 0:
            # 树根为空 降低树高
            x.n = x.c[0].n
            x.leaf = x.c[0].leaf
            x.keys = x.c[0].keys
            x.c = x.c[0].c


def search(x, k):
    """
    键搜索
    :param x:
    :param k:
    :return:
    """
    i = 0
    while i < x.n and k > x.keys[i]:
        i += 1
    if k == x.keys[i]:
        return x, i

    if x.leaf:
        return None, -1

    return search(x.c[i], k)


def minimum(x):
    while x.c[0]:
        x = x.c[0]
    return x, 0


def maximum(x):
    while x.c[x.n]:
        x = x.c[x.n]
    return x, x.n - 1


def predecessor(x, i):
    if x.leaf:
        if i == 1:
            return None, -1
        return x, i - 1
    return maximum(x.c[i])


def successor(x, i):
    if x.leaf:
        if i == x.n - 1:
            return None, -1
        return x, i + 1
    return minimum(x.c[i + 1])


def tree_print(x):
    print('-----------------------------------')
    keys = []
    current = [x]
    cs = []
    key_str = '|'
    while True:
        for item in current:
            keys.append([k for k in item.keys if k])
            if item.c:
                cs += [i for i in item.c if i]
        current = cs
        cs = []

        for key in keys:
            key_str += ','.join([str(i) for i in key]) + '|'
        print(key_str)
        keys = []
        key_str = '|'

        if len(current) <= 0:
            break

    print('-----------------------------------')
    print()


def ALLOCATE_NODE(t=3):
    """
    创建并初始化一个B-Tree结点
    :param t:
    :return:
    """
    return BNode(t)


def DISK_READ(x):
    """
    模拟磁盘读操作
    :param x:
    :return:
    """
    # print('Read "x" from disk!')
    pass


def DISK_WRITE(x):
    """
    模拟磁盘写操作
    :param x:
    :return:
    """
    # print('Write "x" to disk!')
    pass

