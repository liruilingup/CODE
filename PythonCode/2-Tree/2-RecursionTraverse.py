class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


# 构建树结构
leafnode4=treenode(4)
leafnode5=treenode(5)
leafnode6=treenode(6)
leafnode7=treenode(7)
left = treenode(2, leafnode4, leafnode5)
right = treenode(3, leafnode6, leafnode7)
root = treenode(1, left, right)

print('------'+'前序遍历'+'------')
def PreorderRecursionTraverse(root):
    if not root:
        return
    print(root.item)
    PreorderRecursionTraverse(root.left)
    PreorderRecursionTraverse(root.right)
PreorderRecursionTraverse(root)

print('------'+'中序遍历'+'------')
def InorderRecursionTraverse(root):
    if not root:
        return
    InorderRecursionTraverse(root.left)
    print(root.item)
    InorderRecursionTraverse(root.right)
InorderRecursionTraverse(root)

print('------'+'后序遍历'+'------')
def PostorderRecursionTraverse(root):
    if not root:
        return
    PostorderRecursionTraverse(root.left)
    PostorderRecursionTraverse(root.right)
    print(root.item)
PostorderRecursionTraverse(root)
