'''归并排序'''

def MergeBuild(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    l1 = MergeBuild(left)
    l2 = MergeBuild(right)

    return MergeSort(l1, l2)

def MergeSort(left, right):
    res = []
    while len(left) and len(right):
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res
if __name__ == '__main__':
    nums = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 1,16]
    res = MergeBuild(nums)
    print(res)



