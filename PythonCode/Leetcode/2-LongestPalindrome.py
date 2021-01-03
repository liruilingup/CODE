
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


