class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False