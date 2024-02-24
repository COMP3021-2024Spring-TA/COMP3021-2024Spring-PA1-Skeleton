class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        min_index = 0
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dist < min_dist:
                    min_dist = dist
                    min_index = i

        if min_dist == float('inf'):
            return -1
        return min_index