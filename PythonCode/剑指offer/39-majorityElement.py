# 方法一、排序
def majorityElement(nums):
    nums.sort()
    mid = len(nums) // 2
    return nums[mid]


# 方法二、摩尔投票法
def majorityElement(nums):
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

