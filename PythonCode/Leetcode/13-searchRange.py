'''34. 在排序数组中查找元素的第一个和最后一个位置'''
def searchLeft(nums, target):
    i,j = 0,len(nums)-1
    while i <= j:
        mid = (i+j) // 2
        if nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1

    if i >=len(nums) or nums[i] != target:
        return -1
    return i

def searchRight(nums, target):
    i,j = 0, len(nums)-1
    while i <= j:
        mid = (i+j)//2
        if nums[mid] > target:
            j = mid-1
        elif nums[mid] < target:
            i = mid+1
        else:
            i = mid+1
    if j < 0 or nums[j] != target:
        return -1
    return j


def searchRange(nums, target):
    if not nums:return [-1, -1]

    return [searchLeft(nums, target), searchRight(nums, target)]

nums = [5,5,5,8,8,10]
target = 0
print(searchRange(nums, target))

