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

'''反转链表'''
def ReverseLink(head):
    Pre = linknode(None) # 最后也会有个None
    while head:
        tmp = head
        head = head.next
        tmp.next = Pre
        Pre = tmp

    return Pre

head = link().CreateLink([1,2,3,4,5])

reversehead = ReverseLink(head)
while reversehead:
    print(reversehead.val)
    reversehead = reversehead.next




