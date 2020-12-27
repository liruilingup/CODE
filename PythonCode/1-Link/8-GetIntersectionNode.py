class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 创建节点相交的链表
class link:
    def __init__(self):
        return

    def CreateLink(self, nums, nums1, nums2):

        # 创建链表1
        head1 = linknode(None)
        tmp1 = head1
        for i in nums1:
            node = linknode(i)
            tmp1.next = node
            tmp1 = node

        # 创建链表2
        head2 = linknode(None)
        tmp2 = head2
        for i in nums2:
            node = linknode(i)
            tmp2.next = node
            tmp2 = node

        # 创建共同的链表
        head = linknode(None)
        tmp = head
        for i in nums:
            node = linknode(i)
            tmp.next = node
            tmp = node


        tmp1.next = head.next
        tmp2.next = head.next

        return head1.next, head2.next

        # return head.next

'''两个相交的链表'''
def getIntersectionNode(head1, head2):
    res = set()
    while head1:
        res.add(head1)
        head1 = head1.next
    while head2:
        if head2 in res:
            return head2.val
        head2 = head2.next

    return None

nums = [8, 4, 5]
nums1 = [4, 1]
nums2 = [5, 0, 1]
head1, head2 = link().CreateLink(nums, nums1, nums2)
print(getIntersectionNode(head1, head2))

