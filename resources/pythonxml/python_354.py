class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        min_x, min_y = 200, 200
        max_x, max_y = 0, 0
        for circle in circles:
            if circle[0] + circle[2] > max_x:
                max_x = circle[0] + circle[2]
            if circle[0] - circle[2] < min_x:
                min_x = circle[0] - circle[2]
            if circle[1] + circle[2] > max_y:
                max_y = circle[1] + circle[2]
            if circle[1] - circle[2] < min_y:
                min_y = circle[1] - circle[2]
        
        ans = 0
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for xi, yi, ri in circles:
                    if (xi - x) * (xi - x) + (yi - y) * (yi - y) <= ri * ri:
                        ans += 1
                        break
        
        return ans