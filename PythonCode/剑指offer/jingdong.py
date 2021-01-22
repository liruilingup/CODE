'''删除链表中重复的节点'''

class linknode:
    def __init__(self,val):
        self.val = val
        self.next = None

def createLink(nums):
    tmp = linknode(None)
    Pre = tmp
    for i in nums:
        node = linknode(i)
        Pre.next = node
        Pre = Pre.next
    return tmp.next
head = createLink([1,2,2,3,3,4])

# while head:
#     print(head.val)
#     head = head.next

def deleteDuplicates(head):
    if not head:return

    sen = Pre = linknode(None)
    Pre.next = head

    while head.next:
        Pre = head
        tmp = head
        head = head.next
        if tmp.val == head.val:
            Pre.next = head.next

    return sen.next

# head = deleteDuplicates(head)
# while head:
#     print(head.val)
#     head = head.next


'''找出第二高薪水'''
# select a.Salary
# from
# (
#     select Salary
#     from Employee
#     group by Salary
# )a
# desc a.Salary
# limit(1,1)


'''字符类型转换成int
考虑各种情况
还有正负'''
def stringToInt(s):
    # 100000007
    res = 0
    if s[0]!='+' and s[0] !='-' and  s[0]<='0' or '9'<=s[0]:
        return -1
    if '0'<=s[0]<='9':
        for i in s:
            if '0'<i<'9':
                num = int(i)
                res += num
                if res > 100000007:
                    return 100000007
                    res = res % 100000007
                res *= 10
            else:
                break
    else:
        for i in s[1:]:
            if '0' < i < '9':
                num = int(i)
                res += num
                if res >100000007:
                    res = res % 100000007
                res *= 10
            else:
                break
    if s[0] == '+':
        return res
    elif s[0] == '-':
        return type((0-res) // 10)

    return (res // 10)

s = '1234'
s = '123a' #
s = 'a22'  # 0
s = '100000009'
print(stringToInt(s))
# s = '1234' # 默认正


# s = 333
# s = '-2343'
# s = '+111'






