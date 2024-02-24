class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        num_map = dict()
        for num in nums2:
            while stack and num > stack[-1]:
                num_map[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for num in nums1:
            res.append(num_map.get(num, -1))
        return res