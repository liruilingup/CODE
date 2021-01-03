'''序列化和反序列化都需要先之后根节点，前序和后序都可以找到，中序遍历不可以'''
'''层序遍历可以'''


class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, right = treenode(4))
right = treenode(3)
root = treenode(1, left, right)


'''前序序列二叉树'''
res = []
def treeSerialize(root):
    if not root:
        res.append('#')
        return
    res.append(root.item)
    treeSerialize(root.left)
    treeSerialize(root.right)

treeSerialize(root)
print(res)


'''反序列二叉树，将前序遍历的结果变成树结构，先确定根节点'''
# res 是前序遍历的结果存放到了列表中
def Deserialize(res):
    if not res:
        return
    node = res.pop(0)  # 前序，第一个就是根节点，所有pop(0)
    if node == '#':
        return
    root = treenode(node)
    root.left = Deserialize(res)
    root.right = Deserialize(res)
    return root
root = Deserialize(res)


# 验证一下
def traverse(root):
    if not root:
        return
    print(root.item, end=' ')
    traverse(root.left)
    traverse(root.right)
traverse(root)
