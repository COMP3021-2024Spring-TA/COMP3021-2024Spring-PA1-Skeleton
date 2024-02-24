class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        dist = 0
        for i in range(len(distance)):
            if start <= i < destination:
                dist += distance[i]
        
        return min(dist, sum(distance) - dist)