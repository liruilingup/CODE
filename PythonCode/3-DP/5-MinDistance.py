
'''72. 编辑距离'''
# 使用i、j指向最后一个字母，进行4种操作
'''使用暴力递归的方法'''
def MinDistance(word1, word2):

    def dp(i, j):
        # base case
        if i == -1: return j + 1
        if j == -1: return i+1

        # 选择
        if word1[i] == word2[j]:
            return dp(i-1, j-1) # 什么都不做
        else:
            return min(
                dp(i, j-1) + 1, # 插入
                dp(i-1, j) + 1, # 删除
                dp(i-1, j-1) + 1  # 替换
            )
    return dp(len(word1)-1, len(word2)-1)

print('使用暴力递归的方法', MinDistance('intention', 'execution'))

'''使用备忘录的方法'''
def MemoMinDistance(word1, word2):
    memo = dict()
    def dp(i,j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == -1: return j + 1
        if j == -1: return i + 1
        if word1[i] == word2[j]:
            memo[(i, j)] = dp(i-1, j-1)
        else:
            memo[(i, j)] = min(
                dp(i, j - 1) + 1,  # 插入
                dp(i - 1, j) + 1,  # 删除
                dp(i - 1, j - 1) + 1  # 替换
            )
        return memo[(i, j)]
    return dp(len(word1)-1, len(word2)-1)
print('使用备忘录的方法', MemoMinDistance('intention', 'execution'))

'''使用动态规划的方法'''
def DpMinDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                dp[i-1][j] + 1,  # 插入
                dp[i][j-1] + 1,  # 删除
                dp[i-1][j-1] + 1  # 替换
            )
    return dp[m][n]

print('使用动态规划的方法',DpMinDistance('rad', 'apple') )