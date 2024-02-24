
def find(self, val):
    cur = self.head
    while cur:
        if val == cur.val:
            return cur
        cur = cur.next

    return None