class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visitedDict = dict()

        def dfs(node: 'Node') -> 'Node':
            if node in visitedDict:
                return visitedDict[node]

            clone_node = Node(node.val, [])
            visitedDict[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node)