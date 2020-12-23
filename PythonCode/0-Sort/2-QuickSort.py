'''快速排序'''

def QuickSort(nums, start, end):
    if start < end:
        i, j = start, end
        base = nums[i]
        while i < j:
            while i < j and nums[j] >= base:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= base:
                i += 1
            nums[j] = nums[i]
        nums[i] = base
        QuickSort(nums, start, i - 1)
        QuickSort(nums, i+1, end)

nums = [9,4,10,8,13,2,15,7]
QuickSort(nums, 0, len(nums)-1)
print(nums)
