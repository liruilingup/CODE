'''455. 分发饼干'''
# 输入: g = [1,2,3], s = [1,1]
# 输出: 1
# 解释:
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。

# 输入: g = [1,2], s = [1,2,3]
# 输出: 2
# 解释:
# 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
# 你拥有的饼干数量和尺寸都足以让所有孩子满足。
# 所以你应该输出2.


def findContentChildren(g, s):
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            child += 1
        cookie += 1
    return child
g = [1,2]
s = [1,2,3]
print('分发饼干结果:', findContentChildren(g, s))
