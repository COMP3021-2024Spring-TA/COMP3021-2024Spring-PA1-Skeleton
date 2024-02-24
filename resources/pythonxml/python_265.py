class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)
        left, right = 0, size - 1
        ans = 0
        while left < right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            ans += 1
        if left == right:
            ans += 1
        return ans