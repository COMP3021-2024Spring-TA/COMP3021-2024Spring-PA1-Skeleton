class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
            elif not root.right:
                dfs(root.left, path + "->")
            elif not root.left:
                dfs(root.right, path + "->")
            else:
                dfs(root.left, path + "->")
                dfs(root.right, path + "->")
        dfs(root, "")
        return res