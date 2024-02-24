class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        size = len(arr)
        if size <= 2:
            return True

        arr.sort()
        for i in range(2, size):
            if arr[i] - arr[i - 1] != arr[i - 1] - arr[i - 2]:
                return False
        return True