from random import randint


def RandomArray(max=5000, number=5000):
    list = [randint(-max, max) for x in range(max)]
    return list
