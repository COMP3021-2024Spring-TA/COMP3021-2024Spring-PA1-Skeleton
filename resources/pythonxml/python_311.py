class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        size = len(nums)
        left = 0
        right = 0
        window_product = 1
        
        count = 0
        
        while right < size:
            window_product *= nums[right]

            while window_product >= k:
                window_product /= nums[left]
                left += 1

            count += (right - left + 1)
            right += 1
            
        return count