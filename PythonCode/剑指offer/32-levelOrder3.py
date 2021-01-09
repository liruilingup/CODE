class treenode:  #定义树的数据结构
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right

# 创建一颗树
left = treenode(2, treenode(4), treenode(5))
right = treenode(3, treenode(6), treenode(7))
root = treenode(1, left, right)

'''方法一、判断偶数层倒序'''
def levelOrder(root):
    if not root: return []
    res = []
    queue = [root]
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(tmp if len(res) % 2 == 0 else tmp[::-1])
    return res
print(levelOrder(root))

'''方法二、使用双端队列，'''
def levelOrder2(root):
    if not root: return []
    res = []
    queue = [root]
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if len(res) % 2==1 :
                tmp.insert(0, node.val) # 偶数层 -> 队列头部
            else:
                tmp.append(node.val) # 奇数层 -> 队列头部
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res

print(levelOrder2(root))

'''方法三、奇偶层分别'''
import collections
def levelOrder3(root):
    if not root: return []
    res, deque = [], collections.deque()
    deque.append(root)
    while deque:
        tmp = []
        # 打印奇数层
        for _ in range(len(deque)):
            # 从左向右打印
            node = deque.popleft()
            tmp.append(node.val)
            # 先左后右加入下层节点
            if node.left: deque.append(node.left)
            if node.right: deque.append(node.right)
        res.append(tmp)
        if not deque: break  # 若为空则提前跳出
        # 打印偶数层
        tmp = []
        for _ in range(len(deque)):
            # 从右向左打印
            node = deque.pop()
            tmp.append(node.val)
            # 先右后左加入下层节点
            if node.right: deque.appendleft(node.right)
            if node.left: deque.appendleft(node.left)
        res.append(tmp)
    return res

print(levelOrder3(root))