'''剑指 Offer 11. 旋转数组的最小数字'''
# 使用二分法
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
print([3,4,5,1,2])
