
'''0-1背包问题'''
# 只能使用一次，求出来这个包最多能装的价值
def bag(number, capacity, weight, value):
    dp = [[0 for _ in range(capacity+1)] for _ in range(number+1)]

    for i in range(1, number+1): # 遍历每一个物品
        for j in range(1, capacity+1): # 遍历包的容量
            if weight[i-1] > j: # 说明装不下
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight[i-1]] + value[i-1])

    return dp[-1][-1]

number = 4
capacity = 8
weight = [2,3,4,5]
value = [3,4,5,6]

print('0-1背包问题', bag(number, capacity, weight, value))


'''完全背包问题'''
# 每个物品能拿无数次
def CompleteBag(number, capacity, weight, value):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(number + 1)]

    for i in range(1, number + 1):  # 遍历每一个物品
        for j in range(1, capacity + 1):  # 遍历包的容量
            if j - weight[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i-1]] + value[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

number = 4
capacity = 8
weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]

print('完全背包问题', CompleteBag(number, capacity, weight, value))


'''多重背包问题'''
# 规定每个物品的个数
def Solution(n, capacity, weight, value, number):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):  # 遍历每一个物品
        for j in range(1, capacity + 1):  # 遍历包的容量
            if weight[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                count = min(number[i-1], j // weight[i-1])
                for k in range(1, count+1):
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - k*weight[i - 1]] + k*value[i - 1])
    return dp[-1][-1]

n = 4
capacity = 8
weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]
number = [1, 2, 3, 4]
print('多重背包问题', Solution(n, capacity, weight, value, number))



