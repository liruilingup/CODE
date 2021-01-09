'''剑指 Offer 29. 顺时针打印矩阵'''

def spiralOrder(matrix):
    row = len(matrix)
    column = len(matrix[0])
    res = []
    top, bottom, left, right = 0, row-1, 0, column-1
    while top < bottom and left < right:
        for column in range(left, right+1): # 行不变
            res.append(matrix[top][column])

        for row in range(top+1, bottom): # 列不变
            res.append(matrix[row][right])

        for column in range(right, left-1, -1): #行不变
            res.append(matrix[bottom][column])

        for row in range(bottom-1, top, -1): # 列不变
            res.append(matrix[row][left])
        top, bottom, left, right = top+1, bottom-1, left+1, right-1
    if top==bottom and left==right:
        res.append(matrix[left][left])
    elif top==bottom:
        for column in range(left, right+1): # 行不变
            res.append(matrix[top][column])
    elif left==right:
        for row in range(top, bottom+1): # 列不变
            res.append(matrix[row][left])
    return res

matrix = [[7],[9],[6]]
print('结果', spiralOrder(matrix))

