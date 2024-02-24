class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        slow = head
        fast = head
        for _ in range(k):
            if fast == None:
                return fast
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val