'''堆排序'''
# 最大堆总是将其中的最大值存放在树的根节点。
# 而对于最小堆，根节点中的元素总是树中的最小值
# 应用场景
# 比如求10亿个数中的最大的前10个数，时时构建只有10个元素的小顶堆，如果比堆顶小，则不处理；如果比堆顶大，则替换堆顶，然后依次下沉到适当的位置。
# 比如求10亿个数中的最小的前10个数，时时构建只有10个元素的大顶堆，如果比堆顶大，则不处理；如果比堆顶小，则替换堆顶，然后依次下沉到适当的位置。
# 一般升序采用大顶堆，降序采用小顶堆

'''构造大顶堆'''
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
    left, right = 2 * i + 1, 2 * i + 2  # 左右子节点的下标
    index = i
    # 构造大顶推
    if left <= l and nums[i] < nums[left]:
        index = left

    if right <= l and nums[left] < nums[right] and nums[i] < nums[right]:
        index = right

    if index != i:
        nums[i], nums[index] = nums[index], nums[i]
        HeapSort(nums, index, l)

nums = [17, 13, 40 , 22, 31, 14, 33, 56, 24, 19 ,10, 41, 51, 42, 26]
print('使用大顶堆排序：', HeapBuild(nums))

'''构造小顶堆'''
def SmallHeapBuild(nums):
    l = len(nums) - 1
    # 从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
    for i in range(len(nums)//2 - 1, -1, -1):
        SmallHeapSort(nums, i, l) # 小顶堆构造函数

    # 上面的循环完成了小顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆
    # 使用小顶堆进行降序，nums[0]是最小的，放到最后
    for j in range(l, -1 ,-1):
        nums[0], nums[j] = nums[j], nums[0]
        SmallHeapSort(nums, 0, j-1)
    return nums

def SmallHeapSort(nums, i, l):
    left, right = 2 * i + 1, 2 * i + 2  # 左右子节点的下标
    index = i
    # 构建小顶堆
    if left <= l and nums[i] > nums[left]:
        index = left

    if right <= l and nums[left] > nums[right] and nums[i] > nums[right]:
        index = right

    if index != i:
        nums[i], nums[index] = nums[index], nums[i]
        SmallHeapSort(nums, index, l)

nums = [17, 13, 40 , 22, 31, 14, 33, 56, 24, 19 ,10, 41, 51, 42, 26]
print('使用小顶堆倒排序', SmallHeapBuild(nums))
