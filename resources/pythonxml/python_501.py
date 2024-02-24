class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans = 0
        flip_count = 0
        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == 2:
                flip_count -= 1
            if (flip_count + nums[i]) % 2 == 0:
                if i + k > len(nums):
                    return -1
                nums[i] = 2
                flip_count += 1
                ans += 1
        return ans