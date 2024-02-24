class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        curr = new_head
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            curr.next = node2
            node1.next = node2.next
            node2.next = node1
            curr = node1
        return new_head.next