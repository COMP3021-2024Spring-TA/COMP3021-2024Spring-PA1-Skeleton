class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x):
            visited.add(x)
            for key in rooms[x]:
                if key not in visited:
                    dfs(key)
        visited = set()
        dfs(0)
        return len(visited) == len(rooms)