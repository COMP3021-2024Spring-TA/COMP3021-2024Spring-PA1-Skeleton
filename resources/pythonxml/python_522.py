class Solution:
    
    def heapify(self, arr, index, end):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            
            max_index = index
            if arr[left] > arr[max_index]:
                max_index = left
            if right <= end and arr[right] > arr[max_index]:
                max_index = right
            if index == max_index:
                
                break
            arr[index], arr[max_index] = arr[max_index], arr[index]
            
            index = max_index
            left = index * 2 + 1
            right = left + 1

    
    def buildMaxHeap(self, arr):
        size = len(arr)
        
        for i in range((size - 2) // 2, -1, -1):
            self.heapify(arr, i, size - 1)
        return arr

    
    
    
    
    
    def maxHeapSort(self, arr):
        self.buildMaxHeap(arr)
        size = len(arr)
        for i in range(size):
            arr[0], arr[size-i-1] = arr[size-i-1], arr[0]
            self.heapify(arr, 0, size-i-2)
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.maxHeapSort(nums)