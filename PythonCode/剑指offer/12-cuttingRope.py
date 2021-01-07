'''剑指 Offer 14- I. 剪绳子'''

def cuttingRope(n):
    dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
    dp[2] = 1  # 初始化
    for i in range(3, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
    return dp[n]

print(cuttingRope(2))
