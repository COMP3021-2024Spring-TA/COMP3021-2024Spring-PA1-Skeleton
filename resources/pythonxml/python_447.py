class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size = len(nums)
        left, right = 0, 0
        window_len = 0
        max_len = 0
        
        while right < size:
            window_len += 1
            
            if right > 0 and nums[right - 1] >= nums[right]:
                left = right
                window_len = 1

            max_len = max(max_len, window_len)
            right += 1
            
        return max_len