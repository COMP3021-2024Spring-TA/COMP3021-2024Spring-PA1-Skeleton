class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                left = mid
                break
        return left * left == num