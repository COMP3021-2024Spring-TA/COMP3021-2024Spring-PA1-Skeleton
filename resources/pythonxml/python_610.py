class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        if root:
            node_left = self.lowestCommonAncestor(root.left, p, q)
            node_right = self.lowestCommonAncestor(root.right, p, q)
            if node_left and node_right:
                return root
            elif not node_left:
                return node_right
            else:
                return node_left
        return None