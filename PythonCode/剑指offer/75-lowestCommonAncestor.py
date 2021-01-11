'''二叉搜索树的最近公共祖先'''


class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
tree4 = treenode(4, treenode(3), treenode(5))
tree2 = treenode(2, treenode(0), tree4)
tree8 = treenode(8, treenode(7), treenode(9))
tree6 = treenode(6, tree2, tree8)

'''
二叉搜索树：左节点<根节点<右节点
所以：如果p<根节点<q，那么根节点一定是最近的公共祖先，递归判断左子树和右子树
1、p < 根节点 and q < 根节点，判断左子树
2、p > 根节点 and q > 根节点，判断右子树
3、如果左右子树不符合，最近公共祖先就是根节点
'''

def lowestCommonAncestor(root, p, q):
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    return root

print('结果', lowestCommonAncestor(tree6, tree2, tree8).val)



