class Solution:
    def arraySign(self, nums: List[int]) -> int:
        minus_count = 0
        for num in nums:
            if num < 0:
                minus_count += 1
            elif num == 0:
                return 0

        if minus_count % 2 == 0:
            return 1
        else:
            return -1