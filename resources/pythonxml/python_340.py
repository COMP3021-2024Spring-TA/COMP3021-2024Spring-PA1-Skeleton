class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hand_map = collections.defaultdict(int)
        for i in range(len(nums)):
            hand_map[nums[i]] += 1
        for key in sorted(hand_map.keys()):
            value = hand_map[key]
            if value == 0:
                continue
            count = 0
            for i in range(k):
                hand_map[key + count] -= value
                if hand_map[key + count] < 0:
                    return False
                count += 1
        return True