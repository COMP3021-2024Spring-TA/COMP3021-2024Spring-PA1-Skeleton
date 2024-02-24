class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        n = len(nums)
        return (n + 1) * n // 2 - sum_nums