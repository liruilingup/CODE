
'''二叉树节点'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# 构建一颗树
left = TreeNode(2)
right = TreeNode(3, TreeNode(6), TreeNode(7))
root = TreeNode(1, left, right)

'''543. 二叉树的直径'''
'''一个二叉树，两个节点，连接两个节点的最长路径长度'''
# 一棵树的直径 = max(左子树的直径, 右子树的直径, 左子树的深度 + 右子树的深度)
def DiameterOfBinaryTree(root):
    def dfs(root):
        if not root:
            return 0, 0
        ldiameter, ldepth = dfs(root.left)
        rdiameter, rdepth = dfs(root.right)
        return max(ldiameter, rdiameter, ldepth + rdepth), max(ldepth, rdepth) + 1
    return dfs(root)[0]

print('方法1', DiameterOfBinaryTree(root))

'''解法2'''
# 对于每一个当前节点，选择左、右节点中最大的长度，然后加上1（当前路径），则是当前的最长路径深度。
# 全局变量dis为直径，每次取左、右节点深度的和。

class Diameter:
    def __init__(self):
        self.dis = 0

    def DiameterOfBinaryTree(self, root):
        if not root: return 0

        def dfs(root):
            if not root:return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.dis = max(l+r, self.dis)
            return max(l,r) + 1

        dfs(root)
        return self.dis

print('方法2', Diameter().DiameterOfBinaryTree(root))
