class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index_g, index_s = 0, 0
        res = 0
        while index_g < len(g) and index_s < len(s):
            if g[index_g] <= s[index_s]:
                res += 1
                index_g += 1
                index_s += 1
            else:
                index_s += 1   

        return res