
def insertInside(self, index, val):
    count = 0
    cur = self.head
    while cur and count < index - 1:
        count += 1
        cur = cur.next
        
    if not cur:
        return 'Error'
    
    node = ListNode(val)
    node.next = cur.next
    cur.next = node