class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        x1, y1 = points[0]
        for point in points:
            x2, y2 = point
            ans += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = point
        
        return ans    