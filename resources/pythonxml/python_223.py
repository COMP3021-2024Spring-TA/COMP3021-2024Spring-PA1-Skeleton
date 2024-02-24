class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if ans == 0:
                    continue
                else:
                    return ans
            else:
                ans += 1
        return ans