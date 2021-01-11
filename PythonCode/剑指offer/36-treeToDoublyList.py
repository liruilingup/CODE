# 如treenode(2).right=treenode(3)
# 要treenode(3).left=treenode(2)

def treeToDoublyList(self, root: 'Node') -> 'Node':
    def dfs(cur):
        if not cur: return
        dfs(cur.left) # 递归左子树
        if self.pre: # 修改节点引用
            self.pre.right, cur.left = cur, self.pre
        else: # 记录头节点
            self.head = cur # 第一次的时候用于保存头结点
        self.pre = cur # 保存 cur
        dfs(cur.right) # 递归右子树

    if not root: return
    self.pre = None
    dfs(root)
    self.head.left, self.pre.right = self.pre, self.head
    return self.head