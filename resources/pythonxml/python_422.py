class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ord('A') <= ord(ch) <= ord('Z'):
                ans += chr(ord(ch) + 32)
            else:
                ans += ch
        return ans