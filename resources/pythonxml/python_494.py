class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()

        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]

            clone_node = Node(node.val, [])
            visited[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node)