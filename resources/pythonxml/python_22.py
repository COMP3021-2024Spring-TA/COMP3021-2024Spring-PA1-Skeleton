
def removeInside(self, index):
    count = 0
    cur = self.head
    
    while cur.next and count < index - 1:
        count += 1
        cur = cur.next
        
    if not cur:
        return 'Error'
        
    del_node = cur.next
    cur.next = del_node.next