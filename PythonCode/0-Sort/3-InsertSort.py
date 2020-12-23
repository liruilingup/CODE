'''插入排序'''

def InsertSort(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            while i>=0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i -= 1
    return nums
nums = [9,4,10,8,13,2,15,7]
print(InsertSort(nums))
