'''114. 二叉树展开为链表'''

class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)

def flatten(root):
    preorder = []
    def dfs(root):
        if not root:return
        preorder.append(root) # 添加的是根节点
        dfs(root.left)
        dfs(root.right)
    dfs(root)

    for i in range(1, len(preorder)):
        prev, curr = preorder[i - 1], preorder[i]
        prev.left = None
        prev.right = curr
    return root

root = flatten(root)

