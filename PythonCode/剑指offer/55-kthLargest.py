class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
tree2 = treenode(2, treenode(1), treenode(3))
tree5 = treenode(6, treenode(5), treenode(7))
root4 = treenode(4, tree2, tree5)

class Solution:
    def __init__(self):
        return

    def kthLargest(self, root, k):

        def dfs(root):
            if not root:return
            dfs(root.right)
            if self.k==0: return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.res = -1
        self.k = k
        dfs(root)
        return self.res

print(Solution().kthLargest(root4, 1))
print(Solution().kthLargest(root4, 2))
print(Solution().kthLargest(root4, 3))
print(Solution().kthLargest(root4, 4))
print(Solution().kthLargest(root4, 5))
print(Solution().kthLargest(root4, 6))
print(Solution().kthLargest(root4, 7))
