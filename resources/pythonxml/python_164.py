class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        node = head
        while node.next != head:
            if node.val <= insertVal <= node.next.val:
                break
            elif node.next.val < node.val <= insertVal:
                break
            elif insertVal < node.next.val < node.val:
                break
            else:
                node = node.next

        insert_node = Node(insertVal)
        insert_node.next = node.next
        node.next = insert_node
        return head