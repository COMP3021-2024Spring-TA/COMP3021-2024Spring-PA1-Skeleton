class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_sub_array(low, high):
            if low == high:
                return nums[low]

            mid = low + (high - low) // 2
            leftMax = max_sub_array(low, mid)
            rightMax = max_sub_array(mid + 1, high)

            total = 0
            leftTotal = -inf
            for i in range(mid, low - 1, -1):
                total += nums[i]
                leftTotal = max(leftTotal, total)
            
            total = 0
            rightTotal = -inf
            for i in range(mid + 1, high + 1):
                total += nums[i]
                rightTotal = max(rightTotal, total)
            
            return max(leftMax, rightMax, leftTotal + rightTotal)
        
        return max_sub_array(0, len(nums) - 1)