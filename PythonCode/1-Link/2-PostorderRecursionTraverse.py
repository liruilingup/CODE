class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None

def CreakLink(nums):
    head = linknode(None)
    tmp = head

    for i in nums:
        node = linknode(i)
        tmp.next = node
        tmp = node
    return head.next


'''使用递归后序遍历链表'''
def PostorderRecursionTraverse(head):
    if not head:
        return
    PostorderRecursionTraverse(head.next)
    print(head.val)

nums = [1,2,3,4,5]
head = CreakLink(nums)
PostorderRecursionTraverse(head)
