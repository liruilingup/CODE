class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
leaf = treenode(10, treenode(6), treenode(7))
left = treenode(2)
right = treenode(3, leaf, treenode(8))
root = treenode(1, left, right)

'''判断是否是一颗二叉搜索树BST'''
def IsValidBST(root):
    def bst(root, minvalue, maxvalue):
        if not root: return True
        if root.item <= minvalue or root.item >= maxvalue: return False
        return bst(root.left, minvalue, root.item) and bst(root.right, root.item, maxvalue)

    return bst(root, float("-inf"), float("inf"))
print('是否是二叉搜索树', IsValidBST(root))

'''使用中序遍历判断'''
def InorderIsValidBST(root):
    stack = []
    node = root
    tmp = None
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if tmp and node.item <= tmp.item:
            return False
        tmp = node
        node = node.right
    return True
print('中序遍历判断是否是二叉搜索树', InorderIsValidBST(root))


