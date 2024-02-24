class Solution:
    res = []
    count = 0
    max_count = 0
    pre = None
    def search(self, cur: TreeNode):
        if not cur:
            return
        self.search(cur.left)
        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1

        self.pre = cur

        if self.count == self.max_count:
            self.res.append(cur.val)
        elif self.count > self.max_count:
            self.max_count = self.count
            self.res.clear()
            self.res.append(cur.val)

        self.search(cur.right)
        return

    def findMode(self, root: TreeNode) -> List[int]:
        self.count = 0
        self.max_count = 0
        self.res.clear()
        self.pre = None
        self.search(root)
        return self.res