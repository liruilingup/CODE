
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

'''方法1，使用栈，先进后出'''
def reversePrint(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res[::-1]
print('栈方法', reversePrint(head))

'''方法2，链表递归'''
def reversePrint2(head):
    return reversePrint2(head.next) + [head.val] if head else []

reversePrint2(head)
print('栈方法', reversePrint2(head))


