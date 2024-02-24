class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeset = set()

        while head:
            if head in nodeset:
                return True
            nodeset.add(head)
            head = head.next
        return False