class Solution:
    def binarySearch(self, reader, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if target > reader.get(mid):
                left = mid + 1
            else:
                right = mid
        if reader.get(left) == target:
            return left
        else:
            return -1

    def search(self, reader, target):
        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        return self.binarySearch(reader, left, right, target)