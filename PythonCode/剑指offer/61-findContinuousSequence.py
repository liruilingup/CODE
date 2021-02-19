def findContinuousSequence(target):
    i = 1  # 滑动窗口的左边界
    j = 1  # 滑动窗口的右边界
    sum = 0  # 滑动窗口中数字的和
    res = []

    while i <= target // 2:
        if sum < target:
            # 右边界向右移动
            sum += j
            j += 1
        elif sum > target:
            # 左边界向右移动
            sum -= i
            i += 1
        else:
            # 记录结果
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            sum -= i
            i += 1
    return res



# 使用双指针，自己写的
def findContinuousSequence1(target):
    i=j=1
    sum = 0
    res = []
    while i < target:
        if sum <target:
            sum += j
            j+=1
        elif sum > target:
            sum = 0
            i += 1
            j = i
        else:
            res.append(list(range(i,j)))
            sum = 0
            i += 1
            j=i

    return res
print(findContinuousSequence1(9))