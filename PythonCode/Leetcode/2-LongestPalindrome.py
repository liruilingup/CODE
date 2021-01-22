
'''5. 最长回文子串'''
# 子串都是连续的，自序列不是
def longestPalindrome(s):
    n = len(s)
    for i in range(n, -1, -1):
        for j in range(n-i+1):
            sub = s[j:i+j]  # 注意i，j的变化范围
            if sub == sub[::-1]:
                return sub
    return s[0]
print(longestPalindrome("babad"))

# 动态规划解法
def longestPalindrome(s):
    # dp[i][j] 记录 s[i:j] 是不是一个回文串,满足以下2个条件就是～
    # 1. s[i] = s[j]
    # 2. s[i+1:j-1] 是一个回文串,这里用一个条件判断 i+1 >= j-1, 初始化 长度为1 和 长度为0 的串为回文串

    length = len(s)
    dp = [[1] * length for _ in range(length)]
    left, right = 0, 0 #长度为1时
    for i in range(1, length):
         for j in range(length-i):
            if s[j] == s[j+i] and dp[j+1][j+i-1]:
                dp[j][j+i] = 1
                left, right = j, j+i
            else:
                dp[j][j+i] = 0
    return s[left: right+1]
