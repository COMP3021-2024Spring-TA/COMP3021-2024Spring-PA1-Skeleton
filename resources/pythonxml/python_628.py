class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = [root]
        
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.val)
                for child in cur.children:
                    queue.append(child)
            ans.append(level)

        return ans