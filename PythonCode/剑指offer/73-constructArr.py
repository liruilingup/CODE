''''
构建一个二维表格, 行列相同的时候为1
总的乘积就是上三角和下三角的的乘积
上三角和下三角的乘积跟上下有关系，不用每次遍历都从头计算
'''
'''
  0 1 2 3 4
0 1 2 3 4 5
1 1 1 3 4 5
2 1 2 1 4 5
3 1 2 3 1 5
4 1 2 3 4 1
'''

def constructArr(a):
    b, tmp = [1] * len(a), 1
    for i in range(1, len(a)):
        b[i] = b[i - 1] * a[i - 1]  # 下三角
    for i in range(len(a) - 2, -1, -1):
        tmp *= a[i + 1]  # 上三角
        b[i] *= tmp  # 下三角 * 上三角
    return b

