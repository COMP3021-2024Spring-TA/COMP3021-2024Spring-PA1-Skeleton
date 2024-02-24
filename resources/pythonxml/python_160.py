class Solution:
    def totalDigits(self, x):
        digits = 0
        digit, cnt = 1, 9
        while digit <= x:
            digits += digit * cnt
            digit += 1
            cnt *= 10
        return digits

    def findNthDigit(self, n: int) -> int:
        left, right = 1, 9
        while left < right:
            mid = left + (right - left) // 2
            if self.totalDigits(mid) < n:
                left = mid + 1
            else:
                right = mid

        digit = left
        pre_digits = self.totalDigits(digit - 1)
        idx = n - pre_digits - 1
        number = 10 ** (digit - 1) + idx // digit
        digit_idx = idx % digit
    
        return int(str(number)[digit_idx])