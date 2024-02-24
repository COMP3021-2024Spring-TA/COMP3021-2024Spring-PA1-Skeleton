class CBTInserter:

    def __init__(self, root: TreeNode):
        self.queue = [root]
        self.nodelist = [None]

        while self.queue:
            node = self.queue.pop(0)
            self.nodelist.append(node)
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)


    def insert(self, v: int) -> int:
        self.nodelist.append(TreeNode(v))
        index = len(self.nodelist) - 1
        father = self.nodelist[index // 2]
        if index % 2 == 0:
            father.left = self.nodelist[-1]
        else:
            father.right = self.nodelist[-1]
        return father.val


    def get_root(self) -> TreeNode:
        return self.nodelist[1]