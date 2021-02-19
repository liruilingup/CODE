def myPow(x, n):
    if n == 0: return 1
    if n < 0: return (1 / x) * myPow(1 / x, -n - 1)
    return myPow(x * x, n >> 1) if n % 2 == 0 else x * myPow(x * x, (n - 1) >> 1)


x = 2.00000
n = 10
print(myPow(x, n))