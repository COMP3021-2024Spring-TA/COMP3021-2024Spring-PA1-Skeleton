class Solution:
    def hasSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.hasSubStructure(A.left, B.left) and self.hasSubStructure(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if self.hasSubStructure(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)