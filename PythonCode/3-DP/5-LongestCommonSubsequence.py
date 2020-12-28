# 上午看动态规划和字符串
# 晚上看机器学习


'''最长公共子序列'''
# 使用二维动态规划来解决，行和列分别是两个字符串
# step1、dp[i][j]表示s1[0:i]和s2[0:j]中LCS的个数
# step2、base case dp[0][]=0, dp[][0]=0，因为空串和一个串的LCS是0
# step3、s1[i]和s2[j]只有相等和不相等，如果相等就是共同字符串dp+1；如果不相等取，max(dp[i-1][j], dp[i][j-1])


'''使用暴力递归的方法'''
def LongestCommonSubsequence(str1, str2):
    def dp(i, j):
        if i == -1 or j == -1:
            return 0
        if str1[i] == str2[j]:
            return dp(i-1, j-1) + 1
        else:
            return max(dp(i, j-1), dp(i-1, j))

    return dp(len(str1)-1, len(str2)-1)

print('使用暴力递归的方法', LongestCommonSubsequence('abcde', 'aceb'))

'''使用动态规划的解法'''
def DpLongestCommonSubsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]
print('使用动态规划的解法', DpLongestCommonSubsequence('abcde', 'aceb'))
