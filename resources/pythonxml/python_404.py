class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = dict()
        for jewel in jewels:
            jewel_dict[jewel] = 1
        count = 0
        for stone in stones:
            if stone in jewel_dict:
                count += 1
        return count