class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True