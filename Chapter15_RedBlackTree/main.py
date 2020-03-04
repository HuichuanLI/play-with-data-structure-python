from time import time

from Chapter9_SET_MAP.BSTMap import BSTMap
from Chapter14_AVL.avl_map import AVLMap
from RBTree import RBTree

if __name__ == '__main__':
    words = ''
    with open('./shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time()
    bst_map = BSTMap()
    for word in words:
        if bst_map.contains(word):
            bst_map.setter(word, bst_map.getter(word) + 1)
        else:
            bst_map.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', bst_map.get_size())
    print('Contains word "they": ', bst_map.contains('they'))
    ## 耗时1.23秒左右
    print('BSTMap Total time: {} seconds'.format(time() - start_time))

    bst_map.remove('they')
    print(bst_map.contains('they'))
    bst_map.setter('they', 100)
    print(bst_map.getter('they'))

    print('*' * 20)

    start_time = time()
    avl_tree = AVLMap()
    for word in words:
        if avl_tree.contains(word):
            avl_tree.setter(word, avl_tree.getter(word) + 1)
        else:
            avl_tree.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', avl_tree.get_size())
    print('Contains word "they": ', avl_tree.contains('they'))
    ## 耗时1.23秒左右
    print('AVL Total time: {} seconds'.format(time() - start_time))

    avl_tree.remove('they')
    print(avl_tree.contains('they'))
    # avl_tree.setter('they', 100)
    # print(avl_tree.getter('they'))

    print('*' * 20)

    start_time = time()
    rb_tree = RBTree()
    for word in words:
        if rb_tree.contains(word):
            rb_tree.setter(word, rb_tree.getter(word) + 1)
        else:
            rb_tree.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', rb_tree.get_size())
    print('Contains word "they": ', rb_tree.contains('they'))
    ## 耗时1.23秒左右
    print('RBTree Total time: {} seconds'.format(time() - start_time))

    rb_tree.remove('they')
    print(rb_tree.contains('they'))
    rb_tree.setter('they', 100)
    print(rb_tree.getter('they'))
