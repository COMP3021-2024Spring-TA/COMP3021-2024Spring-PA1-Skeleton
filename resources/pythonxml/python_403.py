class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2, len(s)):
            if s[i - 2] != s[i - 1] and s[i - 1] != s[i] and s[i - 2] != s[i]:
                ans += 1
        return ans