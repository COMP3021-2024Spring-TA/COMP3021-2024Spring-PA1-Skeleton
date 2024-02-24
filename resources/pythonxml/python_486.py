class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0

        
        if root.left == None and root.right == None:
            return 1

        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        
        min_depth = 0xffffff
        if root.left:
            min_depth = min(leftHeight, min_depth)
        if root.right:
            min_depth = min(rightHeight, min_depth)

        
        return min_depth + 1