class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = []
        res = []
        if root:
            queue.append(root)
        while queue:
            max_level = float('-inf')
            size_level = len(queue)
            for i in range(size_level):
                node = queue.pop(0)
                max_level = max(max_level, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_level)
        return res