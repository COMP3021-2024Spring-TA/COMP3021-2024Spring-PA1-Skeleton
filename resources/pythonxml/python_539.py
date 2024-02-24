class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
        return root