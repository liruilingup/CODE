'''剑指 Offer 07. 重建二叉树'''
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]

class treenode:  #定义树的数据结构
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 创建一颗树
print('------创建的树------')
# left = treenode(2, right = treenode(4))
# right = treenode(3)
# root = treenode(1, left, right)
left = treenode(2, treenode(4), treenode(5))
right = treenode(3,treenode(6), treenode(7))
root = treenode(1, left, right)

# 前序遍历
def PreTraverse(root, PreRes):
    def dfs(root):
        if not root:
            return
        PreRes.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return PreRes

# 中序遍历
def InTraverse(root, InRes):
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        InRes.append(root.val)
        dfs(root.right)
    dfs(root)
    return InRes

# 后序遍历
def PostTraverse(root, PostRes):
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        PostRes.append(root.val)
    dfs(root)
    return PostRes
PreRes = PreTraverse(root, [])
InRes = InTraverse(root, [])
PostRes = PostTraverse(root, [])
print('前序结果', PreRes)
print('中序结果', InRes)
print('后序结果', PostRes)



def PreInorderBuildTree(pre, inorder):
    if not pre:
        return
    if len(pre) == 1:
        return treenode(pre[0])
    root = treenode(pre[0])
    index = inorder.index(pre[0])
    root.left = PreInorderBuildTree(pre[1:index+1], inorder[:index])
    root.right = PreInorderBuildTree(pre[index+1:], inorder[index+1:])
    return root
root = PreInorderBuildTree(PreRes, InRes)
print('结果：',PreTraverse(root, []), InTraverse(root, []))

