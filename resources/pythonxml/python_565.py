class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        letterSet = set()
        right = 0
        ans = 0
        for i in range(len(s)):
            if i != 0:
                letterSet.remove(s[i - 1])
            while right < len(s) and s[right] not in letterSet:
                letterSet.add(s[right])
                right += 1
            ans = max(ans, right - i)
        return ans