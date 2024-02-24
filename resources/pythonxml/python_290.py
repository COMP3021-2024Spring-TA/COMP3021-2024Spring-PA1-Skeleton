class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_dict = dict()
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            node_dict[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                node_dict[curr].next = node_dict[curr.next]
            if curr.random:
                node_dict[curr].random = node_dict[curr.random]
            curr = curr.next
        return node_dict[head]