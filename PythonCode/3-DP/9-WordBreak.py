'''139. 单词拆分'''
def WordBreak(s, wordDict):
    n = len(s)
    dp = (n+1) * [False]
    dp[0] = True
    for i in range(n):
        for j in range(i+1, n+1):
            if (dp[i] and s[i:j] in wordDict):
                dp[j] = True
    return dp[-1]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print('', WordBreak(s, wordDict))



