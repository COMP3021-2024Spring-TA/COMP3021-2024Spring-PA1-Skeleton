class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        left_1 = 0
        left_2 = 0
        res = []
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] == nums2[left_2]:
                if nums1[left_1] not in res:
                    res.append(nums1[left_1])
                left_1 += 1
                left_2 += 1
            elif nums1[left_1] < nums2[left_2]:
                left_1 += 1
            elif nums1[left_1] > nums2[left_2]:
                left_2 += 1
        return res