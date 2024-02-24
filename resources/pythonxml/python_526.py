class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        left_cnt = 0
        for ch in s:
            if ch == '(':
                left_cnt += 1
            elif ch == ')':
                left_cnt -= 1
                if left_cnt == -1:
                    left_cnt = 0
                    res += 1
        res += left_cnt
        return res