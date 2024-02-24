class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        size = len(nums)
        left, right = 0, 0
        count = 0
        product = 1
        while right < size:
            product *= nums[right]
            right += 1
            while product >= k:
                product /= nums[left]
                left += 1
            count += (right - left)
        return count