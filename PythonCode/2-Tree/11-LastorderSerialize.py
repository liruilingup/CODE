
class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, right = treenode(4))
right = treenode(3)
root = treenode(1, left, right)

'''后序序列二叉树'''
res = []
def treeSerialize(root):
    if not root:
        res.append('#')
        return
    treeSerialize(root.left)
    treeSerialize(root.right)
    res.append(root.item)

treeSerialize(root)
print(res)


'''反序列二叉树，将后序遍历的结果变成树结构，先确定根节点'''
def Deserialize(res):
    if not res: return
    node = res.pop() # 后序，最后一个就是根节点，所有pop()
    if node == '#':
        return
    root = treenode(node)
    root.right = Deserialize(res) # 后序，先建立右子树
    root.left = Deserialize(res)
    return root

# 验证一下
def traverse(root):
    if not root:
        return
    traverse(root.left)
    traverse(root.right)
    print(root.item, end=' ')
traverse(root)