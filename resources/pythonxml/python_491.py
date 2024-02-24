class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(datalist):
            val = datalist.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(datalist)
            root.right = dfs(datalist)
            return root

        datalist = data.split(',')
        return dfs(datalist)