




class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        index = 1
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre = dummy_head

        reverse_start = dummy_head
        while reverse_start.next and index < left:
            reverse_start = reverse_start.next
            index += 1

        pre = reverse_start
        cur = pre.next
        while cur and index <= right:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            index += 1

        reverse_start.next.next = cur
        reverse_start.next = pre
        
        return dummy_head.next