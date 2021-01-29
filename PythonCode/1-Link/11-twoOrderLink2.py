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

'''
链表奇数递增，偶数递减，进行排序o(n)
1、奇数链表
2、偶数链表反转
3、有序链表合并
'''
def sortLink2(head):
    link1 = linknode(None)
    tmp1 = link1

    Pre = None

    while head and head.next:
        link1.next = head
        link1 = link1.next
        head = head.next

        # 偶数链表反转
        tmp = head
        head = head.next
        tmp.next = Pre
        Pre = tmp


    if head: # 奇数
        link1.next = head
    else: #偶数
        link1.next = None

    left = tmp1.next
    right = Pre

    newlink = linknode(None)
    sen = newlink

    while left and right:
        if left.val < right.val:
            newlink.next = left
            left = left.next
        else:
            newlink.next = right
            right = right.next
        newlink = newlink.next

    newlink.next = left if left else right
    return sen.next

nums = [1, 6, 3, 4, 5, 2, 7]
head = link().CreateLink(nums)
newhead = sortLink2(head)
while newhead:
    print(newhead.val)
    newhead = newhead.next

