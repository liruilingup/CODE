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

nums = [1, 2, 3, 4]
head = link().CreateLink(nums)

# 方法一使用双指针
def reverseList(head):
    if not head:return head
    Pre = None
    while head:
        tmp = head
        head = head.next
        tmp.next = Pre
        Pre = tmp
    return Pre

# 方法二使用递归
def reverseList1(head):
    if not head or not head.next: return head
    last = reverseList1(head.next)
    head.next.next = head
    head.next = None
    return last

headNew = reverseList1(head)
while headNew:
    print(headNew.val)
    headNew = headNew.next

