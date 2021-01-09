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

nums1 = [1, 2, 3, 4]
head1 = link().CreateLink(nums1)

nums2 = [1, 4, 6, 7]
head2 = link().CreateLink(nums2)

def mergeTwoLists(head1, head2):
    if not head1 and not head2:return
    Pre = linknode(None)
    tmp = Pre
    while head1 and head2:
        if head1.val < head2.val:
            Pre.next = head1
            head1 = head1.next
        else:
            Pre.next = head2
            head2 = head2.next
        Pre = Pre.next
    Pre.next = head1 if head1 else head2
    return tmp.next
# 验证
print('验证结果')
head = mergeTwoLists(head1, head2)
while head:
    print(head.val, end=',')
    head = head.next


