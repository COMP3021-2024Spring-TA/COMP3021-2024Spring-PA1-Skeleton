class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set(candyType)
        return min(len(candyType) // 2, len(candy_set))