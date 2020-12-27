class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)


'''递归的创建二叉树的镜像'''
def MirrorTree(root):
    if not root: return
    if root.left or root.right:
        root.left, root.right = root.right, root.left
    MirrorTree(root.left)
    MirrorTree(root.right)
    return root

# 验证
def LevelorderTraversal1(root):
    res = []
    queue = [root]
    while queue:
        LevelItem = []
        for i in range(len(queue)): # 不使用中间变量存储每一层
            node = queue.pop(0)
            LevelItem.append(node.item)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(LevelItem)
    return res
print('二叉树', LevelorderTraversal1(root))
mirrorroot = MirrorTree(root)
print('二叉树镜像', LevelorderTraversal1(mirrorroot))