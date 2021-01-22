
'''剑指 Offer 10- II. 青蛙跳台阶问题'''
# 每次跳1个或者两个
# 总结归纳得出就是斐波那契
# 不同的就是初始值a是1


def numWays(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007
print(numWays(10))


def numWays2(n):
    if n == 0 or n == 1: return 1
    a = 1
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b % 1000000007



