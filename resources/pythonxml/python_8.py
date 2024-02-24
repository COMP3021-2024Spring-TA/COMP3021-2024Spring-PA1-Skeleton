class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k = 0
        curr = head
        while k < n // 2:
            k += 1
            curr = curr.next
        return curr