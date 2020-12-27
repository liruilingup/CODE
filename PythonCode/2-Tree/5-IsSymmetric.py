class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(3), treenode(4))
right = treenode(2, treenode(4), treenode(3))
root = treenode(1, left, right)



'''使用递归的方式'''
def IsSymmetric(root):
    def recur(L, R):
        if not L and not R:
            return True
        if not L or not R or L.item != R.item:
            return False
        return recur(L.left, R.right) and recur(L.right, R.left)
    return recur(root.left, root.right) if root else True

print('使用递归的方式', IsSymmetric(root))

'''使用层次遍历的方式'''
def IterIsSymmetric(root):
    if not root: return True

    queue = [root]
    while queue:
        res = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                res.append(node.left.item)
            else:
                res.append(None)
            if node.right:
                queue.append(node.right)
                res.append(node.right.item)
            else:
                res.append(None)
        mid = len(res) // 2
        if res[:mid] != res[mid:][::-1]:
            return False
    return True
print('使用层次遍历的方式', IterIsSymmetric(root))

