class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def get_count(dist):
            left, count = 0, 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > dist:
                    left += 1
                count += (right - left)
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left