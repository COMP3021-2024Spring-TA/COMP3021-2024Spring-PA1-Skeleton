




class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        cur = dummy_head
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        return dummy_head.next