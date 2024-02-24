class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c ** 0.5)
        while a <= b:
            sum = a*a + b*b
            if sum == c:
                return True
            elif sum < c:
                a += 1
            else:
                b -= 1
        return False