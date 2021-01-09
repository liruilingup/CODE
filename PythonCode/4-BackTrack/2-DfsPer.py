# 数字的全排列
n = 2
res = []
def dfs(x):
    if x == n:
        res.append(nums[:])
        return
    for i in range(10):
        nums[x] = i
        dfs(x+1)

nums = ['0'] * n
res = []
dfs(0)
print(res)
