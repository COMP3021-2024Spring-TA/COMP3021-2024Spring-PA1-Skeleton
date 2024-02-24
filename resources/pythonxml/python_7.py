fast = head
slow = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next