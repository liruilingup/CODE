'''k种面值的硬币，一个总金额amount，最少需要几枚硬币凑出这个金额'''


'''方法1：暴力递归。选择方式，画出递归树'''
def CoinChange(coins, amount):

    # 定义要凑出来的金额，至少需要dp(n)枚硬币
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        # 做选择，选择需要硬币最少的那个结果
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem == -1:continue
            res = min(res, 1+subproblem)
        return res if res != float('INF') else -1
    return dp(amount)
coins = [1,2,5]
amount = 11
print('暴力递归的方法', CoinChange(coins, amount))

'''方法2：使用备忘录的递归方法'''
def CoinChangeMemo(coins, amount):
    memo = dict()
    def dp(n):
        if n in memo:return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem == -1: continue
            res = min(res, 1+subproblem)
        memo[n] = res if res != float('INF') else -1
        return memo[n]
    return dp(amount)
print('使用备忘录的递归方法', CoinChangeMemo(coins, amount))

'''方法3：使用动态规划的方法'''
def CoinChangeDp(coins, amount):
    dp = [amount+1] * (amount+1)  # 初始化
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[-1] if dp[amount] != (amount + 1) else -1 # 判断根据初始化
print('使用动态规划的方法', CoinChangeDp(coins, amount))

