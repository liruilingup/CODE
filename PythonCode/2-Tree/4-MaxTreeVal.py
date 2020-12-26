class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)



'''求树的最大值'''
def maxVal(root):
    if not root:return -1 # 不能返回的是空
    item = root.item
    left = maxVal(root.left)
    right = maxVal(root.right)

    return max(item, left, right)
print(maxVal(root))


