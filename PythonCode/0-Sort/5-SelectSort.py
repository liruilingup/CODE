'''选择排序'''
def SelectSort(nums):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums
nums = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 1,16]
print(SelectSort(nums))