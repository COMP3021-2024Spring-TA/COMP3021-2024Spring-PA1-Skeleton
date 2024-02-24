




class Solution:
    def reverse(self, head, tail):
        pre = head
        cur = pre.next
        first = cur
        while cur != tail:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = pre
        first.next = tail
        return first

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        tail = dummy_head.next
        index = 0
        while tail:
            index += 1
            if index % k == 0:
                cur = self.reverse(cur, tail.next)
                tail = cur.next
            else:
                tail = tail.next
        return dummy_head.next