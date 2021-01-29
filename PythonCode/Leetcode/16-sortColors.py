# 方法一、单指针
# 在第一次遍历中，我们将数组中所有的 0 交换到数组的头部。
# 在第二次遍历中，我们将数组中所有的 1 交换到头部的 0 之后
# 此时2 都出现在数组的尾部

def sortColors(nums):
    n = len(nums)
    Pre = 0
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[Pre] = nums[Pre], nums[i]
            Pre += 1
    for i in range(Pre, n):
        if nums[i] == 1:
            nums[i], nums[Pre] = nums[Pre], nums[i]
            Pre += 1
    print(nums)
sortColors([2,0,1])


# 方法二、双指针
# 指针p0来交换 0，p2来交换 2
# p2是从右向左移动的，从左向右遍历整个数组时，如果遍历到的位置超过了p2，那么就可以直接停止遍历了。
def sortColors1(nums):
    n = len(nums)
    p0, p2 = 0, n-1
    i = 0
    while i <= p2:
        while i <= p2 and nums[i]==2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
        i += 1
    print(nums)

sortColors1([2,0,1])

def sortColors3(nums):
    l,r,i =0,0,0

    while i < len(nums) and r < len(nums) and l < len(nums):
        if nums[i]==2:
            i += 1
            continue
        elif nums[i] ==1 :
            nums[i], nums[r] = nums[r], nums[i]
            r += 1
            i += 1
        elif nums[i] == 0 and l == i:
            i += 1
            l += 1
            r += 1
        else:
            nums[i], nums[l] = nums[l], nums[i]
            if l==r:
                r+=1
            l += 1

    print(nums)

sortColors3([0, 0, 1])


