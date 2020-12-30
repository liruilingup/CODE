
class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left1 = treenode(2)
right1 = treenode(3, treenode(6), treenode(7))
root1 = treenode(1, left1, right1)


left2 = treenode(2)
right2 = treenode(3, treenode(6), treenode(7))
root2 = treenode(1, left2, right2)

'''判断两棵二叉树是否完全相同'''
def IsSameTree(root1, root2):
    if not root1 and not root2: return True
    if not root1 or not root2: return False
    if root1.item != root1.item: return False

    # root1和root2都比完了
    return IsSameTree(root1.left, root2.left) and IsSameTree(root1.right, root2.right)
print(IsSameTree(root1, root2))
