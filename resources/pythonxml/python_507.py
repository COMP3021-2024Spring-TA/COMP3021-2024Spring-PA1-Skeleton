class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.move_node(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_node(node)
            return
        if len(self.hashmap) == self.capacity:
            self.hashmap.pop(self.head.next.key)
            self.remove_node(self.head.next)

        node = Node(key=key, val=value)
        self.hashmap[key] = node
        self.add_node(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def add_node(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node


    def move_node(self, node):
        self.remove_node(node)
        self.add_node(node)