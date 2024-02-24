class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev = None                 
        
        while root or stack:        
            while root:
                stack.append(root)  
                root = root.left    

            node = stack.pop()      

            
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node         
                root = None         
            else:
                stack.append(node)  
                root = node.right   
                
        return res