
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

