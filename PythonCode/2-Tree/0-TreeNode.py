class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

tree2 = TreeNode(2, TreeNode(4), TreeNode(5))
tree3 = TreeNode(3, TreeNode(6), TreeNode(7))
root = TreeNode(1, tree2, tree3)

def PreTraverse(root):
    if not root:return []
    return [root.val] + PreTraverse(root.left) + PreTraverse(root.right)

def InTraverse(root):
    if not root:return []
    return InTraverse(root.left) + [root.val] + InTraverse(root.right)

'''根据前序和中序构建二叉树'''
preorder = PreTraverse(root)
inorder = InTraverse(root)
print(preorder)
def PreInBuildTree(Pre, In):
    if not Pre:return
    if len(Pre) == 1:return TreeNode(Pre[0])
    root = TreeNode(Pre[0])
    index = In.index(Pre[0])
    root.left = PreInBuildTree(Pre[1:index+1], In[:index])
    root.right = PreInBuildTree(Pre[index+1:], In[index+1:])
    return root

print(PreTraverse(PreInBuildTree(preorder, inorder)))

'''使用栈的方式进行前序遍历'''
def stackReverse(root):
    if not root:return []
    stack = []
    res = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res

