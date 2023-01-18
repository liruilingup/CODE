class linknode:
    def __init__(self, val):
        self.val = val
        self.next = None







'''链表的一些常用操作'''


# 链表反转
class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None


def CreateLink(nums):
    Pre = LinkNode(None)
    dummy = Pre
    for i in nums:
        node = LinkNode(i)
        Pre.next = node
        Pre = Pre.next
    return dummy.next



# 反转链表
def reverseLink(head):
    if not head or not head.next:
        return head
    Pre = None
    while head:
        tmp = head
        head = head.next
        tmp.next = Pre
        Pre = tmp
    return Pre

# 递归的反转链表
def recursionReverse(head):
    if not head or not head.next:return head
    last = recursionReverse(head.next)
    head.next.next = head
    head.next = None

    return last

# 递归的遍历链表
def traverseLink(head):
    if not head:return
    traverseLink(head.next)
    print(head.val)


# 奇偶链表
def oddEvenList(head):
    if not head or not head.next:return head
    odd = LinkNode(None)
    o_dummy = odd
    even = LinkNode(None)
    e_dummy = even

    while head and head.next:
        odd.next = head
        odd = odd.next
        head = head.next

        even.next = head
        even = even.next
        head = head.next

    if head:# 奇数
        even.next = None
        odd.next = head
        odd = odd.next
    else: # 偶数
        odd.next = None

    odd.next = e_dummy.next

    return o_dummy.next

# 反转m,n位置的链表
def reverseBetween(head, m, n):
    if not head or not m or not n:return head
    dummy = LinkNode(None)
    dummy.next = head

    if m==1:
        Pre = dummy
    else:
        for i in range(1, m):
            Pre = head
            head = head.next
    end = head
    start = None
    for i in range(m, n+1):
        tmp = head
        head = head.next
        tmp.next = start
        start = tmp
    Pre.next = start
    end.next = head

    return dummy.next


def partition(head, x):
    p = less = LinkNode(0)
    q = more = LinkNode(0)

    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            more.next = head
            more = more.next
        head = head.next

    more.next = None
    less.next = q.next
    return p.next



def quickSortLink(head):
    if not head.next:return head
    small = None
    equal = None
    big = None
    cur = head
    while cur:
        t = cur
        cur = cur.next
        if t.val < head.val:# 使用的是后插法
            t.next = small
            small = t
        elif t.val > head.val:
            t.next = big
            big = t
        else:
            t.next = equal
            equal = t
    big = quickSortLink(big)
    small = quickSortLink(small)

    ret = cur = LinkNode(None)
    for p in [small, equal, big]:
        while p:
            cur.next = p
            p = p.next
            cur = cur.next
    return ret.next

head = CreateLink([4,1,3,2,5,2])
head = quickSortLink(head)

while head:
    print(head.val, end=' ')
    head =  head.next




