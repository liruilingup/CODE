class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)

'''层次遍历使用队列实现'''
def LevelorderTraversal(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        CurlevelItem = []
        next_level_node = []  # 使用中间变量存储每一层
        for node in queue:
            CurlevelItem.append(node.item)
            if node.left:
                next_level_node.append(node.left)
            if node.right:
                next_level_node.append(node.right)
        res.append(CurlevelItem)
        queue = next_level_node
    return res
print(LevelorderTraversal(root))


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
print(LevelorderTraversal1(root))




