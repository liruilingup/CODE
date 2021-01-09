# 层序遍历
class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, right = treenode(4))
right = treenode(3)
root = treenode(1, left, right)


'''层序序列二叉树'''
def treeSerialize(root):
    if not root:return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node:
            res.append('#')
            continue
        res.append(node.item)
        queue.append(node.left)
        queue.append(node.right)
    return res
print('层次遍历序列化结果', treeSerialize(root))

res = treeSerialize(root)
'''层序反序列二叉树'''

def DeSerialize(res):
    if not res:
        return
    root = treenode(res[0])
    queue = [root] # 队列中只存父节点
    for i in range(1, len(res), 2):
        parent = queue.pop(0)
        left = res[i]
        if left != '#':
            parent.left = treenode(left)
            queue.append(parent.left)
        else:
            parent.left = None
        i += 1
        right = res[i]
        if right != '#':
            parent.right = treenode(right)
            queue.append(parent.right)
        else:
            parent.right = None
        print('', )
    return root
root = DeSerialize(res)

# 验证结果
def level(root):
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node:continue
        res.append(node.item)
        queue.append(node.left)
        queue.append(node.right)
    return res

print('验证结果', level(root))







