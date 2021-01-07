
'''54. 螺旋矩阵'''

# (top, left)、(top, right)
# (bottom, left)、(bottom, right)
# 假设当前层的左上角位于(top, left)，右下角位于(bottom, right)
# 从左到右遍历上侧元素: (top, left)->(top, right)
# 从上到下遍历右侧元素:(top+1, right)->(bottom, right)
# 从右到左遍历下侧元素:(bottom, right-1)->(bottom, left+1) 前提：left < right 和 top < bottom
# 从下到上遍历左侧元素:(bottom, left)->(top+1, left)

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, columns = len(matrix), len(matrix[0])
    res = []
    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left <= right and top <= bottom:
        for column in range(left, right+1): # 上边
            res.append(matrix[top][column])

        for row in range(top+1, bottom+1): # 右边
            res.append(matrix[row][right])

        if left < right and top < bottom:
            for column in range(right - 1, left, -1): # 下边
                res.append(matrix[bottom][column])
            for row in range(bottom, top, -1): # 左边
                res.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

    return res


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print('方法一、结果：', spiralOrder(matrix))

'''方法二'''
def spiralOrder2(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, columns = len(matrix), len(matrix[0])
    res = []
    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left < right and top < bottom:
        for column in range(left, right+1): # 上边
            res.append(matrix[top][column])

        for row in range(top+1, bottom): # 右边
            res.append(matrix[row][right])

        for column in range(right, left-1, -1): # 下边
            res.append(matrix[bottom][column])

        for row in range(bottom-1, left, -1): # 左边
            res.append(matrix[row][left])
        left, right, top, bottom = left+1, right-1, top+1, bottom-1

    if left == right and top == bottom: # 行数和列数相同
        res.append(matrix[left][left])
    elif left == right:
        for row in range(top, bottom+1): # 从上到下
            res.append(matrix[row][left])
    elif top == bottom:
        for column in range(left, right+1): # 从左到右
            res.append(matrix[top][column])

    return res


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
matrix = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
print('方法二结果：', spiralOrder2(matrix))
