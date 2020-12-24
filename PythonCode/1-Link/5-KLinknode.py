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

'''找到倒数第K个元素'''
def KLinknode(head, k):
    slow = fast = head
    while k:
        fast = fast.next
        k -= 1
    while fast:
        fast = fast.next
        slow = slow.next
    return slow, slow.val

nums = [1,2,3,4,5,6,7,8,9,10]
head = CreakLink(nums)
print(KLinknode(head, 10))


