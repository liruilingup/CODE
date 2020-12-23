'''二分查找'''
def BinarySearch(target, nums):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return 'target in nums'
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 'target not in nums'
nums = [2, 4, 7, 8, 9, 10, 13, 15, 19]
print(BinarySearch(13, nums))
print(BinarySearch(20, nums))
