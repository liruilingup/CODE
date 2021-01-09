
# 方法一、使用迭代
def printNumbers(n):
    res = []
    for i in range(1, 10 ** n):
        res.append(i)
    return res

print(printNumbers(3))


# 方法二、使用递归全排列
class PNumer:
    def __init__(self):
        return

    def printNumbers1(self, n):

        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1 # 说明最后一位数字变成9了
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1 # 回溯之后nine的值减去1
        self.nine = 0
        self.start = n - 1
        num, res = ['0'] * n, []

        dfs(0)
        return res
print(PNumer().printNumbers1(3))



