'''
一个射击员打靶，请问连开10枪打80环的可能性有多少种
解题方法：动态规划，背包问题的变形
同零钱兑换
'''

huan = [i for i in range(1,11)]
# huan = [1,2,5]
value = 80
def ability(huan, value):
    dp = [[0 for _ in range(value+1)] for _ in range(len(huan) + 1)]
    dp[0][0] = 1
    for i in range(1, len(huan)+1):
        dp[i][0] = 1

    for i in range(1, len(huan) + 1):
        for j in range(1, value+1):
            if huan[i-1] > j: # 不选择
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-huan[i-1]]
    print(dp[-1][-1])

ability(huan, value)

