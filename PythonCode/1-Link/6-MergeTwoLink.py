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

nums1 = [1, 2, 4]
head1 = link().CreateLink(nums1)

nums2 = [1, 3, 4]
head2 = link().CreateLink(nums2)

'''合并两个有序链表'''
def mergeTwoLink(l1, l2):
    Pre = linknode(None)
    sen = Pre

    while l1 and l2:
        if l1.val < l2.val:
            Pre.next = l1
            l1 = l1.next
        else:
            Pre.next = l2
            l2 = l2.next
        Pre = Pre.next
    Pre.next = l1 if l1 else l2
    return sen.next

# 验证
head = mergeTwoLink(head1, head2)
while head:
    print(head.val)
    head = head.next
