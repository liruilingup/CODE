class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None

'''创建无环链表'''
def CreakLinkNoCycle(nums):
    head = linknode(None)
    tmp = head

    for i in nums:
        node = linknode(i)
        tmp.next = node
        tmp = node

    return head.next

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

'''判断是否有环'''
def LinkHasCycle(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

nums = [1,2,3,4,5,6]
has_cycle_head = CreakLinkHasCycle(nums, 3)
print('有环', LinkHasCycle(has_cycle_head))
no_cycle_head = CreakLinkNoCycle(nums)
print('无环', LinkHasCycle(no_cycle_head))

