
'''正序遍历数组'''
def TrueBinArrayTraverse(nums):
    m = len(nums)
    n = len(nums[0])
    print('正序遍历行和列', m, n)
    for i in range(m):
        for j in range(n):
            print(nums[i][j], end=' ')
        print()

'''倒序遍历数组'''
def ReverseBinArrayTraverse(nums):
    m = len(nums)
    n = len(nums[0])
    print('倒序遍历行和列', m, n)
    for i in range(m-1, -1 ,-1):
        for j in range(n-1, -1, -1):
            print(nums[i][j], end = ' ')
        print()

'''-----两种斜着遍历数组-----'''
def SlantBinArrayTraverse1(nums):
    m = len(nums)
    n = len(nums[0])
    print('从左至右斜着遍历行和列', m, n)
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = l + i -1
            print(nums[i][j], end=' ')
        print()

def SlantBinArrayTraverse2(nums):
    m = len(nums)
    n = len(nums[0])
    print('从下向上，从左到右斜着遍历', m, n)
    for i in range(n-2, -1, -1): # 从下向上
        for j in range(i+1, n): # 从左到右
            print(nums[i][j], end=' ')
        print()

# 6行5列的数组
m = 5
n = 5
nums = [[i+j for i in range(n)] for j in range(m)]
TrueBinArrayTraverse(nums)
ReverseBinArrayTraverse(nums)
SlantBinArrayTraverse1(nums)
SlantBinArrayTraverse2(nums)
