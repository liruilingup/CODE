# 变化规律
def findNthDigit(n):
    digit, start, count = 1, 1, 9
    while n > count:  # 1.
        n -= count
        start *= 10
        digit += 1
        count = 9 * start * digit
    num = start + (n - 1) // digit  # 2.
    return int(str(num)[(n - 1) % digit])  # 3.