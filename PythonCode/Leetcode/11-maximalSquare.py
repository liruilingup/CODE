
'''221. 最大正方形'''

# 使用动态规划
def maximalSquare(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0: return 0
    maxside = 0
    rows, columns = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxside = max(maxside, dp[i][j])

    return maxside * maxside

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(maximalSquare(matrix))

# 使用暴力方法

def maximalSquare1(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    maxSide = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':
                maxSide = max(maxSide, 1)
                currentMaxSide = min(rows - i, columns - j)
                for k in range(1, currentMaxSide):
                    flag = True
                    if matrix[i + k][j + k] == '0':
                        break
                    for m in range(k):
                        if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                            flag = False
                            break
                    if flag:
                        maxSide = max(maxSide, k+1)
                    else:
                        break
    return maxSide * maxSide

print(maximalSquare1(matrix))


