class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digits += 1
            start *= 10
            base = start * digits * 9

        number = start + (n - 1) // digits
        idx = (n - 1) % digits
        return int(str(number)[idx])