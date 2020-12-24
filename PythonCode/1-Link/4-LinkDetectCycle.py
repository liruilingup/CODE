class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None

'''创建有环链表'''
def CreakLinkHasCycle(nums, n):
    head = linknode(None)
    tmp = head

    for i in nums:
        node = linknode(i)
        tmp.next = node
        tmp = node

    # 创建有环的链表
    cur = head.next
    for _ in range(n):
        cur = cur.next

    tmp.next = cur
    return head.next

'''找到成环的节点'''
def LinkDetectCycle(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow.val
nums = [1,2,3,4,5,6]
head = CreakLinkHasCycle(nums, 2)
print(LinkDetectCycle(head))
