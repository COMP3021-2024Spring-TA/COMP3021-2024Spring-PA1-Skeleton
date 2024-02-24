class Solution:
    def average(self, salary: List[int]) -> float:
        min_s, max_s = min(salary), max(salary)
        total = sum(salary) - min_s - max_s
        return total / (len(salary) - 2)