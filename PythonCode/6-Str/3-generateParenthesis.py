def generateParenthesis(n):
    def dfs(tmp, left, right):
        if left == 0 and right == 0:
            res.append(tmp)
        if left > 0:
            dfs(tmp + '(', left - 1, right)
        if left < right:
            dfs(tmp + ')', left, right - 1)

    res = []
    dfs('', n, n)
    return res
print(generateParenthesis(3))

