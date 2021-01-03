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


'''部分链表反转'''
class Reverse():
    def __init__(self):
        self.successor = None
        return

    def NReverse(self, head, n):

        if n==1:
            self.successor = head.next
            return head
        last = self.NReverse(head.next, n-1)

        head.next.next = head
        head.next = self.successor
        return last

head = Reverse().NReverse(head, 2)
while head:
    print(head.val)
    head = head.next



