# 前序遍历的特点是根节点始终出现在第一位
# 后序遍历的特点是根节点始终出现在最后一位

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

'''889. 根据前序和后序遍历构造二叉树'''
print('------根据前序和后序遍历构造二叉树-----')
def PrePostBuildTree(pre, post):
    if not pre:
        return
    if len(pre) == 1:
        return treenode(pre[0])
    root = treenode(pre[0])     # 根据前序数组的第一个元素，创建根节点
    left = post.index(pre[1])+1 # 根据前序数组第二个元素，确定后序数组左子树范围
    root.left = PrePostBuildTree(pre[1:left+1], post[:left]) # 递归执行前序数组左边、后序数组左边
    root.right = PrePostBuildTree(pre[left+1:], post[left:-1]) # 递归执行前序数组右边、后序数组右边
    return root

root = PrePostBuildTree(PreRes, PostRes)
print('结果:',PreTraverse(root, []), PostTraverse(root, []))

'''LeetCode105 从前序与中序遍历序列构造二叉树'''
print('------根据前序与中序遍历构造二叉树-----')

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

'''LeetCode106 从中序与后序遍历序列构造二叉树'''
print('------根据中序与后序遍历构造二叉树-----')

def InorderPostBuildTree(inorder, post):
    if not post:
        return
    if len(post) == 1:
        return treenode(post[-1])
    root = treenode(post[-1])
    index = inorder.index(post[-1])
    root.left = InorderPostBuildTree(inorder[:index], post[:index])
    root.right = InorderPostBuildTree(inorder[index+1:], post[index:-1])
    return root
root = InorderPostBuildTree(InRes, PostRes)
print('结果：', InTraverse(root, []), PostTraverse(root, []))