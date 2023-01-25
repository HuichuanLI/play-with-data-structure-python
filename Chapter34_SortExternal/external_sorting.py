from LoserTree import LoserTree
import unittest

# 合并有序序列
def _merge(a, p, q, r, reverse=False):
    """
    合并有序序列
    将两个有序序列合并为一个新的有序序列
    “归并排序”辅助方法
    依次对比前后两部分的记录，按顺序合并进原序列
    :param a:
    :param p:
    :param q:
    :param r:
    :param reverse:
    :return:
    """
    # 哨兵
    sentry = float('-inf') if reverse else float('inf')

    # 获取前半部分有序序列
    l_a = [v for i, v in enumerate(a) if p <= i <= q]
    # 追加哨兵
    l_a.append(sentry)

    # 获取后半部分有序序列
    r_a = [v for i, v in enumerate(a) if q < i <= r]
    # 追加哨兵
    r_a.append(sentry)

    # 遍历l_a和l_b，对比两个序列中的记录，按顺序回写如原序列
    i, j, k = 0, 0, p
    while l_a[i] is not sentry or r_a[j] is not sentry:
        if l_a[i] > r_a[j] if reverse else l_a[i] < r_a[j]:
            a[k] = l_a[i]
            i += 1
        else:
            a[k] = r_a[j]
            j += 1
        k += 1


# 归并排序
def _merge_sort(a, p, r, reverse=False):
    """
    归并排序
    主要思想：将两个或两个以上的有序序列组合成一个新的有序序列
    该方法实现的是2路归并排序。主要操作是，递归的将待排序类均分为两部分，
    直到细分到每部分只有一条记录(一条记录天然有序)，然后逐层合并，最终得到有序序列。
    :param a:
    :param p:
    :param r:
    :param reverse:
    :return:
    """
    if p < r:
        # 均分待排序列
        q = (r + p) // 2

        # 递归排序前后两部分
        _merge_sort(a, p, q, reverse=reverse)
        _merge_sort(a, q + 1, r, reverse=reverse)

        # 前后两部分分别有序后，合并之
        _merge(a, p, q, r, reverse=reverse)


# 归并排序封装方法
def merge_sort(a, reverse=False):
    """
    归并排序封装方法
    :param a:
    :param reverse:
    :return:
    """
    _merge_sort(a, 0, len(a) - 1, reverse)


# 多路平衡归并排序
def multi_ways_balance_merge_sort(a):
    """
    多路平衡归并排序
    - 多用于外部排序
    - 使用多维数组模拟外部存储归并段
    - 使用loser tree来实现多路归并
    - 归并的趟数跟路数k成反比，增加路数k可以调高效率
    :param a:
    :return:
    """
    SENTRY = float('inf')  # 哨兵，作为归并段的结尾
    leaves = []  # 每个归并段中的一个元素构成loser tree的原始序列
    b = []  # 输出归并段，此实现中简化为以为数组。实际情况下也需要对输出分段。
    for v in a:
        merge_sort(v)  # 归并段内排序，采用归并排序
        v.append(SENTRY)  # 每个归并段追加哨兵
        leaves.append(v[0])  # 每个归并段的首元素构成初始化loser tree的原始序列
        del v[0]  # 删除各归并段的首元素
    lt = LoserTree(leaves)  # 构建loser tree
    # 循环获取winner
    while True:
        i, v = lt.winner  # winner
        if v == SENTRY:
            # 排序结束
            break

        b.append(v)  # 将winner写入输出归并段
        lt.modify_key(i, a[i][0])  # winner所在的归并段的下一个元素更新入loser tree
        del a[i][0]  # 删除已处理数据
    return b  # 返回有序序列


# 外部排序测试
class ExternalSortingTest(unittest.TestCase):
    def setUp(self):
        self.k = 6  # 内存工作区可容纳记录条数
        self.a = [51, 49, 39, 46, 38, 29, 14, 61, 15, 30, 1, 48, 52, 3, 63, 27, 4, 13, 89, 24, 46, 58, 33, 76]  # 原始待排序列
        self.b = [self.a[i: i + self.k] for i in range(0, len(self.a), self.k)]  # 拆分归并段

    # 多路平衡归并排序测试
    def test_multi_ways_balance_merge_sort(self):
        """
        多路平衡归并排序测试
        :return:
        """
        mwbms_result = multi_ways_balance_merge_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, mwbms_result, 'The list is NOT sorted after multi-ways balance merge sort!')
