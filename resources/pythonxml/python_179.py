class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        mmax, mmin = 0, 0
        for num in nums:
            mmax = max(mmax, 0) + num
            mmin = min(mmin, 0) + num
            ans = max(ans, mmax, -mmin)

        return ans