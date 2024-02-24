class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for point_i in points:
            dis_dict = dict()
            for point_j in points:
                if point_i != point_j:
                    dx = point_i[0] - point_j[0]
                    dy = point_i[1] - point_j[1]
                    dis = dx * dx + dy * dy
                    if dis in dis_dict:
                        dis_dict[dis] += 1
                    else:
                        dis_dict[dis] = 1
            for value in dis_dict.values():
                ans += value*(value-1)
        return ans