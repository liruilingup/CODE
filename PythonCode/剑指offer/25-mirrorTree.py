
class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(1), treenode(3))
right = treenode(7, treenode(6), treenode(9))
root = treenode(4, left, right)

'''层次遍历'''
def traversetree(root):
    queue = [root]
    res = []
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.item)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res
print('镜像反转之前', traversetree(root))

def mirrorTree(root):
    if not root:return

    def cur(root):
        if not root:return
        root.left, root.right = root.right, root.left
        if root.left:
            cur(root.left)
        if root.right:
            cur(root.right)
    cur(root)
    return root
root = mirrorTree(root)
print('镜像反转之后', traversetree(root))



