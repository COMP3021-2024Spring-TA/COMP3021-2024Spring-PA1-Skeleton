class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                
            return []
        
        res = []
        stack = []

        while root or stack:        
            while root:
                stack.append(root)  
                root = root.left    
            
            node = stack.pop()      
            res.append(node.val)    
            root = node.right       
        return res