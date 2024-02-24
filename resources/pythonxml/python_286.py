class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        size = len(startTime)
        for i in range(size):
            if startTime[i] <= queryTime <= endTime[i]:
                cnt += 1
        return cnt