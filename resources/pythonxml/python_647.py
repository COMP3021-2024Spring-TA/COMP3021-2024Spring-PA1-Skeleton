class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        max_num, min_num = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, size):
            temp_max = max_num
            temp_min = min_num
            max_num = max(temp_max * nums[i], nums[i], temp_min * nums[i])
            min_num = min(temp_min * nums[i], nums[i], temp_max * nums[i])
            ans = max(max_num, ans)
        return ans