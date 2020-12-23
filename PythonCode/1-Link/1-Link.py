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
while head:
    print(head.val)
    head = head.next


# 创建一个链表，使用头结点
class linkhead:
    def __init__(self):
        self.head = linknode(None)

    def CreateLink(self, nums):
        tmp = self.head
        for i in nums:
            node = linknode(i)
            tmp.next = node
            tmp = node
        return self.head.next
# nums = [4,5,6,7]
# head1 = linkhead().CreateLink(nums)
# while head1:
#     print(head1.val)
#     head1 = head1.next






