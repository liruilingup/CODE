
'''剑指 Offer 10- I. 斐波那契数列'''
# 动态规划
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007
print('')