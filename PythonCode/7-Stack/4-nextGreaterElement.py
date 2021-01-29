'''496. 下一个更大元素 I'''
# 维护一个递减的单调栈
# 当前值大于栈顶元素的话，栈顶元素进入集合的key，value是当前值
# 当前值进栈

nums1 = [4,1,2]
nums2 = [1,3,4,2]

def nextGreaterElement(nums1, nums2):
    hash = {}
    stack = []
    for i in nums2:
        while stack and i > stack[-1]:
            hash[stack.pop()] = i
        stack.append(i)
    return [hash.get(i, -1) for i in nums1]
print(nextGreaterElement(nums1, nums2))



