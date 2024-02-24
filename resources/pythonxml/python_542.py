class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size = len(s1)
        diff_cnt = 0
        c1, c2 = None, None
        for i in range(size):
            if s1[i] == s2[i]:
                continue
            diff_cnt += 1
            if diff_cnt == 1:
                c1 = s1[i]
                c2 = s2[i]
            elif diff_cnt == 2:
                if c1 != s2[i] or c2 != s1[i]:
                    return False
            else:
                return False

        return diff_cnt == 0 or diff_cnt == 2