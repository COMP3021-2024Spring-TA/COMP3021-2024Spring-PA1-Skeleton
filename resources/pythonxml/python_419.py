class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.sum(root, targetSum, 0)

    def sum(self, root: TreeNode, targetSum: int, curSum:int) -> bool:
        if root == None:
            return False
        curSum += root.val
        if root.left == None and root.right == None:
            return curSum == targetSum
        else:
            return self.sum(root.left, targetSum, curSum) or self.sum(root.right, targetSum, curSum)