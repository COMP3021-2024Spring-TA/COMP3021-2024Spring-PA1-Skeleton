class Solution:
    res = 0
    def traversal(self, cur: TreeNode) -> int:
        if not cur:
            return 3

        left = self.traversal(cur.left)
        right = self.traversal(cur.right)

        if left == 1 or right == 1:
            self.res += 1
            return 2

        if left == 2 or right == 2:
            return 3

        if left == 3 and right == 3:
            return 1
        return -1

    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        if self.traversal(root) == 1:
            self.res += 1
        return self.res