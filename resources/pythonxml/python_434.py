class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        curr = head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        cut = count - k % count
        curr.next = head
        while cut:
            curr = curr.next
            cut -= 1
        newHead = curr.next
        curr.next = None
        return newHead