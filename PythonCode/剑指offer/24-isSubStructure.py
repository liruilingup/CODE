class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树1
left = treenode(4, treenode(1), treenode(2))
right = treenode(5)
root1 = treenode(3, left, right)

# 创建一颗树2
root2 = treenode(4, left=treenode(1))

def isSubStructure(A, B):
    if not A or not B: return False
    def recur(s, t):
        if not t: return True # 顺序不能反
        if not s: return False
        return s.val == t.val and recur(s.left, t.left) and recur(s.right, t.right)

    return recur(A, B) or isSubStructure(A.left, B) or isSubStructure(A.right, B)

print(isSubStructure(root1, root2))
