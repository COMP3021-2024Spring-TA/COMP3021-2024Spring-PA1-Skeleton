class Solution:
    def merge_sort(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.merge_sort(head, mid), self.merge_sort(mid, tail))

    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        root = ListNode(-1)
        cur = root
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        if a:
            cur.next = a
        if b:
            cur.next = b
        return root.next

    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head, None)