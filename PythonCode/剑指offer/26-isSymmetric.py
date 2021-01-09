class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(3), treenode(4))
right = treenode(2, treenode(4), treenode(3))
root = treenode(1, left, right)

'''层次遍历'''
def traversetree(root):
    queue = [root]
    res = []
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res
print('层次遍历看', traversetree(root))



def isSymmetric(root):
    if not root:return True
    def recur(L, R):
        if not L and not R:return True
        if not L or not R or L.val != R.val:return False
        return recur(L.left, R.right) and recur(L.right, R.left)

    return recur(root.left,root.right)
print('递归的结果：', isSymmetric(root))


'''方法二、使用层次遍历的方式判断'''
def isSymmetric2(root) :
    if not root: return True
    queue = [root]
    while queue:
        res = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                res.append(node.left.val)
            else:
                res.append(None)
            if node.right:
                queue.append(node.right)
                res.append(node.right.val)
            else:
                res.append(None)
        mid = len(res) // 2
        if res[:mid] != res[mid:][::-1]:
            return False
    return True
