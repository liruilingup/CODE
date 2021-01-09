'''剑指 Offer 34. 二叉树中和为某一值的路径'''

# 定义树的数据结构
class treenode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(11, treenode(7), treenode(2))
right = treenode(4, treenode(5), treenode(1))
left = treenode(4, left = left)
right = treenode(8, treenode(13), right)
root = treenode(5, left, right)

def pathSum(root, sum):
    if not root:return []
    res, path = [], []
    def recur(root, tar):
        if not root:return
        path.append(root.val)
        tar -= root.val
        if tar == 0 and not root.left and not root.right:
            res.append(list(path))
        recur(root.left, tar)
        recur(root.right, tar)
        path.pop()
    recur(root, sum)
    return res
print(pathSum(root, 22))
