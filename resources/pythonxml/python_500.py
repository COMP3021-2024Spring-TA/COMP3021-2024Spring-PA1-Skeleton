class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums_dict = dict()
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in nums_dict:
                    nums_dict[sum] += 1
                else:
                    nums_dict[sum] = 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                sum = num3 + num4
                if -sum in nums_dict:
                    count += nums_dict[-sum]

        return count