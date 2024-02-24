class Solution:
    pre = 0

    def createBinaryTree(self, root: TreeNode):
        if not root:
            return
        self.createBinaryTree(root.right)
        root.val += self.pre
        self.pre = root.val
        self.createBinaryTree(root.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.pre = 0
        self.createBinaryTree(root)
        return root