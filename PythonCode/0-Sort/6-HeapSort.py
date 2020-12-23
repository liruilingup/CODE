'''堆排序'''
def HeapBuild(nums):
    l = len(nums) - 1
    # 构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
    for i in range(len(nums)//2 - 1, -1, -1):
        HeapSort(nums, i, l)
    # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆
    for j in range(l, -1, -1):
        nums[0], nums[j] = nums[j], nums[0]
        HeapSort(nums, 0, j-1)
    return nums


def HeapSort(nums, i, l):
    left, right = 2 * i + 1, 2 * i + 2  ## 左右子节点的下标
    index = i
    if left <= l and nums[i] < nums[left]:
        index = left

    if right <= l and nums[left] < nums[right] and nums[i] < nums[right]:
        index = right

    if index != i:
        nums[i], nums[index] = nums[index], nums[i]
        HeapSort(nums, index, l)

nums = [17, 13, 40 , 22, 31, 14, 33, 56, 24, 19 ,10, 41, 51, 42, 26]
print(HeapBuild(nums))