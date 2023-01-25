class CompleteBinaryTree(object):
    @staticmethod
    def parent(i):
        return (i - 1) >> 1

    @staticmethod
    def left(i):
        return (i << 1) + 1

    @staticmethod
    def right(i):
        return (i << 1) + 2
