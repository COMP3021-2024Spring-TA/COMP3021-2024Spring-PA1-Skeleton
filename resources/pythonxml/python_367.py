class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def dfs(self, root):
        if not root:
            return 0
        left_max = max(self.dfs(root.left), 0)
        right_max = max(self.dfs(root.right), 0)
        self.max_sum = max(self.max_sum, root.val + left_max + right_max)
        return root.val + max(left_max, right_max)

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_sum