class Solution:
    def dfs(self, root: TreeNode):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        val_steal = root.val + left[1] + right[1]
        val_no_steal = max(left[0], left[1]) + max(right[0], right[1])
        return [val_steal, val_no_steal]
    def rob(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])