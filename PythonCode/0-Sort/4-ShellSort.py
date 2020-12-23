'''希尔排序'''
#①第一层循环 gap折半 直到gap=1
#②二层三层循环直接插入排序
def ShellSort(nums):
    gap = len(nums) // 2
    while gap >= 1:
        for i in range(gap, len(nums)):
            for j in range(i-gap, -1, -gap):
                if nums[j] > nums[j+gap]:
                    nums[j], nums[j+gap] = nums[j+gap], nums[j]
        gap = gap // 2
    return nums
nums = [9,4,10,8,13,2,15,7]
print(ShellSort(nums))
