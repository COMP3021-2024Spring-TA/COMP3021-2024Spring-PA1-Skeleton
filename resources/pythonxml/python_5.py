slow = head
fast = head

while n:
    fast = fast.next
    n -= 1
while fast:
    fast = fast.next
    slow = slow.next