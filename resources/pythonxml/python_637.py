class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        ans = 0
        for i in range(n):
            line_dict = dict()
            line_dict[0] = 0
            same = 1
            for j in range(i+1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                gcd_dx_dy = math.gcd(abs(dx), abs(dy))
                if (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                    dx = abs(dx) // gcd_dx_dy
                    dy = abs(dy) // gcd_dx_dy
                elif dx < 0 and dy > 0:
                    dx = -dx // gcd_dx_dy
                    dy = -dy // gcd_dx_dy
                elif dx > 0 and dy < 0:
                    dx = dx // gcd_dx_dy
                    dy = dy // gcd_dx_dy
                elif dx == 0 and dy != 0:
                    dy = 1
                elif dx != 0 and dy == 0:
                    dx = 1
                key = (dx, dy)
                if key in line_dict:
                    line_dict[key] += 1
                else:
                    line_dict[key] = 1
            ans = max(ans, same + max(line_dict.values()))
        return ans