'''冒泡排序'''

"""
def BubbleSort(nums):
    listLength = len(nums)
    while listLength > 0:
        for i in range(listLength - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        listLength -= 1
    return nums
"""

def BubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 16,1]
print(BubbleSort(nums))
