'''剑指 Offer 59 - I. 滑动窗口的最大值'''
'''使用单调队列的方式可以降低复杂度'''

def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums)-k+1):
        res.append(max(nums[i:i+k]))
    return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print('结果', maxSlidingWindow(nums, k))
