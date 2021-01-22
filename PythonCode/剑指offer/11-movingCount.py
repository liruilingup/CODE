
'''剑指 Offer 13. 机器人的运动范围'''

# 使用广度优先，就是向右、向下
# 使用queue和s
class movingCount:
    def __init__(self):
        return

    def digitsum(self, n):
        res = 0
        while n:
            res += n%10
            n //= 10
        return res

    def BFS(self, m,n,k):
        queue = [(0, 0)]
        s = set()
        while queue:
            x, y = queue.pop(0)
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and self.digitsum(x) + self.digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]: # 列表就是向右、向下
                    queue.append((nx, ny))
        return len(s)

print('广度优先解法', movingCount().BFS(2,3,1))


# 深度优先解法
def digitsum(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res
def movingCount(m, n, k):
    def dfs(i, j):
        if i >= m or j >= n or k < (digitsum(i) + digitsum(j)) or (i, j) in visited: return 0
        visited.add((i, j))
        return 1 + dfs(i + 1, j) + dfs(i, j + 1)

    visited = set()
    return dfs(0, 0)
print('深度优先解法', movingCount(2, 3, 1))

