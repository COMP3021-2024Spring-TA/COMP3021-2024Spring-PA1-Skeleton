class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root

        if root.val > val:
            root.left = self.deleteNode(root.left, val)
            return root
        elif root.val < val:
            root.right = self.deleteNode(root.right, val)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right