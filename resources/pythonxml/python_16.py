
def insertFront(self, val):
    node = ListNode(val)
    node.next = self.head
    self.head = node