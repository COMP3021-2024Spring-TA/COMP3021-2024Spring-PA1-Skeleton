class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        size = len(arr)
        res = 0
        for i in range(1, size - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < size - 1 and arr[right + 1] < arr[right]:
                    right += 1
                if right - left + 1 > res:
                    res = right - left + 1
        return res