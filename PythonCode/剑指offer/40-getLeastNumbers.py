'''剑指 Offer 40. 最小的k个数'''
# 方法一、对所有元素进行排序，然后取出第K个元素
# 方法二、使用选择排序或者冒泡排序，进行K次选择，可得到第K大的数 时间复杂度：O(n*k)，是有序的
# 方法三、类快排、小顶堆(只是需要知道k个数，不一定有序)

'''类快排'''
# 随机选取枢纽，得到比枢纽小和比枢纽大两部分，若比枢纽大的部分数量等于K-1，返回当前枢纽；
# 若大于k-1，则在比枢纽大的部分继续查找，重复该过程

'''使用快排实现'''
def getLeastNumbers(arr, k):
    if not arr or not k: return []
    if len(arr) <= k: return arr
    # 使用快速排序
    start = 0
    end = len(arr) - 1
    index = 0

    while index != k-1 :
        # if index < k-1:
        #     start = index + 1  # 必须
        #     index = quicksort(arr, start, end)
        # if index > k-1:
        #     end = index - 1 # 必须
        #     index = quicksort(arr, start, end)
        index = quicksort(arr, start, end)
        if index < k-1:
            start = index + 1
        else:
            end = index - 1
    return arr[:k]

def quicksort(arr, start, end):
    # 没有if start < end
    i, j = start, end
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= base:
            i += 1
        arr[j] = arr[i]
    arr[i] = base
    return i

arr = [1,3,4,5,2,9]
k = 2
print('使用快排实现', getLeastNumbers(arr, k))


'''使用大顶堆实现'''
# 维护一个k大小的堆，堆顶元素是最大K个数中最小的一个。
# 时间复杂度：O(N*logK) 特点：当海量数据时，内存中可以只维持一个K的堆，

def HeapBuild(nums):
    l = len(nums) - 1
    # 构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
    for i in range(len(nums)//2 - 1, -1, -1):
        HeapSort(nums, i, l)
    # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆

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

def HeapgetLeastNumbers(nums, k):
    BigHeap = nums[:k]  # 维护一个大顶堆
    HeapBuild(BigHeap)
    for i in nums[k:]:
        if i < BigHeap[0]:
            BigHeap[0] = i
            HeapBuild(BigHeap)
    return BigHeap

nums = [17, 13, 40 , 22, 31, 14, 33, 56, 24, 19 ,10, 41, 51, 42, 26]
print('使用堆实现结果：', HeapgetLeastNumbers(nums, 8))


