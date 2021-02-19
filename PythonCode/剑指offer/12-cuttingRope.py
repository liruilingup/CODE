'''剑指 Offer 14- I. 剪绳子'''

# 方法一、数学证明法
def cuttingRope1(n):
    if n <=3:return n-1
    a,b = n//3, n%3
    if b==0:return 3**a
    if b==1:return 4*(3**(a-1))
    if b==2:return 2*(3**a)


# 方法二、贪心
def cuttingRope1(n):
    if n <=3:return n-1
    if n == 4:return 4
    res = 1
    while n>=3:
        res *= 3
        n -= 3
    if n==0:
        return res
    elif n==1:
        res //= 3
        return 4*res
    else:
        return 2*res

# 方法三、动态规划
def cuttingRope2(n):
    dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
    dp[2] = 1  # 初始化
    for i in range(3, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
    return dp[n]

print('动态规划结果', cuttingRope2(2))


