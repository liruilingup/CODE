# 第k个大的元素和最大的K个元素
# 两个相同的算两个，就是一样的
'''215. 数组中的第K个最大元素'''
'''使用堆方法'''

# 第k个大的元素，建立小顶堆， k个元素里面最小的
def FindKthLargest(nums, k):
    arr = nums[:k]
    HeapBild(arr)
    for i in nums[k:]:
        if i > arr[0]: # 每一次把最小的元素去掉
            arr[0] = i
            HeapBild(arr)
    return arr[0]

def HeapBild(nums):
    l = len(nums) - 1
    for i in range(len(nums) // 2 - 1, -1, -1):
        HeapSort(nums, i, l)
    return nums

def HeapSort(nums, i, n):
    left = 2*i + 1
    right = 2*i + 2
    index = i

    if left <= n and nums[i] > nums[left]:
        index = left
    if right <= n and nums[left] > nums[right] and nums[i] > nums[right]:
        index = right
    if index != i:
        nums[i], nums[index] = nums[index], nums[i]
        HeapSort(nums, index, n)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print('使用小顶堆实现：', FindKthLargest(nums, k))

'''方法二、使用快排实现'''
def QuickFindKthLargest(nums, k):
    k = len(nums) - k #第k大=第len(nums)-k小
    l, r = 0, len(nums) - 1
    # while True:
    #     idx = partition(l, r)
    #     if idx == k:
    #         return nums[idx]
    #     elif idx < k:
    #         l = idx + 1
    #     else:
    #         r = idx - 1
    idx = partition(l, r)
    while idx != k:
        idx = partition(l, r)
        if idx < k:
            l = idx + 1
        else:
            r = idx - 1

    return nums[k]

def partition(l, r):
    pivot = l
    while l < r:
        while l < r and nums[r] >= nums[pivot]: r -= 1
        while l < r and nums[l] <= nums[pivot]: l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[pivot] = nums[pivot], nums[l]
    return l
print('使用快排实现：', QuickFindKthLargest(nums, k))
