class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        cross1 = (x2 - x1) * (y3 - y2)
        cross2 = (x3 - x2) * (y2 - y1)
        return cross1 - cross2 != 0