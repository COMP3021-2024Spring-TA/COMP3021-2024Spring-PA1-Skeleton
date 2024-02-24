class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        order = []
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                order.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return order