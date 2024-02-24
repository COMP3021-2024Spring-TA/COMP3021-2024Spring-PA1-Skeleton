class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digit += 1
            start *= 10
            base = start * digit * 9

        number = start + (n - 1) // digit
        digit_idx = (n - 1) % digit
        return int(str(number)[digit_idx])