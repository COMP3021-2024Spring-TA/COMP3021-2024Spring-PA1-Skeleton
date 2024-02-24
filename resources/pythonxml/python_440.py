class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node: 'Node'):
            if not node:
                return

            dfs(node.left)
            if self.tail:
                self.tail.right = node
                node.left = self.tail
            else:
                self.head = node
            self.tail = node
            dfs(node.right)

        if not root:
            return None

        self.head, self.tail = None, None
        dfs(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head