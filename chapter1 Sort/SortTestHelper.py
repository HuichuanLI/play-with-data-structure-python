from random import randint


def RandomArray(max=5000, number=5000):
    list = [randint(-max, max) for x in range(number)]
    return list


def NearlyOrderArray(swap_times=100, number=5000):
    lista = []
    for i in range(number + 1):
        lista.append(i)
    for j in range(swap_times):
        index1 = randint(0, number)
        index2 = randint(0, number)
        lista[index1], lista[index2] = lista[index2], lista[index1]
    return lista
