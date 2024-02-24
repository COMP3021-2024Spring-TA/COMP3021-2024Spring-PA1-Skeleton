class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        ans = head
        while ans != slow:
            ans, slow = ans.next, slow.next
        return ans    