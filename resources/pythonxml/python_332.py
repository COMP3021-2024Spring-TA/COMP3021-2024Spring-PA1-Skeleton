class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        degrees = collections.Counter()

        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1

        for i in range(1, n + 1):
            if degrees[i] == n - 1:
                return i
        return -1