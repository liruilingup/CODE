'''最长上升子序列'''
# Longest Increasing Subsequence
def LengthOfLIS(nums):
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j]+1,dp[i])
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print('最长上升子序列', LengthOfLIS(nums))

