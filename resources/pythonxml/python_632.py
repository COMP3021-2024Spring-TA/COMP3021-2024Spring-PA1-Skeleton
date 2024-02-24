class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if root == None:
                return False
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight-rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight)+1
        return height(root) >= 0