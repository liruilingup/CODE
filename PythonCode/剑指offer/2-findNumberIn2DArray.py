# 暴力时间复杂度是 o(m*n)
# 线性查找时间复杂度是 o(m+n)
# 若 flag > target ，则 target 一定在 flag 所在 行的上方，即 flag 所在行可被消去。
# 若 flag < target ，则 target 一定在 flag 所在 列的右方，即 flag 所在列可被消去。

def findNumberIn2DArray(matrix, target):
    i = len(matrix) - 1
    j = 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > target: i -= 1
        elif matrix[i][j] < target:
            j += 1
        else: return True
    return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 5
print('结果：', findNumberIn2DArray(matrix, target))
