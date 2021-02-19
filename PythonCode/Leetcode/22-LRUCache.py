class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next = None
        self.pre = None

# 主要操作是增加一个节点
# 删除一个节点
# hashmap的key是key，value是node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap.keys():
            node = self.hashmap[key]
            self.del_key(key)
            self.add_new(key, node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap.keys():
            self.del_key(key)
            self.add_new(key, value)
        else:
            if len(self.hashmap) < self.capacity:
                self.add_new(key, value)
            else: # cache满了，需要删除最后面的节点
                node = self.head.next
                self.head.next = node.next
                node.next.pre = self.head
                del self.hashmap[node.key]
                self.add_new(key, value)

    def add_new(self, key, value):
        node = Node(key, value)
        # 双向链表
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        # hash
        self.hashmap[key] = node

    def del_key(self, key):
        node = self.hashmap[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.hashmap[key]