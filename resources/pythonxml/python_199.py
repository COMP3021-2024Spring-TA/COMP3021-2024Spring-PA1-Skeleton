class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_diff, min_sum = 0, float('inf')
        for i in range(len(gas)):
            sum_diff += gas[i] - cost[i]
            min_sum = min(min_sum, sum_diff)

        if sum_diff < 0:
            return -1

        if min_sum >= 0:
            return 0

        for i in range(len(gas)-1, -1, -1):
            min_sum += gas[i] - cost[i]
            if min_sum >= 0:
                return i
        return -1