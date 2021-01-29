'''下一个更大元素 '''
# 方法二
# 倒序维护一个递减的单调栈
# res[i]=栈顶元素 or -1
# 进栈


nums2 = [1,3,4,2]
# 结果是[3, 4, -1, -1]

def nextGreaterElement1(nums2):
    res = [0] * len(nums2)
    stack = []
    for i in range(len(nums2)-1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums2[i])
    return res
print(nextGreaterElement1(nums2))


# 索引进栈的方法
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
def nextGreaterElements2(nums) :
    nums = nums
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        stack.append(i)

    return res
print(nextGreaterElements2(temperatures))

