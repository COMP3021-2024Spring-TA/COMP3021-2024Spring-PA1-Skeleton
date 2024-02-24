class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        cnt = 1
        size = len(s)
        for i in range(1, size):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                if cnt >= 3:
                    res.append([i - cnt, i - 1])
                cnt = 1
        if cnt >= 3:
            res.append([size - cnt, size - 1])
        return res