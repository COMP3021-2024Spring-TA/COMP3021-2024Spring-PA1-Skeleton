class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False

        queue = collections.deque([[root, 0]])
        ans = 0
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            size = len(queue)
            for _ in range(size):
                cur, index = queue.popleft()
                if cur.left:
                    queue.append([cur.left, index * 2 + 1])
                if cur.right:
                    queue.append([cur.right, index * 2 + 2])
        return ans