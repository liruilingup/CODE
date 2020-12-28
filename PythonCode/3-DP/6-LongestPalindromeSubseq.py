

'''最长回文子序列'''
# dp[i][j]表示s[i-j]的最长回文子序列

def LongestPalindromeSubseq(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]
print('最长回文子序列', LongestPalindromeSubseq('aecda'))



