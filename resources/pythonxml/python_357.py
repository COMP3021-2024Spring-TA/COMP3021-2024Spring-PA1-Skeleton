class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right :
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1