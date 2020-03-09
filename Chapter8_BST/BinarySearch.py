def BinarySearch(alist, target):
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid = first + (last - first) // 2
        if alist[mid] == target:
            return True
        else:
            if alist[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
    return False


def binarySearchRecursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binarySearchRecursion(alist[mid + 1:], item)
        else:
            return binarySearchRecursion(alist[:mid], item)


if __name__ == "__main__":
    Bs = BinarySearch([1, 2, 3, 4, 5], 2)
    print(Bs)
