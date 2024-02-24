class Solution:
    def bubbleSort(self, head: ListNode):
        node_i = head
        tail = None
        
        while node_i:
            node_j = head
            while node_j and node_j.next != tail:
                if node_j.val > node_j.next.val:
                    
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            
            tail = node_j
            node_i = node_i.next
            
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bubbleSort(head)