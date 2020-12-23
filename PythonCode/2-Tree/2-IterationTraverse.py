class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


# 构建树结构
leafnode4=treenode(4)
leafnode5=treenode(5)
leafnode6=treenode(6)
leafnode7=treenode(7)
left = treenode(2, leafnode4, leafnode5)
right = treenode(3, leafnode6, leafnode7)
root = treenode(1, left, right)

print('------'+'前序遍历'+'------')
def PreorderIterationTraverse(root):
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            res.append(node.item)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    print(res)
PreorderIterationTraverse(root)


print('------'+'中序遍历'+'------')
def InorderIterationTraverse(root):
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.item)
        node = node.right
    print(res)
InorderIterationTraverse(root)

print('------'+'后序遍历'+'------')
def PostorderIterationTraverse(root):
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            res.append(node.item)
            stack.append(node)
            node = node.right
        node = stack.pop()
        node = node.left
    print(res[::-1])
PostorderIterationTraverse(root)