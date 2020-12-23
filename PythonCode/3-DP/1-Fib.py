'''使用暴力递归的方法'''
def Fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return Fib(n-1)+Fib(n-2)

'''使用备忘录的递归方法'''
def MemoFib(n):
    if n == 0:
        return 0
    memo = [0] * (n+1)  # 初始化0
    return helper(memo, n)

def helper(memo, n):
    if n == 1 or n == 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = helper(memo, n-1) + helper(memo, n-2)
    return memo[n]
print('备忘录的递归方法', MemoFib(10))

'''使用动态规划的方法'''
def DpFib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print('动态规划方法', DpFib(10))




