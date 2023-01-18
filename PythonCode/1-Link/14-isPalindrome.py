class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def CreatLink(nums):
    Pre = LinkNode(None)
    sen = Pre
    for i in nums:
        node = LinkNode(i)
        Pre.next = node
        Pre = Pre.next
    return sen.next

head = CreatLink([1,2,3,3,2,1])
head = CreatLink([1,2,3,2,1])
# head = CreatLink([1,0,0])

def isPalindrome(head):
    if not head or not head.next:return True
    slow, fast = head, head
    left = None
    while fast and fast.next:
        fast = fast.next.next

        # 反转前面的链表
        tmp = slow
        slow = slow.next
        tmp.next = left
        left = tmp

    if fast:
        right = slow.next
    else:
        right = slow

    while left and right and left.val == right.val:
        left = left.next
        right = right.next
    return True if not left else False
print(isPalindrome(head))


def isPalindrome1(head):
    slow = fast = head
    pre = None
    while fast and fast.next:
        fast = fast.next.next
        tmp = slow
        slow = slow.next
        tmp.next = pre
        pre = tmp

    if fast:
        slow = slow.next

    while pre and pre.val == slow.val:
        pre = pre.next
        slow = slow.next

    return not pre



