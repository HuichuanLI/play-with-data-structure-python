class BPNode(object):
    """
    B+Tree 结点
    """
    # 关键字
    keys = []
    # 卫星数据，仅限叶子结点
    values = None
    # 子结点
    c = []
    # 关键字数量
    n = 0
    # 是否为叶子结点
    is_leaf = False
    # 下一结点指针，仅限叶子结点
    next = None

    def __init__(self, t=5, is_leaf=False):
        self.keys = [None] * (2 * t - 1)
        self.c = [None] * (2 * t - 1)
        self.is_leaf = is_leaf
        if self.is_leaf:
            self.values = [None] * (2 * t - 1)

    def insert_key(self, i, k):
        """
        插入关键字
        :param i:
        :param k:
        :return:
        """
        j = self.n - 1
        while j >= i:
            self.keys[j + 1] = self.keys[j]
            j -= 1
        self.keys[i] = k
        self.n += 1

    def insert_value(self, i, v):
        """
        插入卫星数据
        :param i:
        :param v:
        :return:
        """
        j = len([value for value in self.values if value is not None]) - 1
        while j >= i:
            self.values[j + 1] = self.values[j]
            j -= 1

        self.values[i] = v

    def insert_c(self, i, cn):
        """
        插入子结点
        :param i:
        :param cn:
        :return:
        """
        j = len([c for c in self.c if c]) - 1
        while j >= i:
            self.c[j + 1] = self.c[j]
            j -= 1
        self.c[i] = cn

    def append_key(self, k):
        """
        追加关键字
        :param k:
        :return:
        """
        self.keys[self.n] = k
        self.n += 1

    def append_value(self, v):
        """
        追加卫星数据
        :param v:
        :return:
        """
        idx = len([value for value in self.values if value is not None])
        self.values[idx] = v

    def append_c(self, cn):
        """
        追加子结点
        :param cn:
        :return:
        """
        idx = len([c for c in self.c if c])
        self.c[idx] = cn

    def del_key(self, i):
        """
        删除指定位置关键字，并返回该关键字
        :param i:
        :return:
        """
        key = self.keys[i]
        while i < self.n - 1:
            self.keys[i] = self.keys[i + 1]
            i += 1
        self.pop_key()
        return key

    def del_value(self, i):
        """
        删除指定位置卫星数据，并返回该数据
        :param i:
        :return:
        """
        value = self.values[i]
        idx = len([value for value in self.values if value is not None]) - 1
        while i < idx:
            self.values[i] = self.values[i + 1]
            i += 1
        self.pop_value()
        return value

    def del_c(self, i):
        """
        删除指定位置子结点，并返回该子结点
        :param i:
        :return:
        """
        c = self.c[i]
        idx = len([c for c in self.c if c]) - 1
        while i < idx:
            self.c[i] = self.c[i + 1]
            i += 1
        self.pop_c()
        return c

    def pop_key(self):
        """
        弹出关键字
        :return:
        """
        key = self.keys[self.n - 1]
        self.keys[self.n - 1] = None
        self.n -= 1
        return key

    def pop_value(self):
        """
        弹出卫星数据
        :return:
        """
        idx = len([value for value in self.values if value is not None]) - 1
        value = self.values[idx]
        self.values[idx] = None
        return value

    def pop_c(self):
        """
        弹出子结点
        :return:
        """
        idx = len([c for c in self.c if c]) - 1
        c = self.c[idx]
        self.c[idx] = None
        return c


class BPTree(object):
    """
    B+Tree
    """
    # 根结点
    root = None
    # 数据链表头
    head = None

    def __init__(self, t=3):
        self.t = t
        self.create()

    def create(self):
        """
        创建B+Tree
        :return:
        """
        x = ALLOCATE_NODE(t=self.t, is_leaf=True)
        DISK_WRITE(x)
        self.root = x
        self.head = x

    def tree_walk(self):
        """
        B+Tree遍历，基于数据链表
        :return: 关键字列表
        """
        keys = []
        p = self.head
        while p:
            keys += [key for key in p.keys if key is not None]
            p = p.next
        return keys

    def _split_node(self, x, i):
        """
        拆分结点
        当结点关键字满时，将结点拆分为两个新结点。
        左新结点持有原结点前t-1个数据，右新结点持有原结点后t个数据。
        :param x: 父结点
        :param i: 子结点索引
        :return:
        """
        y = x.c[i]  # 原结点
        z = ALLOCATE_NODE(t=self.t, is_leaf=y.is_leaf)  # 新建结点

        # 将后t个数据转移到新结点中
        for _ in range(self.t):
            z.insert_key(0, y.pop_key())
            z.insert_c(0, y.pop_c())
            if y.is_leaf:
                z.insert_value(0, y.pop_value())

        # 在父结点中注册新结点
        x.insert_key(i + 1, z.keys[0])
        x.insert_c(i + 1, z)

        # 如果结点是叶子结点，维护数据链表
        if y.is_leaf:
            z.next, y.next = y.next, z

        # 数据变动写入磁盘
        DISK_WRITE(x)
        DISK_WRITE(y)
        DISK_WRITE(z)

    def _merge_node(self, x, i):
        """
        合并结点
        当结点的仅有t-1个关键字，且左结点或右结点也仅有t-1个关键字时，将两个结点合并。
        :param x: 父结点
        :param i: 子结点索引
        :return: 合并成功，返回True；否则，返回False。
        """
        # 原结点
        y = x.c[i]  # type:BPNode
        # 左兄弟结点，如果原结点为最左侧结点，则不存在左兄弟结点
        l_bro = x.c[i - 1] if i > 0 else None  # type:BPNode
        # 右兄弟结点，同上
        r_bro = x.c[i + 1] if i < x.n - 1 else None  # type:BPNode

        # 优先左兄弟结点
        if l_bro and l_bro.n <= self.t - 1:
            '''
            情况1：如果存在左兄弟结点，且左兄弟结点仅有t-1个关键字，则与左兄弟结点合并
            '''
            # 将原结点数据合并入左兄弟结点
            while y.n > 0:
                l_bro.append_key(y.del_key(0))
                l_bro.append_c(y.del_c(0))
                if y.is_leaf:
                    l_bro.append_value((y.del_value(0)))

            # 如果为叶子结点，维护数据链表
            if y.is_leaf:
                l_bro.next = y.next

            # 在父结点中删除原结点关键字分割和指针
            x.del_key(i)
            x.del_c(i)

            DISK_WRITE(x)
            DISK_WRITE(y)
            DISK_WRITE(l_bro)

            return True
        elif r_bro and r_bro.n <= self.t - 1:
            '''
            情况2：如果存在右兄弟结点，且右兄弟结点仅有t-1个关键字，则与右兄弟结点合并
            '''
            # 操作同情况1对称
            while r_bro.n > 0:
                y.append_key(r_bro.del_key(0))
                y.append_c(r_bro.del_c(0))
                if y.is_leaf:
                    y.append_value(r_bro.del_value(0))

            if y.is_leaf:
                y.next = r_bro.next

            x.del_key(i + 1)
            x.del_c(i + 1)

            DISK_WRITE(x)
            DISK_WRITE(y)
            DISK_WRITE(r_bro)

            return True
        '''
        情况3：情况1和情况2都不满足，合并失败
        '''
        return False

    def _rotation(self, x, i):
        """
        关键字旋转
        当结点的关键字满时，检查相邻兄弟结点是否有空余位置；
        如果有则将一部分关键字转移到相邻兄弟结点，优先左兄弟结点。
        该操作有助于减少高消耗的结点拆分操作。
        :param x: 父结点
        :param i: 子结点索引
        :return:
        """
        # 目标结点
        r = x.c[i]  # type: BPNode

        # 左右兄弟结点
        l_bro = x.c[i - 1] if i > 0 else None  # type: BPNode
        r_bro = x.c[i + 1] if i < x.n - 1 else None  # type: BPNode

        '''
        无限旋转的坑：
        问题描述：当目标结点为满结点，相邻兄弟结点只有一个空余位置，且旋转处于两结点之间的边界关键字时，会出现两个相邻兄弟结点相互旋转的死循环
        示例： t=2，[1,2]  [3,5,6], 后者为目标结点，做插入关键字"4"的操作。
                定位结点索引为"1"， 关键字"3"做左旋，结果为[1,2,3]  [5,6]；此时重新定位结点索引为"0"，需要关键字"3"做右旋，此时回到原始状态。如此陷入死循环。
        解决方案：需要保证兄弟结点至少有两个空位置才进行旋转
        '''
        if l_bro and l_bro.n < 2 * self.t - 2:
            '''
            情况1：左兄弟结点存在，且左兄弟结点有至少两个空余位置
            '''
            # 目标结点第一个数据左旋
            l_bro.append_key(r.del_key(0))
            l_bro.append_c(r.del_c(0))
            if r.is_leaf:
                l_bro.append_value(r.del_value(0))

            # 更新父结点分割边界
            x.keys[i] = x.c[i].keys[0]

            DISK_WRITE(r)
            DISK_WRITE(l_bro)

            return True
        elif r_bro and r_bro.n < 2 * self.t - 2:
            '''
            情况2：右兄弟结点存在，且右兄弟结点有至少两个空余位置
            '''
            # 操作与情况1对称
            r_bro.insert_key(0, r.pop_key())
            r_bro.insert_c(0, r.pop_c())
            if r.is_leaf:
                r_bro.insert_value(0, r.pop_value())
            x.keys[i + 1] = x.c[i + 1].keys[0]

            DISK_WRITE(r)
            DISK_WRITE(r_bro)

            return True

        '''
        情况3：情况1和情况2均不满足，旋转失败。
        '''
        return False

    def _de_rotation(self, x, i):
        """
        关键字逆旋转，旋转操作的逆操作
        当结点仅有t-1个关键字时，检查相邻兄弟结点是否有多于t-1个关键字；
        如果有，则从相邻兄弟结点转移一部分关键字到该结点，优先左兄弟结点。
        该操作有助于减小高消耗的结点合并操作.
        :param x:
        :param i:
        :return:
        """
        # 操作与旋转操作对称
        r = x.c[i]  # type:BPNode
        l_bro = x.c[i - 1] if i > 0 else None  # type: BPNode
        r_bro = x.c[i + 1] if i < x.n - 1 else None  # type: BPNode

        if l_bro and l_bro.n > self.t - 1:
            r.insert_key(0, l_bro.pop_key())
            r.insert_c(0, l_bro.pop_c())
            if r.is_leaf:
                r.insert_value(0, l_bro.pop_value())
            x.keys[i] = x.c[i].keys[0]

            DISK_WRITE(r)
            DISK_WRITE(l_bro)

            return True
        elif r_bro and r_bro.n > self.t - 1:
            r.append_key(r_bro.del_key(0))
            r.append_c(r_bro.del_c(0))
            if r.is_leaf:
                r.append_value(r_bro.del_value(0))
            x.keys[i + 1] = x.c[i + 1].keys[0]

            DISK_WRITE(r)
            DISK_WRITE(r_bro)

            return True
        return False

    def _insert_non_full(self, x, k, v):
        """
        非满结点插入操作，辅助B+Tree插入操作。
        :param x: 根结点
        :param k: 关键字
        :param v: 卫星数据
        :return:
        """
        if x.is_leaf:
            '''
            情况2：结点为叶子结点，直接插入关键字
            '''
            # 定位k应该插入的位置索引
            i = x.n - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1

            # 插入关键字和卫星数据
            x.insert_key(i, k)
            x.insert_value(i, v)
        else:
            '''
            情况1： 结点为内部结点
            '''
            # 如果k小于现有最小值，则k称为最小值
            if k < x.keys[0]:
                x.keys[0] = k

            # 定位k应该插入的位置索引
            i = x.n - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1

            if x.c[i].n >= 2 * self.t - 1:
                '''
                情况1a：结点x已满
                解决方案：对结点x先做旋转操作，如果失败，再做结点拆分操作
                '''
                if not self._rotation(x, i):
                    self._split_node(x, i)

                # 递归插入，直到叶子结点
                self._insert_non_full(x, k, v)
            else:
                '''
                情况1b：结点x未满，直接插入
                '''
                self._insert_non_full(x.c[i], k, v)

    def insert(self, k, v):
        """
        插入操作
        :param k: 关键字
        :param v: 卫星数据
        :return:
        """
        r = self.root

        if r.n >= 2 * self.t - 1:
            # 如果根结点已满，先做拆分操作和升高操作
            s = ALLOCATE_NODE(t=self.t, is_leaf=False)
            self.root = s
            s.c[0] = r
            s.insert_key(0, r.keys[0])
            self._split_node(s, 0)
            DISK_WRITE(s)

        self._insert_non_full(self.root, k, v)

    def delete(self, x, k):
        """
        删除操作，递归实现
        :param x: 根结点
        :param k: 关键字
        :return:
        """
        # 定位k的位置索引
        i = x.n - 1
        while i >= 0 and k < x.keys[i]:
            i -= 1

        if x.is_leaf:
            '''
            情况2：结点为叶子结点
            '''
            idx = x.keys.index(k)
            if idx > -1:
                # 如果存在关键字，删除关键字和卫星数据
                x.del_key(idx)
                x.del_value(idx)
        else:
            '''
            情况2：结点为内部结点
            '''
            if i < 0:
                # k小于树的最小值，说明key不在该树中
                return

            if x.c[i].n <= self.t - 1:
                '''
                情况2a：结点x仅有t-1个关键字
                解决方案：对结点x，先做逆旋转操作，如果失败，再做合并结点操作。
                '''
                if not self._de_rotation(x, i):
                    self._merge_node(x, i)
                    if i > x.n - 1 or k < x.keys[i]:
                        i -= 1

            # 如果k刚好是分割关键字，使用其后继代替之
            if k == x.keys[i]:
                y, j = successor(x, i)
                x.keys[i] = y.keys[j]

            # 递归删除
            self.delete(x.c[i], k)


def search(x, k):
    """
    搜索B+Tree
    :param x: 根结点
    :param k: 关键字
    :return: (目标结点, 目标关键字索引)
    """
    # 定位k的位置索引
    i = x.n - 1
    while i >= 0 and k < x.keys[i]:
        i -= 1

    if i < 0:
        # 如果k小于树的最小值，关键字不存在
        return None, -1

    if x.is_leaf:
        # 如果是叶子结点，直接定位关键字
        if k == x.keys[i]:
            return x, i
        else:
            return None, -1

    # 递归搜索
    return search(x.c[i], k)


def minimum(x):
    """
    B+Tree最小关键字
    :param x:
    :return:
    """
    while x.c[0]:
        x = x.c[0]
    return x, 0


def maximum(x):
    """
    B+Tree最大关键字
    :param x:
    :return:
    """
    while x.c[x.n - 1]:
        x = x.c[x.n - 1]
    return x, x.n - 1


def predecessor(x, i):
    """
    关键字前驱
    :param x:
    :param i:
    :return:
    """
    if x.is_leaf:
        if i <= 0:
            return None, -1
        return x, i - 1
    return maximum(x.c[i])


def successor(x, i):
    """
    关键字后继
    :param x:
    :param i:
    :return:
    """
    if x.is_leaf:
        if i >= x.n - 1:
            return None, -1
        return x, i + 1
    y, j = minimum(x.c[i])
    return y, j + 1


def ALLOCATE_NODE(t=3, is_leaf=False):
    """
    申请新的结点
    :param t:
    :param is_leaf:
    :return:
    """
    return BPNode(t=t, is_leaf=is_leaf)


def DISK_READ(x):
    """
    模拟磁盘读操作
    :param x:
    :return:
    """
    pass


def DISK_WRITE(x):
    """
    模拟磁盘写操作
    :param x:
    :return:
    """
    pass
