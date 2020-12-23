class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None

'''创建链表'''
def CreakLink(nums):
    head = linknode(None)
    tmp = head

    for i in nums:
        node = linknode(i)
        tmp.next = node
        tmp = node
    return head.next

'''迭代访问'''
def IterationTraverse(head):
    while head:
        print(head.val)
        head = head.next

nums = [1,2,3,4]
head = CreakLink(nums)
IterationTraverse(head)