class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode, res: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)

        res1 = []
        dfs(root1, res1)
        res2 = []
        dfs(root2, res2)
        return res1 == res2