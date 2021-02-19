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

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = link().CreateLink(nums)


'''需要记录头结点个尾结点'''
def reverse(head, tail):
    start = head
    end = tail.next
    pre = None
    while start!=end:
        tmp = start
        start = start.next
        tmp.next = pre
        pre = tmp

    return pre, head

def reverseKGroup(head, k):
    Pre = linknode(None)
    sen = Pre

    while head:
        tail = head
        for i in range(k-1):
            tail = tail.next
            if not tail:
                return sen.next
        newStart = tail.next
        head, tail = reverse(head, tail)

        Pre.next = head
        tail.next = newStart
        head = newStart
        Pre = tail

    return sen.next

newHead = reverseKGroup(head, 2)
while newHead:
    print(newHead.val)
    newHead = newHead.next