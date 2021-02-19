
'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
'''
def singleNumbers(nums):
    x, y, n, m = 0, 0, 0, 1
    for num in nums:  # 1. 遍历异或
        n ^= num
    while n & m == 0:  # 2. 循环左移，计算 m
        m <<= 1
    for num in nums:  # 3. 遍历 nums 分组
        if num & m:
            x ^= num  # 4. 当 num & m != 0
        else:
            y ^= num  # 4. 当 num & m == 0
    return x, y  # 5. 返回出现一次的数字
print(singleNumbers([1,2,1,2,4,5]))


'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
'''
def singleNumber2(nums):
    ones, twos = 0, 0
    for num in nums:
        ones = ones ^ num & ~twos
        twos = twos ^ num & ~ones
    return ones
nums = [3,4,3,3]
print(singleNumber2(nums))