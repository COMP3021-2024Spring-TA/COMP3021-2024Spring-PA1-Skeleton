class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        start = 0
        end = 0
        sum = 0
        ans = n + 1
        while end < n:
            sum += nums[end]
            while sum >= target:
                ans = min(ans, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1
        if ans == n + 1:
            return 0
        else:
            return ans