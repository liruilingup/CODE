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


'''归并排序链表'''
def SortLink(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    left, right = SortLink(head), SortLink(mid)
    h = res = linknode(None)

    while left and right:
        if left.val < right.val:
            h.next = left
            left = left.next
        else:
            h.next = right
            right = right.next
        h = h.next
    h.next = left if left else right
    return res.next

nums1 = [-1, 5, 3, 4, 0]
h = link().CreateLink(nums1)
head = SortLink(h)
while head:
    print(head.val)
    head = head.next