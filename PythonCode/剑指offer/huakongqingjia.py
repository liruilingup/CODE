'''
1、有序的数组
2、target插入数组
3、返回有序数组
'''

def array(nums, target):
    start = 0
    end = len(nums)
    i = 0
    while start < end:
        mid = (start + end) // 2
        i += 1
        print('test', i)
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            nums.insert(mid, target)
            return nums
    mid = (start + end) // 2
    nums.insert(mid, target)
    return nums

nums = [1,2,3,4,6,7]
target = 8
# print(array(nums, target))

'''
1、m*n矩阵
2、左上角出发点(0,0)->(m-1, n-1)
3、返回路径
'''
def sumPath(m, n):
    # 动态规划方法
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:continue
            elif i == 0: dp[i][j] = dp[i][j-1]
            elif j == 0: dp[i][j] = dp[i-1][j]
            else: dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp)

    # 递归方法
    def dfs(i, j):
        # if i < 0 or j <0: return
        if i == 0 and j == 0:
            return 1
        if i == 0:
            return dfs(i, j-1)
        if j == 0:
            return dfs(i-1, j)
        return dfs(i-1, j) + dfs(i, j-1)
    print(dfs(m-1, n-1))
    return

m = 3
n = 4
sumPath(m, n)

'''二分查找
返回第一次出现的索引'''

def BinarySearch(target, nums):
    low = 0
    high = len(nums)-1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            high = mid
            low = mid-1

    return low
nums = [2, 2, 7, 8, 9, 9,9, 10, 13, 19, 19]
print(BinarySearch(19, nums))
