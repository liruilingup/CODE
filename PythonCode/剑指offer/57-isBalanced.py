def isBalanced(self, root) -> bool:
    if not root: return True
    left = self.depth(root.left)
    right = self.depth(root.right)

    if abs(left - right) > 1: return False

    return self.isBalanced(root.right) and self.isBalanced(root.left)


def depth(self, root):
    if not root: return 0

    return 1 + max(self.depth(root.left), self.depth(root.right))