# 希尔排序，又叫“缩小增量排序”，是对插入排序进行优化后产生的一种排序算法。它的执行思路是：把数组内的元素按下标增量分组，对每一组元素进行插入排序后，缩小增量并重复之前的步骤，直到增量到达1。
# 一般来说，希尔排序的时间复杂度在O(n^1.3))到O(n^2)之间，这视增量大小而定。希尔排序的空间复杂度是O(1)O(1)，它是一个不稳定的排序算法。进行希尔排序时，元素一次移动可能跨越多个元素，从而可能抵消多次移动，提高了效率。

nums = [5, 3, 6, 4, 1, 2, 8, 7]


def ShellSort(nums):
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)):
            index = i
            while index >= step and nums[index] <= nums[index - step]:
                nums[index], nums[index - step] = nums[index - step], nums[index]
                index -= step
        step //= 2
    return nums


nums = ShellSort(nums)

print(nums)
