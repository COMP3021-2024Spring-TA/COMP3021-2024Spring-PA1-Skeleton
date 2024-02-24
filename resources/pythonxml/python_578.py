class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            elif ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor