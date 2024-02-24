class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def preorderTraversal(root, min_v, max_v):
            if root == None:
                return True
            if root.val >= max_v or root.val <= min_v:
                return False
            return preorderTraversal(root.left, min_v, root.val) and preorderTraversal(root.right, root.val, max_v)

        return preorderTraversal(root, float('-inf'), float('inf'))