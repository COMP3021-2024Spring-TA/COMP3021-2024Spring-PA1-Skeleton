class Solution:
    def numSubarrayMaxK(self, nums, k):
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] <= k:
                count += 1
            else:
                count = 0
            ans += count
        return ans

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        return self.numSubarrayMaxK(nums, right) - self.numSubarrayMaxK(nums, left - 1)