class Solution:
    def dfs(self, node: 'Node'):
        
        while node.next and not node.child:
            node = node.next
        tail = None
        if node.child:
            
            tail = self.dfs(node.child)

            
            temp = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None
            tail.next = temp
            if temp:
                temp.prev = tail
            
            return self.dfs(tail)
        
        return node
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.dfs(head)
        return head