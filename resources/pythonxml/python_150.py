class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            ans = guess(mid)
            if ans == 1:
                left = mid + 1
            elif ans == -1:
                right = mid - 1
            else:
                return mid
        return 0