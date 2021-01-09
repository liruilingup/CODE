def exchange(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        while i < j and nums[i] & 1 == 1: i += 1
        while i < j and nums[j] & 1 == 0: j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return nums
nums = [1,2,3,4]
print(exchange(nums))