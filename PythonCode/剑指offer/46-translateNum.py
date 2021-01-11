# 使用动态规划
def translateNum(num):
    s = str(num)
    a = b = 1
    for i in range(len(s) - 2, -1, -1):
        print(s[i:i + 2])
        a, b = (a + b if "10" <= s[i:i + 2] <= "25" else a), a
    return a
print('结果', translateNum(12258))


def translateNum2(num):
    s = str(num)
    dp = [1] * (len(s)+1)
    for i in range(2, len(s)+1):
        if "10" <= s[i-2:i]<= "25": # 可翻译
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
    return dp[-1]

print('', translateNum2(12258))