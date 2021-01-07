
'''64. 最小路径和'''
'''给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小'''
# 说明：每次只能向下或者向右移动一步。

'''解题：设dp为大小 m*n 矩阵，其中 dp[i][j]的值代表直到走到(i,j)的最小路径和'''
'''(i, j)只能来自，(i-1,j)、(i, j-1)中最小的，再加上当前grid(i, j)'''
# 1、都不是边界
# 2、左边边界
# 3、上边边界
# 4、左上都是边界


def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    # 不用建立DP，直接使用grid，不会被
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:continue
            elif i==0: grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j==0: grid[i][j] = grid[i-1][j] + grid[i][j]
            else: grid[i][j] = min(grid[i][j - 1], grid[i-1][j]) + grid[i][j]
    return grid[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

print('最小路径和', minPathSum(grid))

