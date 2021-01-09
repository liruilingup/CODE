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

nums = [1, 2, 3, 4, 5, 6, 7]
head = link().CreateLink(nums)


'''------倒数k个节点-------'''
def getKthFromEnd(head, k):
    if not head or not k:return head
    tmp = head
    for i in range(k):
        head = head.next

    while head:
        head = head.next
        tmp = tmp.next
    return tmp
