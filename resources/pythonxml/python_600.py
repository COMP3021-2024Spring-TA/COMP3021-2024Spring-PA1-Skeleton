





class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        levels = []
        while queue:
            level = 0
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                level += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levels.append(level)
        return levels

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = self.levelOrder(root)
        max_sum = max(levels)
        for i in range(len(levels)):
            if levels[i] == max_sum:
                return i + 1