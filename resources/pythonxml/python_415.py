





class Solution:
    def __init__(self):
        self.ans = float('-inf')
        
    def dfs(self, node):
        if not node:
            return 0
        left_max = max(self.dfs(node.left), 0)     
        right_max = max(self.dfs(node.right), 0)   

        cur_max = left_max + right_max + node.val  
        self.ans = max(self.ans, cur_max)          

        return max(left_max, right_max) + node.val 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans