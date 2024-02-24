
class TreeNode:
    def __init__(self, left, right, val=False, lazy_tag=None, letNode=None, rightNode=None):
        self.left = left  
        self.right = right  
        self.mid = (left + right) >> 1
        self.leftNode = letNode  
        self.rightNode = rightNode  
        self.val = val  
        self.lazy_tag = lazy_tag  


class RangeModule:

    def __init__(self):
        self.tree = TreeNode(0, int(1e9))

    
    def __pushup(self, node):
        if node.leftNode and node.rightNode:
            node.val = node.leftNode.val and node.rightNode.val
        else:
            node.val = False

    
    def __pushdown(self, node):
        if not node.leftNode:
            node.leftNode = TreeNode(node.left, node.mid)
        if not node.rightNode:
            node.rightNode = TreeNode(node.mid + 1, node.right)
        if node.lazy_tag is not None:
            node.leftNode.lazy_tag = node.lazy_tag  
            node.leftNode.val = node.lazy_tag  

            node.rightNode.lazy_tag = node.lazy_tag  
            node.rightNode.val = node.lazy_tag  

            node.lazy_tag = None  

    
    def __update_interval(self, q_left, q_right, val, node):
        if q_left <= node.left and node.right <= q_right:  
            node.lazy_tag = val  
            node.val = val  
            return

        self.__pushdown(node)

        if q_left <= node.mid:
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:
            self.__update_interval(q_left, q_right, val, node.rightNode)

        self.__pushup(node)

    
    def __query_interval(self, q_left, q_right, node):
        if q_left <= node.left and node.right <= q_right:  
            return node.val  

        
        self.__pushdown(node)

        if q_right <= node.mid:
            return self.__query_interval(q_left, q_right, node.leftNode)
        if q_left > node.mid:
            return self.__query_interval(q_left, q_right, node.rightNode)

        return self.__query_interval(q_left, q_right, node.leftNode) and self.__query_interval(q_left, q_right, node.rightNode)  


    def addRange(self, left: int, right: int) -> None:
        self.__update_interval(left, right - 1, True, self.tree)


    def queryRange(self, left: int, right: int) -> bool:
        return self.__query_interval(left, right - 1, self.tree)


    def removeRange(self, left: int, right: int) -> None:
        self.__update_interval(left, right - 1, False, self.tree)