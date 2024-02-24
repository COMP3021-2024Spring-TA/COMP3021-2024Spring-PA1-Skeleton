class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 2
        res = []
        while left < right:
            sum = (left + right) * (right - left + 1) // 2
            if sum == target:
                arr = []
                for i in range(0, right - left + 1):
                    arr.append(i + left)
                res.append(arr)
                left += 1
            elif sum < target:
                right += 1
            else:
                left += 1
        return res