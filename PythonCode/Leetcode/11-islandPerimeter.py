
def islandPerimeter(grid):
    m = len(grid)
    n = len(grid[0])
    def dfs(grid,i,j):
        if not 0<=i<m or not 0<=j<n or grid[i][j]==0:return 1
        if grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        return dfs(grid,i-1,j)+dfs(grid,i+1,j)+dfs(grid,i,j-1)+dfs(grid,i,j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return dfs(grid, i, j)
    return 0
