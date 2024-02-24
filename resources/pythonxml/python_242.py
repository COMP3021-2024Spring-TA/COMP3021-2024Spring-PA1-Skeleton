class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res