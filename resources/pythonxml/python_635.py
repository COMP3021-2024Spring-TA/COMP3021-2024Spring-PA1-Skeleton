class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        return x == res or x == res // 10