# 剑指 Offer 15. 二进制中1的个数

def hammingWeight(n):
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res
print('二进制中1的个数', hammingWeight(1))

