
def change(self, index, val):
    count = 0
    cur = self.head
    while cur and count < index:
        count += 1
        cur = cur.next
        
    if not cur:
        return 'Error'
    
    cur.val = val