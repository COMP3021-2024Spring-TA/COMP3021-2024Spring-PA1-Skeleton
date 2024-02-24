class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow