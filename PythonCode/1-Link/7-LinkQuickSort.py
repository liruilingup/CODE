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

nums = [5, 7, 3, 4]
head = link().CreateLink(nums)


def LinKQuickSort(head):
    if head is None:
        return head

    # 分成三个链表，分别是比轴心数小，相等，大的数组成的链表
    big = None
    small = None
    equal = None
    cur = head
    while cur:
        t = cur
        cur = cur.next
        if t.val < head.val:
            t.next = small
            small = t
        elif t.val > head.val:
            t.next = big
            big = t
        else:
            t.next = equal
            equal = t

    # 拆完各自排序即可，equal 无需排序
    big = LinKQuickSort(big)
    small = LinKQuickSort(small)

    ret = linknode(None)
    cur = ret

    # 将三个链表组合成一起，这一步复杂度是 o(n)
    # 可以同时返回链表的头指针和尾指针加速链表的合并。
    for p in [small, equal, big]:
        while p :
            cur.next = p
            p = p.next
            cur = cur.next
            cur.next = None
    return ret.next
head = LinKQuickSort(head)
while head:
    print(head.val)
    head = head.next
