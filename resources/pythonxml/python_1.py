class Solution:
    def sectionSort(self, head: ListNode):
        node_i = head
        
        while node_i and node_i.next:
            
            min_node = node_i
            node_j = node_i.next
            while node_j:
                if node_j.val < min_node.val:
                    min_node = node_j
                node_j = node_j.next
            
            if node_i != min_node:
                node_i.val, min_node.val = min_node.val, node_i.val
            node_i = node_i.next
        
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sectionSort(head)