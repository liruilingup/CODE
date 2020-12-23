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

'''使用递归前序遍历链表'''
def PreorderRecursionTraverse(head):
    '''方式1'''
    if not head:
        return
    print(head.val)
    PreorderRecursionTraverse(head.next)

    '''方式2'''
    # if head:
    #     print(head.val)
    #     RecursionTraverse(head.next)

nums = [1,2,3,4,5]
head = CreakLink(nums)
PreorderRecursionTraverse(head)