
'''剑指 Offer 16. 数值的整数次方'''

# 使用递归
def myPow(x, n):
    if n==0:return 1
    if n < 0:return (1/x) * myPow(1/x, -n-1)
    return myPow(x*x, n>>1) if n%2==0 else x*myPow(x*x,(n-1)>>1)

print('1、使用递归的方法：',myPow(2.00000, 10) )

'''使用快速幂'''
def myPow1(x, n):
    if x == 0: return 0
    res = 1
    if n < 0: x, n = 1 / x, -n
    while n:
        if n & 1: res *= x
        x *= x
        n >>= 1
    return res

print('2、使用快速幂：',myPow1(2.00000, 10) )


