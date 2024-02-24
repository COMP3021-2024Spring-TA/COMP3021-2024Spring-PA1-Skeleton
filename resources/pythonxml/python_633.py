class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return None
            if node.left and not node.left.left and not node.left.right:
                self.ans += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans