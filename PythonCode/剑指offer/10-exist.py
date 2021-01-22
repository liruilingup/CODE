
'''剑指 Offer 12. 矩阵中的路径'''
# 使用dfs+回溯解法
# 先确定边界值，然后需要标记搜索过的，最后再回溯
def exist(board, word):
    def dfs(i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False # 边界和不相等的时候结束
        if k == len(word) - 1: return True # 找到了结束
        board[i][j] = '' # 标记搜索过的
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = word[k] # 通过回溯再修改值
        return res

    for i in range(len(board)):
        for j in range(len(board[0])): # 矩阵中的每一个点都作为开始点进行搜索
            if dfs(i, j, 0): return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))




