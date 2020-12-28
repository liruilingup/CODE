
'''0-1背包问题'''
# 只能使用一次，求出来这个包最多能装的价值
def bag(number, capacity, w, v):
    dp = [[0 for _ in range(capacity+1)] for _ in range(number+1)]

    for i in range(1, number+1): # 遍历每一个物品
        for j in range(1, capacity+1): # 遍历包的容量
            if j < w[i]:# 说明装不下
                dp[i][j] = dp[i-1][j] # 等于上一个物品
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i]) # dp[i-1][j-w[i]]是前i-1个物品的最优解
    return dp[-1][-1]

number = 4
capacity = 8
w=[0,2,3,4,5] # 如果不从0开始，循环的时候，i和j就需要
v=[0,3,4,5,6]
res = bag(number, capacity, w, v)
print('', res)


'''完全背包问题'''
# 每个物品能拿无数次

def CompleteBag():
    return


'''多重背包问题'''
# 规定每个物品的个数



