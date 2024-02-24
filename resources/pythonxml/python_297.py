class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        prefix_sum = 0
        for i in range(len(nums)):
            if 2 * prefix_sum + nums[i] == total:
                return i
            prefix_sum += nums[i]
        
        return -1