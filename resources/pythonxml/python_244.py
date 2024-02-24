class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in range(len(node.children) - 1, -1, -1):
                if node.children[i]:
                    stack.append(node.children[i])
        return res