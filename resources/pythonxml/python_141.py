class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        ans = 1

        while right < len(arr):
            if arr[right - 1] == arr[right]:
                left = right
            elif right != 1 and arr[right - 2] < arr[right - 1] and arr[right - 1] < arr[right]:
                left = right - 1
            elif right != 1 and arr[right - 2] > arr[right - 1] and arr[right - 1] > arr[right]:
                left = right - 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans