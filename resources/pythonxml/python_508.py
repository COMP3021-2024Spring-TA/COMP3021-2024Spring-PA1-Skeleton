class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        size1 = len(slots1)
        size2 = len(slots2)
        left_1, left_2 = 0, 0
        while left_1 < size1 and left_2 < size2:
            start_1, end_1 = slots1[left_1]
            start_2, end_2 = slots2[left_2]
            start = max(start_1, start_2)
            end = min(end_1, end_2)
            if end - start >= duration:
                return [start, start + duration]
            if end_1 < end_2:
                left_1 += 1
            else:
                left_2 += 1
        return []