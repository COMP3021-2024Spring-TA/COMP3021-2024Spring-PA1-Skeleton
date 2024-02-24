class Solution:
    def merge_sort(self, lists: List[ListNode], left: int, right: int) -> ListNode:
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        node_left = self.merge_sort(lists, left, mid)
        node_right = self.merge_sort(lists, mid + 1, right)
        return self.merge(node_left, node_right)

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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        size = len(lists)
        return self.merge_sort(lists, 0, size - 1)