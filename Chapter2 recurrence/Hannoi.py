def move(index, start, mid, end):
    if index == 1:
        print("{}-->{}".format(start, end))
    else:
        # 先移动index-1 放到mid
        move(index - 1, start, end, mid)
        print("{}-->{}".format(start, end))
        move(index - 1, mid, start, end)


# 1.递归本生生调用的时间和空间消耗，效率比较低
# 2.递归中很多的计算都是重复的，可以通过缓存
# 3。调用栈可能会溢出，其实每次调用都使用内存，而没个进程的栈其实有容量大小，有限制。

if __name__ == "__main__":
    move(5, "A", "B", "C")
