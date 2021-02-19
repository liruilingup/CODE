'''518. 零钱兑换 II'''
'''给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个'''
'''
凑成总金额的硬币组合数
使用二维dp
金额是0,硬币是0,方案是1,dp[0][0]=1
金额是0,硬币不是0,方案是1,dp[i][0]=1
金额不是0，硬币是0，方案是0,dp[0][j]=0
选择方案是:dp[i][j]=装+不装
'''

def change(amount, coins):
    # base case
    # 金额是0，只有个1种方法
    # 没有硬币，只有0种方法
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        dp[i][0] = 1

    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j - coins[i - 1] < 0:
                # 没法装
                dp[i][j] = dp[i - 1][j]
            else:
                # dp[i][j] = 不装 + 装
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
    return dp[-1][-1]

amount = 5
coins = [1, 2, 5]
print(change(amount, coins))