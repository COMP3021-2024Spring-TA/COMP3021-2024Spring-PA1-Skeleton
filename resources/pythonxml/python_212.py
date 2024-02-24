class Solution:
    def checkPalindrome(self, s: str, left: int, right: int):
        i, j = left, right
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.checkPalindrome(s, left + 1, right) or self.checkPalindrome(s, left, right - 1)
        return True