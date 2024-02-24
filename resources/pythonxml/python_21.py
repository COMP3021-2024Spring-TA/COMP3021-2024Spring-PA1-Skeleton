
def removeRear(self):
    if not self.head or not self.head.next:
        return 'Error'

    cur = self.head
    while cur.next.next:
        cur = cur.next
    cur.next = None