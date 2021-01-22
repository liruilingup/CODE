'''200. 岛屿数量'''

# 所有1相连接的都是一个岛屿
# 深度优先遍历不是1的停止，遍历过1的设置成0

def numIslands(grid):
    m = len(grid)
    n = len(grid[0])
    def dfs(grid, i,j):
        if not 0<=i<m or not 0<=j<n or grid[i][j] != '':
            return
        grid[i][j] = '0'
        dfs(grid, i, j-1)
        dfs(grid, i, j+1)
        dfs(grid, i-1, j)
        dfs(grid, i+1, j)
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count
