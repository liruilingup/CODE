'''给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种'''

# 如果整数 1 - n 中的 k 作为根节点值，则 1 - k-1 会去构建左子树，k+1 - n 会去构建右子树。
# 左子树出来的形态有 a 种，右子树出来的形态有 b 种，则整个树的形态有a * b种。
# 以 k 为根节点的 BST 种类数 = 左子树 BST 种类数 * 右子树 BST 种类数
# 问题变成：不同的 k 之下，等号右边的乘积，进行累加。

def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[-1]
print(numTrees(3))


