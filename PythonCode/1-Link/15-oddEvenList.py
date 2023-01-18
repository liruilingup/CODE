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

head = CreateLink([1,2,3,4,5,6])

# 奇偶链表
def oddEvenList(head):
    if not head or not head.next:return head
    odd = LinkNode(None)
    o_dummy = odd
    even = LinkNode(None)
    e_dummy = even

    while head and head.next:
        odd.next = head
        odd = odd.next
        head = head.next

        even.next = head
        even = even.next
        head = head.next

    if head:# 奇数
        even.next = None
        odd.next = head
        odd = odd.next
    else: # 偶数
        odd.next = None

    odd.next = e_dummy.next

    return o_dummy.next

head = oddEvenList(head)
while head:
    print(head.val, end=' ')
    head =  head.next



