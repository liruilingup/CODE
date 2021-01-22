# 刷题的第200道
'''287. 寻找重复数'''
# 方法一、使用集合
def findDuplicate(nums):
    if not nums or len(nums) == 1: return nums
    s = set()
    for i in nums:
        if i in s:
            return i
        else:
            s.add(i)

# 方法二、二分查找统计个数
def findDuplicate1(nums):
    n = len(nums)
    low = 1
    high = n
    while low < high:
        mid = (low+high)//2
        count = 0
        for i in range(len(nums)):
            if nums[i] <= mid:
                count += 1
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low
print(findDuplicate1([2,2,2,2,2]))


# 方法三、使用快慢指针
def findDuplicate2(nums):
    slow, fast = 0, 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if slow == fast:
            break
    new = 0
    while True:
        slow = nums[slow]
        new = nums[new]
        if new == slow:
            break
    return slow

print(findDuplicate2([2,2,2,2,2]))