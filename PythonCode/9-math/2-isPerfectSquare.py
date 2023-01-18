import math
def isSqr(n):
    a = int(math.sqrt(n))
    return a * a == n
print('方法一', isSqr(4))


def isPerfectSquare(num):
    start = 1
    end = num
    while start <= end:
        mid = start + (end - start) // 2
        sqr = mid ** 2
        if sqr < num:
            start = mid + 1
        elif sqr > num:
            end = mid - 1
        else:
            return True
    return False
print('方法二', isPerfectSquare(5))

def isPerfectSquare1(num):
    i = 1
    while i * i < num:
        i += 1
    return i * i == num
print('方法三', isPerfectSquare1(4))
