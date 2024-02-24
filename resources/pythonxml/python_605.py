class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        max_i = 0
        for i in range(size):
            if max_i >= i and i + nums[i] > max_i:
                max_i = i + nums[i]
            
        return max_i >= size - 1