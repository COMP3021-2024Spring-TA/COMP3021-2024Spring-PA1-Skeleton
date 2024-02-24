class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        subMax = nums[0]
        ansMax = nums[0]

        for i in range(1, size):
            if subMax < 0:
                subMax = nums[i]
            else:
                subMax += nums[i]
            ansMax = max(ansMax, subMax)
        return ansMax