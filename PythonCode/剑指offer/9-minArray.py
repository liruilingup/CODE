'''剑指 Offer 11. 旋转数组的最小数字'''
# 使用二分法
# 左边数组
# 右边数组
# 有相等的时候j -= 1
def minArray(numbers):
    i, j = 0, len(numbers) - 1
    while i < j:
        m = (i + j) // 2
        if numbers[m] > numbers[j]:
            i = m + 1
        elif numbers[m] < numbers[j]:
            j = m
        else:
            j -= 1
    return numbers[i]
numbers = [3,4,5,1,2]
print(minArray(numbers))


# 旋转数组中的查找
def minArray(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        m = (i + j) // 2
        if numbers[m] == target: return m
        if numbers[i] == target: return i
        if numbers[j] == target: return j

        if numbers[i] < numbers[m]: # 左边有序
            if target > numbers[m]:
                i = m + 1
            else:
                j = m - 1
        else: # 右边有序
            if target > numbers[m]:
                i = m + 1
            else:
                j = m - 1
    return 'not in '
target = 0
print(minArray(numbers, target))
