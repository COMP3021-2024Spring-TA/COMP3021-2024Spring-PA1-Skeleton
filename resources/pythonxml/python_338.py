class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
    
    def reverseN(self, head, n):
        if n == 1:
            return head
        last = self.reverseN(head.next, n - 1)
        next = head.next.next
        head.next.next = head
        head.next = next
        return last