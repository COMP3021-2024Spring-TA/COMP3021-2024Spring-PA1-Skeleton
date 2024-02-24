class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(0, head)
        newHead.next = head

        prev, curr = newHead, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return newHead.next