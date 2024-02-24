class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        cur_diff = 0
        pre_diff = 0
        res = 1
        for i in range(size - 1):
            cur_diff = nums[i + 1] - nums[i]
            if (cur_diff > 0 and pre_diff <= 0) or (pre_diff >= 0 and cur_diff < 0):
                res += 1
                pre_diff = cur_diff
        return res