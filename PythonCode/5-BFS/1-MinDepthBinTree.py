class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2)
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)

'''其实就是二叉树的层次遍历，使用队列实现'''
def MinDepthBinTree(root):
    if not root:
        return 0
    queue = [root]
    depth = 1
    while queue:
        # 将队列中的所有点向四周扩散
        for i in range(len(queue)):
            cur = queue.pop(0)
            if cur.left == None and cur.right == None:
                return depth
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        depth += 1
    return depth
print(MinDepthBinTree(root))

