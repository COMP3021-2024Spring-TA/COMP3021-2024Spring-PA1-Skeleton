class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans