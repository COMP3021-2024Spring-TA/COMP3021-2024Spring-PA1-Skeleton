class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next
        else:
            next = self.tail
            for _ in range(self.size - index):
                next = next.prev
            prev = next.prev

        self.size += 1
        add_node = ListNode(val)
        add_node.prev = prev
        add_node.next = next
        prev.next = add_node
        next.prev = add_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next.next
        else:
            next = self.tail
            for _ in range(self.size - index - 1):
                next = next.prev
            prev = next.prev.prev

        self.size -= 1
        prev.next = next
        next.prev = prev