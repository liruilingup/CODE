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

'''删除链表节点'''
def DeleteNode(head, val):
    if not head:
        return head
    tmp = linknode(None)
    pre = tmp

    tmp.next = head
    while head:
        if head.val == val:
            tmp.next = head.next
        else:
            tmp = head
        head = head.next
    return pre.next


head = CreakLink([1,3,4,5,6])
newhead = DeleteNode(head, 4)

while newhead:
    print(newhead.val)
    newhead = newhead.next

