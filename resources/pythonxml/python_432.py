class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid

        return left