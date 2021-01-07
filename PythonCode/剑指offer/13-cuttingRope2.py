'''剑指 Offer 14- II. 剪绳子 II'''
def cuttingRope2(n):
    if n < 4:return n-1
    elif n==4:return n
    res = 1
    while n > 4:
        res *= 3
        res %= 1000000007
        n -= 3
    return res * n % 1000000007
print(cuttingRope2(1000))

