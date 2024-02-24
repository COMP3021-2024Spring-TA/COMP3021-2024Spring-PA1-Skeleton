class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        slow, fast = 0, 0
        while fast < size:
            if arr[slow] == 0:
                fast += 1
            slow += 1
            fast += 1
        
        slow -= 1 
        fast -= 1 

        while slow >= 0:
            if fast < size: 
                arr[fast] = arr[slow] 
            if arr[slow] == 0 and fast >= 0: 
                fast -= 1
                arr[fast] = arr[slow]
            fast -= 1
            slow -= 1