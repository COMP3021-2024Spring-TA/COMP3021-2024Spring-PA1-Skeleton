class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans, size = 0, len(nums)
        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[size - 1 - i])
        
        return ans