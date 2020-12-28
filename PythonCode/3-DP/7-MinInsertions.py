
'''1312. 让字符串成为回文串的最少插入次数'''
def MinInsertions(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]

    # base case: i==j时，dp[i][j]=0，单个字符串本身就是回文串

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1
    return dp[0][n-1]

print('字符串成为回文串的最少插入次数', MinInsertions('mbadm'))

