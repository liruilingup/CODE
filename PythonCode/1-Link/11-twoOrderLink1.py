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
把链表的奇偶分开，跟链表长度就有关系
最后断开链表时
    链表长度奇数：
        奇数链表.next = head
        偶数链表.next = None
    链表长度偶数：
        奇数链表.next = None
        偶数链表.next = head
'''

def sortLink1(head):
    link1 = linknode(None)
    tmp1 = link1

    link2 = linknode(None)
    tmp2 = link2

    while head and head.next:
        link1.next = head
        link1 = link1.next
        head = head.next

        link2.next = head
        link2 = link2.next
        head = head.next

    if head: # 奇数
        link1.next = head
        link2.next = None
    else: #偶数
        link1.next = None
        link2.next = head
    tmp1 = tmp1.next
    tmp2 = tmp2.next
    print('奇数链表：')
    while tmp1:
        print(tmp1.val, end=' ')
        tmp1 = tmp1.next
    print('\n偶数链表：')
    while tmp2:
        print(tmp2.val, end=' ')
        tmp2 = tmp2.next

# nums = [1, 200, 10, 120, 30, 8, 88]
nums = [1,2,3,4,5,6,7]
head = link().CreateLink(nums)
sortLink1(head)

