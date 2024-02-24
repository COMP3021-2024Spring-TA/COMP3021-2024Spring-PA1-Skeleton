class Solution:
    def inOrder(self, root, res):
        if not root:
            return
        self.inOrder(root.left, res)
        res.append(root)
        self.inOrder(root.right, res)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        self.inOrder(root, res)

        if not res:
            return
        head = TreeNode(-1)
        cur = head
        for node in res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return head.right