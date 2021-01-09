def lastRemaining(n, m):
    f = 0
    for i in range(2, n + 1):
        f = (m + f) % i
    return f