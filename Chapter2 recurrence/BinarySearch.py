data = [1, 7, 17, 18, 27, 29, 30, 35, 39, 41, 63, 66, 67, 78, 82, 91, 92]


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


if __name__ == "__main__":
    search(data, 78)
