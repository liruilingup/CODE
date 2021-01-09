def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left and not right: return  # 1.
    if not left: return right  # 3.
    if not right: return left  # 4.
    return root  # 2. if left and right: