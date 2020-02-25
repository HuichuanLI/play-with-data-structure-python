from collections import defaultdict


class Trie:
    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = defaultdict(None)

    def __init__(self):
        self._root = self._Node()
        # Trie中有多少个单词
        self._size = 0

    def get_size(self):
        return self._size

    # 添加一个字符串
    def add(self, word):
        cur = self._root
        for i in range(len(word)):
            c = word[i]
            if not cur.next.get(c):
                cur.next[c] = self._Node()
            cur = cur.next[c]
        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    def contains(self, word):
        cur = self._root
        for i in range(len(word)):
            c = word[i]
            if not cur.next.get(c):
                return False
            cur = cur.next[c]
        if cur.is_word:
            return True
        else:
            return False

    def is_prefix(self, prefix):
        cur = self._root
        for i in range(len(word)):
            c = word[i]
            if not cur.next.get(c):
                return False
            cur = cur.next[c]
        return True


if __name__ == '__main__':
    trie = Trie()
    words = ['panda', 'pandas', 'apple', 'app', 'banana']
    for word in words:
        trie.add(word)

    print('panda', trie.contains('panda'))
    print('apple', trie.contains('apple'))

    print('pan', trie.contains('pan'))
    print('pana', trie.is_prefix('pana'))
    print('zzz', trie.contains('zzz'))
