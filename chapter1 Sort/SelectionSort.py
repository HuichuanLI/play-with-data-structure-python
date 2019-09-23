def selectionSort(alist):
    for i in range(len(alist)):
        minposition = i
        for j in range(i, len(alist)):
            if alist[minposition] > alist[j]:
                minposition = j
        alist[i], alist[minposition] = alist[minposition], alist[i]
    return alist


if __name__ == "__main__":
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = selectionSort(a)
    for w in a:
        print(w)
