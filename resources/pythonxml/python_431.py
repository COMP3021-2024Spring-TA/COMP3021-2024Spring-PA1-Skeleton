





class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, node):
        if not node:
            return 0
        left_height = self.dfs(node.left)                     
        right_height = self.dfs(node.right)                   
        self.ans = max(self.ans, left_height + right_height)  
        return max(left_height, right_height) + 1             

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans