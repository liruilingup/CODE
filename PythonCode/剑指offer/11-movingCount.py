
'''剑指 Offer 13. 机器人的运动范围'''

def movingCount(m, n, k):
    queue, visited, = [(0, 0, 0, 0)], set()
    while queue:
        i, j, si, sj = queue.pop(0)
        if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
        visited.add((i, j))
        queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
        queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
    return len(visited)


m = 3
n = 1
k = 0
print(movingCount(m, n, k))