class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root