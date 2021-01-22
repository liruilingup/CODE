
'''剑指 Offer 10- I. 斐波那契数列'''
# 动态规划
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007
print('')


def fib2(n):
    if n < 0: return n
    if n == 0: return 0
    if n == 1: return 1
    n1 = 0
    n2 = 1
    for _ in range(2, n + 1):
        n1, n2 = n2, n1 + n2
    return n2 % 1000000007