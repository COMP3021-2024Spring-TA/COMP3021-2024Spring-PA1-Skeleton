class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        isOdd = True

        curr = head.next.next

        while curr:
            if isOdd:
                odd.next = curr
                odd = curr
            else:
                even.next = curr
                even = curr
            isOdd = not isOdd
            curr = curr.next
        odd.next = evenHead
        even.next = None
        return head