'''
一、奇数个：
链表：1->2->3->4->5
断开链表：1->2->3, 5->4
合并：1->5->2->4->3

二、偶数个：
链表：1->2->3->4->5->6
断开链表：1->2->3, 6->5->4
合并：1->6->2->5->3->4

'''

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def CreateLink(nums):
    tmp = LinkNode(None)
    sen = tmp
    for i in nums:
        node = LinkNode(i)
        tmp.next = node
        tmp = tmp.next
    return sen.next

head = CreateLink([1,2,3,4,5])
# head = CreateLink([1,2,3,4,5,6])

def reverse(head):
    if not head or not head.next:return head
    Pre = None
    while head:
        tmp = head
        head = head.next
        tmp.next = Pre
        Pre = tmp
    return Pre

def breakLink(head):
    slow, fast = head, head
    while fast and fast.next:
        Pre = slow
        slow = slow.next
        fast = fast.next.next

    if not fast:
        Pre.next = None
        l2 = reverse(slow)
    else:
        l2 = slow.next
        slow.next = None
        l2 = reverse(l2)

    l1 = head
    i = 0
    Pre = LinkNode(None)
    sen = Pre

    while l1 and l2:
        if i % 2 == 0:
            Pre.next = l1
            l1 = l1.next
        else:
            Pre.next = l2
            l2 = l2.next
        i += 1
        Pre = Pre.next
    Pre.next = l1 if l1 else l2

    sen = sen.next
    while sen:
        print(sen.val)
        sen = sen.next

breakLink(head)
