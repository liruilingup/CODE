'''https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/'''
def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <=0:
            nums[i]= n+1
    for i in range(n):
        num = abs(nums[i]) # 有可能交换的时候被交换成了负数
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    for i in range(n):
        if nums[i] > 0:
            return i+1
    return n+1

nums = [3,4,-1,1]
nums = [3, 4, -1, 1, 9, -5]

print(firstMissingPositive(nums))


