'''剑指 Offer 33. 二叉搜索树的后序遍历序列'''
# 二叉搜索树的特点是左子树的值<根节点<右子树的值。而后续遍历的顺序是：
# 左子节点→右子节点→根节点
# 根据索引使用递归解决

class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(1), treenode(3))
right = treenode(6)
root = treenode(5, left, right)

# 后序遍历先存储结果
postorder = []
def PostorderTraverse(root):
    if not root:return
    PostorderTraverse(root.left)
    PostorderTraverse(root.right)
    postorder.append(root.val)
PostorderTraverse(root)
print(postorder)

def VerifyPostorder(postorder):
    # 先找到第一个比根节点大的数字，找到左子树和右子树
    def recur(i, j):
        if i >= j: return True # 当i>=j，说明是叶子节点

        p = i
        while postorder[p] < postorder[j]:
            p += 1
        m = p # 找到右子树的索引

        while postorder[p] > postorder[j]: # 判断是否为二叉搜索树, 左子树区间都应该<根节点(上一个while实现)，右子树都应该>根节点
            p += 1

        return p == j and recur(i, m - 1) and recur(m, j - 1)

    return recur(0, len(postorder) - 1)
print(VerifyPostorder(postorder))


