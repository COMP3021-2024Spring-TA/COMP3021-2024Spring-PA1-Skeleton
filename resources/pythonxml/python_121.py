
class TreeNode:
    def __init__(self, left=-1, right=-1, val=0):
        self.left = left                            
        self.right = right                          
        self.mid = left + (right - left) // 2
        self.leftNode = None                        
        self.rightNode = None                       
        self.val = val                              
        self.lazy_tag = None                        
        
        

class SegmentTree:
    def __init__(self, function):
        self.tree = TreeNode(0, int(1e9))
        self.function = function                    
            
    
    def __pushup(self, node):
        leftNode = node.leftNode
        rightNode = node.rightNode
        if leftNode and rightNode:
            node.val = self.function(leftNode.val, rightNode.val)
            
    
    def update_point(self, i, val):
        self.__update_point(i, val, self.tree)
        
    
    def __update_point(self, i, val, node):
        if node.left == node.right:
            node.val = val                          
            return
        
        if i <= node.mid:                           
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_point(i, val, node.leftNode)
        else:                                       
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_point(i, val, node.rightNode)
        self.__pushup(node)                         
        
    
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)
    
    
    def __query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:   
            return node.val                         
        if node.right < q_left or node.left > q_right:  
            return 0
                                  
        self.__pushdown(node)                       
        
        res_left = 0                                
        res_right = 0                               
        if q_left <= node.mid:                      
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:                      
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   
    
    
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)
        
    
    def __update_interval(self, q_left, q_right, val, node):
        if node.left >= q_left and node.right <= q_right:  
            if node.lazy_tag:
                node.lazy_tag += val                
            else:
                node.lazy_tag = val                 
            interval_size = (node.right - node.left + 1)    
            node.val += val * interval_size         
            return
        if node.right < q_left or node.left > q_right:  
            return 0
    
        self.__pushdown(node)                       
    
        if q_left <= node.mid:                      
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:                      
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_interval(q_left, q_right, val, node.rightNode)
            
        self.__pushup(node)
    
    
    def __pushdown(self, node):
        lazy_tag = node.lazy_tag
        if not node.lazy_tag:
            return
        
        if not node.leftNode:
            node.leftNode = TreeNode(node.left, node.mid)
        if not node.rightNode:
            node.rightNode = TreeNode(node.mid + 1, node.right)
            
        if node.leftNode.lazy_tag:
            node.leftNode.lazy_tag += lazy_tag      
        else:
            node.leftNode.lazy_tag = lazy_tag       
        left_size = (node.leftNode.right - node.leftNode.left + 1)
        node.leftNode.val += lazy_tag * left_size   
        
        if node.rightNode.lazy_tag:
            node.rightNode.lazy_tag += lazy_tag     
        else:
            node.rightNode.lazy_tag = lazy_tag      
        right_size = (node.rightNode.right - node.rightNode.left + 1)
        node.rightNode.val += lazy_tag * right_size 
        
        node.lazy_tag = None                        