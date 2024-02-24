class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = collections.deque([root])
        is_empty = False
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    is_empty = True
                else:
                    if is_empty:
                        return False
                    queue.append(cur.left)
                    queue.append(cur.right)
        return True