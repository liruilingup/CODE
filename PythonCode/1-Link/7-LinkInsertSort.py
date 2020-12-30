
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

nums = [5, 7, 3, 4]
head = link().CreateLink(nums)

'''链表的插入排序'''
def LinkInsertSort(head):
    dummy = linknode(0)
    cur = head
    while cur:
        pre = dummy
        while pre.next and pre.next.val <= cur.val:
            pre = pre.next
        tmp = cur.next
        cur.next = pre.next
        pre.next = cur
        cur = tmp
    return dummy.next

head = LinkInsertSort(head)
while head:
    print(head.val)
    head = head.next
