class Solution:
    def buildTree(self, preorder, start, end):
        if start == end:
            return None
        root = preorder[start]
        mid = start + 1
        while mid < end and preorder[mid] < root:
            mid += 1
        node = TreeNode(root)
        node.left = self.buildTree(preorder, start + 1, mid)
        node.right = self.buildTree(preorder, mid, end)
        return node

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(preorder, 0, len(preorder))