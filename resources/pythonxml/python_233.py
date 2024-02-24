class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        max_num, min_num = 0, 14
        repeat = set()
        for num in nums:
            if num == 0:
                continue
            if num in repeat:
                return False
            repeat.add(num)
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        return max_num - min_num <= 4