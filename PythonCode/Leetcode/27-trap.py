# 42. 接雨水 困难
'''使用双指针'''

def trap(height):
    if len(height) <= 2:
        return 0
    res = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[0], height[-1]
    while left <= right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max < right_max:
            res += left_max - height[left]
            left += 1
        else:
            res += right_max - height[right]
            right -= 1
    return res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))

