'''108. 将有序数组转换为二叉搜索树'''

# 二叉搜索树的中序遍历是升序序列，题目给定的数组是按照升序排序的有序数组，因此可以确保数组是二叉搜索树的中序遍历序列。
# 有很多种解法

class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)

'''方法一：中序遍历，总是选择中间位置左边的数字作为根节点'''
def sortedArrayToBST(nums):
    def helper(left, right):
        if left > right:
            return None

        # 总是选择中间位置左边的数字作为根节点
        mid = (left + right) // 2

        root = treenode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(nums) - 1)

# 验证
root = sortedArrayToBST([1,2,3,4])
def inorder(root):
    if not root:return
    inorder(root.left)
    print(root.val, end = ', ')
    inorder(root.right)
inorder(root)
