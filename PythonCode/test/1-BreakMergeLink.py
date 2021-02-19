'''
链表：1->2->3->4->5
断开链表：1->3->5,4->2
合并：1->4->3->2->5
'''


class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def CreateLink(nums):
    tmp = LinkNode(None)
    sen = tmp
    for i in nums:
        node = LinkNode(i)
        tmp.next = node
        tmp = tmp.next
    return sen.next

head = CreateLink([1,2,3,4,5])
# head = CreateLink([1,2,3,4,5,6])
def LinkHeadTail(head):
    # 先把链表拆开成奇偶，偶数链表反转，最后合并两个链表
    link1 = LinkNode(None)
    sen1 = link1

    link2 = None

    while head and head.next:
        link1.next = head
        head = head.next
        link1 = link1.next

        tmp = head
        head= head.next
        tmp.next = link2
        link2 = tmp

    if not head:
        link1.next = None
    else:
        link1.next = head

    l1 = sen1.next
    l2 = link2
    # print('奇数链表:')
    # while l1:
    #     print(l1.val, end=' ')
    #     l1 = l1.next
    # print('\n偶数链表:')
    # while l2:
    #     print(l2.val, end=' ')
    #     l2 = l2.next
    print('\n合并链表:')
    i = 0
    Pre = LinkNode(None)
    sen = Pre

    while l1 and l2:
        if i % 2 ==0:
            Pre.next = l1
            l1 = l1.next
        else:
            Pre.next = l2
            l2 = l2.next
        Pre = Pre.next
        i += 1
    Pre.next = l1 if l1 else l2
    sen = sen.next
    while sen:
        print(sen.val)
        sen = sen.next

LinkHeadTail(head)



