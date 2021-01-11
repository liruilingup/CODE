import collections
def maxSlidingWindow( nums, k):
    if not nums or k == 0: return []
    deque = collections.deque()
    for i in range(k):  # 未形成窗口
        while deque and deque[-1] < nums[i]:
            deque.pop()
        deque.append(nums[i])
    res = [deque[0]]
    # 使用双端队列，保证queue[0]是最大的
    for i in range(k, len(nums)):  # 形成窗口后
        if deque[0] == nums[i - k]: # 注意窗口的开始
            deque.popleft()
        while deque and deque[-1] < nums[i]: # 删除所有的比nums[i]小的，保证queue[0]是最大的
            deque.pop()
        deque.append(nums[i])
        res.append(deque[0])
    return res