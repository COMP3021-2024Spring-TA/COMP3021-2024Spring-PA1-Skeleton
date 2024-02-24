class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        return product - total