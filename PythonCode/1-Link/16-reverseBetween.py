# 链表反转
class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None


def CreateLink(nums):
    Pre = LinkNode(None)
    dummy = Pre
    for i in nums:
        node = LinkNode(i)
        Pre.next = node
        Pre = Pre.next
    return dummy.next

# 反转m,n位置的链表
def reverseBetween(head, m, n):
    if not head or not m or not n:return head
    dummy = LinkNode(None)
    dummy.next = head

    if m==1:
        Pre = dummy
    else:
        for i in range(1, m):
            Pre = head
            head = head.next
    end = head
    start = None
    for i in range(m, n+1):
        tmp = head
        head = head.next
        tmp.next = start
        start = tmp
    Pre.next = start
    end.next = head

    return dummy.next


head = CreateLink([1,2,3,4,5])
head = reverseBetween(head, 1, 5)
while head:
    print(head.val, end=' ')
    head =  head.next

