'''剑指 Offer 34. 二叉树中和为某一值的路径'''

# 定义树的数据结构
class treenode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(11, treenode(7), treenode(2))
right = treenode(4, treenode(5), treenode(1))
left = treenode(4, left = left)
right = treenode(8, treenode(13), right)
root = treenode(5, left, right)


'''方法1、DFS + 回溯'''
class PathSum:
    def __init__(self):
        self.res = []

        return

    def PathSum1(self, root, sum):
        self.dfs(root, [], sum)

        return self.res

    def dfs(self, node, stack, s):
        if not node:
            return
        stack.append(node.val)
        if s == node.val and not node.left and not node.right:
            self.res.append(stack.copy())
        self.dfs(node.left, stack, s-node.val)
        self.dfs(node.right, stack, s-node.val)
        stack.pop()

print('方法1：DFS + 回溯结果：', PathSum().PathSum1(root, 22))

'''方法2、DFS迭代'''
def DFSPathSum(root, sum):
    if not root:
        return []
    stack = [(root, root.val, [root.val])]
    res = []
    while stack:
        node, val, temp = stack.pop()
        if val == sum and not node.left and not node.right:
            res.append(temp)
        if node.right:
            stack.append((node.right, val+node.right.val, temp+[node.right.val]))
        if node.left:
            stack.append((node.left, val+node.left.val, temp+[node.left.val]))
    return res
print('方法2、DFS迭代结果：', DFSPathSum(root, 22))

'''方法3、BFS迭代'''
def BFSPathSum(root, sum):
    if not root:
        return []
    queue = [(root, root.val, [root.val])]
    res = []
    while queue:
        node, val, temp = queue.pop(0)
        if val == sum and not node.left and not node.right:
            res.append(temp)
        if node.left:
            queue.append((node.left, val+node.left.val, temp+[node.left.val]))
        if node.right:
            queue.append((node.right, val+node.right.val, temp+[node.right.val]))
    return res
print('方法3、BFS迭代结果：', BFSPathSum(root, 22))
