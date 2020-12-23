class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)

# 树的前序遍历
def travel(root):
    if root == None:
        return
    print(root.item, end=' ')
    travel(root.left)
    travel(root.right)

travel(root)
