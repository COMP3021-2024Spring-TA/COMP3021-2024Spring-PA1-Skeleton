class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        for i in range(size):
            for j in range(i + 1, size):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return [-1, -1]