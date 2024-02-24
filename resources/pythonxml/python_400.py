class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return 'None'

        data = str(root.val) + '-' + str(len(root.children))
        for child in root.children:
            data += '-' + self.serialize(child)
        return data
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        datalist = data.split('-')
        return self.dfs(datalist)

    def dfs(self, datalist):
        val = datalist.pop(0)
        if val == 'None':
            return None
        root = Node(int(val))
        root.children = []

        size = int(datalist.pop(0))
        for _ in range(size):
            root.children.append(self.dfs(datalist))
        return root