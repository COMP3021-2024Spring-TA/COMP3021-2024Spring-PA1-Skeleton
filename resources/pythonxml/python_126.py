class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode):
        if left == None and right == None:
            return True
        elif left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)