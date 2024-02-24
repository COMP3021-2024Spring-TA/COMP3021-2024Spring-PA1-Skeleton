class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)

        dp_max, dp_min = nums[0], nums[0]
        max_num, min_num = nums[0], nums[0]
        for i in range(1, size):
            dp_max = max(dp_max + nums[i], nums[i])
            dp_min = min(dp_min + nums[i], nums[i])
            max_num = max(dp_max, max_num)
            min_num = min(dp_min, min_num)
        sum_num = sum(nums)
        if max_num < 0:
            return max_num
        return max(sum_num - min_num, max_num)