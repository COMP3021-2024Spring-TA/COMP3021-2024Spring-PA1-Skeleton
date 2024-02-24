class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            if abs(target - root.val) < abs(target - closest):
                closest = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest