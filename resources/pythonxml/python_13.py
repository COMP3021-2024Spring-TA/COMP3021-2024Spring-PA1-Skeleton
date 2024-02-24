
def create(self, data):
    self.head = ListNode(0)
    cur = self.head
    for i in range(len(data)):
        node = ListNode(data[i])
        cur.next = node
        cur = cur.next