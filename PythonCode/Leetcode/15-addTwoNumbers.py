class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 创建一个链表，不使用头结点
class link:
    def __init__(self):
        return

    def CreateLink(self, nums):
        head = linknode(None)
        tmp = head
        for i in nums:
            node = linknode(i)
            tmp.next = node
            tmp = node

        return head.next

# nums1 = [9,9,9,9,9,9,9]
nums1 = [3,7]
head1 = link().CreateLink(nums1)


nums2 = [9,2]
head2 = link().CreateLink(nums2)

def addTwoNumbers(l1, l2):
    if not l1 and not l2: return l1
    s = 0
    dummy = tmp = linknode(None)
    while l1 or l2 or s:
        s = s + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        tmp.next = linknode(s % 10)
        tmp = tmp.next
        s //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


head=addTwoNumbers(head1, head2)

while head:
    print(head.val)
    head = head.next


