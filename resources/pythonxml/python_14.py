
def length(self):
    count = 0
    cur = self.head
    while cur:
        count += 1
        cur = cur.next 
    return count