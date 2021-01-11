class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
tree2 = treenode(2, treenode(7), treenode(4))
tree5 = treenode(5, treenode(6), tree2)
tree1 = treenode(1, treenode(0), treenode(8))
tree3 = treenode(3, tree5, tree1)

'''
设节点root为节点 p,q 的某公共祖先，其左子节点 root.lef 和右子节点 root.right都不是 p,q 的公共祖先 
最近公共祖先root的可能情况：
1、p和q在root的子树中，且分列root的异侧
2、p=root，且q在 root 的左或右子树中
3、q=root，且p在 root 的左或右子树中
使用后序遍历：如果左子树、右子树都不是最近公共祖先，那么就是根节点
1、递归结束条件：if not root or root=p or root=q:return root
2、判断左子树
3、判断右子树
4、如果左右子树都不是，返回空
5、如果左子树不是，返回右子树
6、如果右子树不是，返回左子树
7、上诉情况不符合，返回根节点
'''
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left and not right: return  # 1. 可以不要
    if not left: return right  # 3.
    if not right: return left  # 4.
    return root  # 2. if left and right:

print('验证结果', lowestCommonAncestor(tree3, tree1, tree5).val)


