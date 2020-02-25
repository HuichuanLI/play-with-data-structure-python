from BSTSet import BSTSet

from Trie import Trie

if __name__ == '__main__':
    words = ''
    with open('./shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time
    print("BST-SET")
    start_time = time()
    bst_set = BSTSet()
    for word in words:
        bst_set.add(word)

    for word in words:
        bst_set.contains(word)

    print('Total words: ', len(words))
    print('Unique words: ', bst_set.get_size())
    print('Contains word "they": ', bst_set.contains('they'))
    ## 耗时0.58秒左右
    print('Total time: {} seconds'.format(time() - start_time))

    print("Trie")
    start_time = time()
    trie = Trie()
    for word in words:
        trie.add(word)

    for word in words:
        trie.contains(word)

    print('Total words: ', len(words))
    print('Unique words: ', trie.get_size())
    print('Contains word "they": ', trie.contains('they'))
    ## 耗时0.58秒左右
    print('Total time: {} seconds'.format(time() - start_time))
