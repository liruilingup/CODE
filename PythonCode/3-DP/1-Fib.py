'''使用递归的方法'''
def Fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return Fib(n-1)+Fib(n-2)








