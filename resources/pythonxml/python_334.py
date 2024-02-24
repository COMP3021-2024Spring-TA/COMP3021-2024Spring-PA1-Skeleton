class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depths = [0, 0]
        parents = [None, None]

        def dfs(node, depth, parent):
            if not node:
                return
            if node.val == x:
                depths[0] = depth
                parents[0] = parent
            elif node.val == y:
                depths[1] = depth
                parents[1] = parent
            dfs(node.left, depth+1, node)
            dfs(node.right, depth+1, node)

        dfs(root, 0, None)
        return depths[0] == depths[1] and parents[0] != parents[1]