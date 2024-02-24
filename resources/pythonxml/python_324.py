class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left = right
        root.right = left
        return root