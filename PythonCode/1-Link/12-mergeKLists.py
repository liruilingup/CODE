'''合并k个链表'''

'''方法一、分治法'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 创建一个链表，不使用头结点
class link:
    def __init__(self):
        return

    def CreateLink(self, nums):
        head = ListNode(None)
        tmp = head
        for i in nums:
            node = ListNode(i)
            tmp.next = node
            tmp = node

        return head.next

nums = [1, 2, 3, 4]
head = link().CreateLink(nums)

def merge(node_a, node_b):
    dummy = ListNode(None)
    cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
    while cursor_a and cursor_b:  # 对两个节点的 val 进行判断，直到一方的 next 为空
        if cursor_a.val <= cursor_b.val:
            cursor_res.next = ListNode(cursor_a.val)
            cursor_a = cursor_a.next
        else:
            cursor_res.next = ListNode(cursor_b.val)
            cursor_b = cursor_b.next
        cursor_res = cursor_res.next
    # 有一方的next的为空，就没有比较的必要了，直接把不空的一边加入到结果的 next 上
    if cursor_a:
        cursor_res.next = cursor_a
    if cursor_b:
        cursor_res.next = cursor_b
    return dummy.next

def mergeKLists(lists) :
    length = len(lists)

    # 边界情况
    if length == 0:
        return None
    if length == 1:
        return lists[0]

    # 分治
    mid = length // 2
    return merge(mergeKLists(lists[:mid]), mergeKLists(lists[mid:length]))

