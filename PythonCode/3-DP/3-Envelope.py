
'''354. 俄罗斯套娃信封问题'''

# 最长上升子序列的二维问题
def Envelope(envelopes):
    if not envelopes: return 0
    # 先对宽度进行升序排序，再对高度进行降序排列
    envelopes.sort(key=lambda x:(x[0], -x[1]))
    n = len(envelopes)
    height = []
    for i in range(n):
        height.append(envelopes[i][1])

    def LengthOfLIS(nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    return LengthOfLIS(height)

nums = [[5,4], [6,4], [6,7], [2,3]]
print(Envelope(nums))


