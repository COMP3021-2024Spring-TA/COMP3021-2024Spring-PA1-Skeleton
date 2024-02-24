class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = nums[0]
        ans = 0
        for num in nums:
            ans = max(ans + num, num)
            max_ans = max(max_ans, ans)
        return max_ans