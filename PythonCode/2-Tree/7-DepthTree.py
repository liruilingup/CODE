class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2)
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)


'''二叉树的深度'''
# 二叉树的最大深度
def MaxDepthTree(root):
    if not root: return 0
    return 1 + max(MaxDepthTree(root.left), MaxDepthTree(root.right))
print('最大深度', MaxDepthTree(root))

# 二叉树的最小深度,start是根节点，end是叶子节点
def MinDepthTree(root):
    if not root:return 0
    queue = [root]
    depth = 1
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return depth
print('最小深度', MinDepthTree(root))

