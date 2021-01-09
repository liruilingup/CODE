def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]  # 第一个元素没有子数组
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)


nums = [-3, 1, 3, -1, 2, -4, 2]
print(maxSubArray(nums))