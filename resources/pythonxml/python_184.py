class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not p or not root:
            return None

        if root.val <= p.val:
            node = self.inorderSuccessor(root.right, p)
        else:
            node = self.inorderSuccessor(root.left, p)
            if not node:
                node = root
        return node