class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < -asteroid:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()

        return stack