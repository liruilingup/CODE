class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(1), treenode(3))
right = treenode(6)
root = treenode(5, left, right)

'''方法一、使用索引'''
def verifyPostorder(postorder):
    if not postorder:return True

    def recur(i, j): # 使用两个指针记录索引的变化
        if i >= j:return True
        p = i
        while postorder[p] < postorder[j]: #找到第一个比根大的节点
            p += 1
        m = p
        while postorder[p] > postorder[j]:
            p += 1
        return p == j and recur(i, m-1) and recur(m, j-1)

    return recur(0, len(postorder) - 1)

postorder = [1,6,3,2,5]

print(verifyPostorder(postorder))

'''方法二、使用栈'''

def verifyPostorder2(postorder):
    stack, root = [], float("+inf")
    for i in range(len(postorder) - 1, -1, -1):
        if postorder[i] > root: return False
        while (stack and postorder[i] < stack[-1]):
            root = stack.pop()
        stack.append(postorder[i])
    return True
print(verifyPostorder2(postorder))
