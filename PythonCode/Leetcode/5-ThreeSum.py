'''15. 三数之和，为0'''
nums = [-1, 0, 1, 2, -1, -4]
def threeSum(nums):
    nums.sort()
    print('排序后的：', nums)
    n = len(nums)
    res = []

    for i in range(n - 2):
        if nums[i] > 0:break
        if i > 0 and nums[i] == nums[i-1]:continue

        left = i+1
        right = n-1
        while left < right:
            sum = nums[left] + nums[right] + nums[i]
            if sum < 0:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif sum > 0:
                right -= 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return res

print('三个数字之后相加', threeSum(nums))

