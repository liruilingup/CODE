def mergeTrees(t1, t2):
    def dfs(l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        l1.val += l2.val
        l1.left = dfs(l1.left, l2.left)
        l1.right = dfs(l1.right, l2.right)
        return l1

    return dfs(t1, t2)