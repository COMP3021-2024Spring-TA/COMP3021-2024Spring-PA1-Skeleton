class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head
        for _ in range(k):
            if fast == None:
                return fast
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow