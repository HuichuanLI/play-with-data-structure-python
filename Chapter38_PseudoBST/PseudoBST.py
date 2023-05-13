import sys
import time


class PseudoBST:
    def __init__(self, range):
        self.number_count = [0] * (range + 1)
        self.range_count = [0] * (range + 1)
        self.range = range

    def pseudo_BST_insert(self, number):
        l, r = 0, self.range - 1
        while l <= r:
            mid = (l + r) // 2
            self.range_count[mid] += 1
            if mid == number:
                self.number_count[mid] += 1
                return
            elif mid > number:
                r = mid - 1
            else:
                l = mid + 1

    def pseudo_BST_delete(self, number):
        l, r = 0, self.range - 1
        while l <= r:
            mid = (l + r) // 2
            self.range_count[mid] -= 1
            if mid == number:
                self.number_count[mid] -= 1
                return
            elif mid > number:
                r = mid - 1
            else:
                l = mid + 1

    def pseudo_BST_search(self, l, r, x, y):
        if l > r:
            return 0
        mid = (l + r) // 2
        if l == x and r == y:
            return self.range_count[mid]

        left_count, right_count = 0, 0
        if x < mid:
            left_count = self.pseudo_BST_search(l, mid - 1, x, min(mid - 1, y))
        if y > mid:
            right_count = self.pseudo_BST_search(mid + 1, r, max(mid + 1, x), y)

        res = left_count + right_count + (self.number_count[mid] if mid >= x and mid <= y else 0)
        return res


start_time = time.time()
input_file = open("/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/PseudoBST/data/2.in", "r")
output_file = open("/Users/lhc456/Desktop/c++/play-with-data-structure-CPP/PseudoBST/data/2.out", "w")
n = int(input_file.readline().split()[1])
range1 = 100000
pseudo_BST = PseudoBST(range1)

for i in range(n):
    line = input_file.readline().split()
    if len(line) == 0:
        break
    case_type = int(line[0])
    if case_type == 1:
        x = int(line[1])
        pseudo_BST.pseudo_BST_insert(x)
    elif case_type == 2:
        x = int(line[1])
        pseudo_BST.pseudo_BST_delete(x)
    elif case_type == 3:
        x, y = int(line[1]), int(line[2])
        output_file.write(str(pseudo_BST.pseudo_BST_search(0, range1 - 1, x, y)) + "\n")

end_time = time.time()
print("Total time: {:.3f}(s)".format(end_time - start_time))
