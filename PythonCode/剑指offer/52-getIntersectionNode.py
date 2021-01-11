'''
方法一:分别遍历链表
1、遍历链表1、使用集合存储节点
2、遍历链表2，判断节点是否存在集合中
方法二:双指针
使用两个指针分别指向两个链表的头结点同时遍历
'''
def getIntersectionNode(headA, headB):
    node1, node2 = headA, headB

    while node1 != node2:
        node1 = node1.next if node1 else headB
        node2 = node2.next if node2 else headA

    return node1