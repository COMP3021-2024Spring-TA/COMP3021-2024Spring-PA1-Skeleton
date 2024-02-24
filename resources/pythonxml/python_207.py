class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                count += (nums[j] >> i) & 1
            if count % 3 != 0:
                if i == 31:
                    ans -= (1 << 31)
                else:
                    ans = ans | 1 << i
        return ans