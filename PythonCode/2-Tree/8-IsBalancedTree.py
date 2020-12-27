class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
leaf = treenode(10, treenode(6), treenode(7))
left = treenode(2)
right = treenode(3, leaf, treenode(8))
root = treenode(1, left, right)


'''是否是平衡二叉树'''
def IsBalancedTree(root):
    if not root:
        return True # 空树默认是平衡的
    left = depth(root.left)
    right = depth(root.right)
    if abs(left - right) > 1:
        return False

    return IsBalancedTree(root.left) and IsBalancedTree(root.right) # 保证左右子树都是平衡二叉树

def depth(root):
    if not root:
        return 0
    return 1 + max(depth(root.right), depth(root.left))

print(IsBalancedTree(root))
