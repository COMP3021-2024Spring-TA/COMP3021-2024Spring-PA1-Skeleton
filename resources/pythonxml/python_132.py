class Solution:
    def containsOnlyZero(self, root: TreeNode):
        if not root:
            return True
        if root.val == 1:
            return False
        return self.containsOnlyZero(root.left) and self.containsOnlyZero(root.right)

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if self.containsOnlyZero(root):
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root