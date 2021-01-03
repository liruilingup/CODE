# 递归的反转链表
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

def reverse(head):
    if not head or not head.next:
        return head
    last = reverse(head.next)
    head.next.next = head  # head->x->y->z->None, head->x<-y<-z, x指向None, head.next.next = head可以反转
    head.next = None
    return last
head = reverse(head)

while head:
    print(head.val)
    head = head.next

