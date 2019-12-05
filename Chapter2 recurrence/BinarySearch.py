import random


def random_list(start, end, length):
    data_list = []
    for i in range(length):
        data_list.append(random.randint(start, end))
    return data_list


def search(data_list, target):
    left = 0
    right = len(data_list) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if data_list[mid] == target:
            print("查找到数据，所在数据:{}".format(mid))
            return 0
        elif data_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print("找不到".format(target))
    return -1


def search2(data_list, left, right, target):
    if left > right:
        print("找不到")
        return -1
    mid = int((left + right) / 2)
    if data_list[mid] == target:
        print("查找到数据，所在数据:{}".format(mid))
        return mid
    elif data_list[mid] > target:
        return search2(data_list, left, mid - 1, target)
    else:
        return search2(data_list, mid + 1, right, target)


if __name__ == "__main__":
    data = random_list(1, 100, 10)
    data = sorted(data)
    target = random.randint(0, len(data) - 1)

    search(data, data[target])
    search2(data, 0, len(data) - 1, data[target])
